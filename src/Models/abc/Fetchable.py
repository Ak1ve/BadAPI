from __future__ import annotations

import dataclasses
import inspect
from abc import ABC, abstractmethod
from typing import TypeVar, Type, Generic, Callable, TypedDict, Union, TypeAlias
from prodict import Prodict


Self = TypeVar("Self")
Typed = TypeVar("Typed", bound=Union[Prodict, TypedDict], covariant=True)

_ClassMethod: TypeAlias = Callable


def _hook_from_json(func: _ClassMethod[[Type[Self], Typed], Self]) -> _ClassMethod[[Type[Self], Typed], Self]:
    func = getattr(func, "__func__")

    def from_json(cls: Type[Self], obj: Typed) -> Self:
        obj = Prodict(**obj) if not isinstance(obj, Prodict) else obj
        self = func(cls, obj)
        self.json = obj
        return self
    return classmethod(lambda x, y: from_json(x, y))


class FetchableMeta(type):
    def __new__(mcs, name: str, bases: tuple, dct: dict):
        dct.update({"from_json": _hook_from_json(dct["from_json"])})
        return type.__new__(mcs, name, bases, dct)


class _Fetchable(metaclass=FetchableMeta):
    @classmethod
    def from_json(cls, obj):
        pass


class Fetchable(Generic[Typed], _Fetchable):
    json: Typed

    @classmethod
    @abstractmethod
    def from_json(cls: Type[Self], obj: dict | Typed) -> Self:
        pass
