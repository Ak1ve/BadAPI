from abc import ABC, abstractmethod
from typing import TypeVar, Type, Generic, Callable, TypedDict
from prodict import Prodict


Self = TypeVar("Self")
Typed = TypeVar("Typed", bound=Prodict | TypedDict, covariant=True)


def _hook_from_json(func: Callable[[Type[Self], Typed], Self]) -> Callable[[Type[Self], Typed], Self]:
    def from_json(cls: Type[Self], obj: Typed) -> Self:
        self = func(cls, obj)
        self.json = obj
        return self
    return from_json


class FetchableMeta(type):
    def __new__(mcs, name: str, bases: tuple, dct: dict):
        dct.update({"from_json": _hook_from_json(dct["from_json"])})
        return type.__new__(mcs, name, bases, dct)


class Fetchable(ABC, Generic[Typed]):
    json: Typed

    @classmethod
    @abstractmethod
    def from_json(cls: Type[Self], obj: Typed) -> Self:
        pass
