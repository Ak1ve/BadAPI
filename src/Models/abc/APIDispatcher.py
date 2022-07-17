from __future__ import annotations

import asyncio

from aiohttp import ClientSession
from typing import Type, TypeVar, Protocol, Callable, Coroutine
from src.Models.abc.Fetchable import Fetchable

T_Fetchable = TypeVar("T_Fetchable", bound=Fetchable)

K = TypeVar("K")
T = TypeVar("T")
V = TypeVar("V")


__all__ = ("APIDispatcher",)


class APIDispatcherMeta(type):
    __instances__: dict[Type[APIDispatcher], APIDispatcher] = {}

    def __call__(cls: Type[APIDispatcher], *args, **kwargs):
        if cls not in cls.__instances__:
            cls.__instances__[cls] = super().__call__(*args, **kwargs)
        return cls.__instances__[cls]


class APIDispatcher(metaclass=APIDispatcherMeta):
    def __init__(self):
        self._session = ClientSession()

    async def fetch_json(self, link: str, as_obj: Type[T_Fetchable]) -> T_Fetchable:
        s = (await (await self._session.get(link)).json())
        return as_obj.from_json(s)

