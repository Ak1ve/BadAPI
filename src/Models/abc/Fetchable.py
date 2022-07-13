from __future__ import annotations

from abc import abstractmethod
from typing import TypeVar, Type, Generic, Callable, TypedDict, Union, TypeAlias
from prodict import Prodict


__all__ = ("Typed", "Fetchable")


Self = TypeVar("Self")
Typed = TypeVar("Typed", bound=Union[Prodict, TypedDict], covariant=True)

_ClassMethod: TypeAlias = Callable


def _hook_from_json(func: _ClassMethod[[Type[Self], Typed], Self]) -> _ClassMethod[[Type[Self], Typed], Self]:
    """
    Hooks a :class:Fetchable from_json method to convert :class:dict to :class:Prodict
    Also sets the .json property
    :param func:
    :return:
    """
    func = getattr(func, "__func__")

    def from_json(cls: Type[Self], obj: Typed) -> Self:
        obj = Prodict(**obj) if not isinstance(obj, Prodict) else obj
        self = func(cls, obj)
        self.json = obj
        return self
    return classmethod(lambda x, y: from_json(x, y))


class FetchableMeta(type):
    """
    Metaclass for :class:Fetchable used to hook the from_json method
    to convert :class:dict objects to :class:Prodict , allowing for easy
    use
    """
    def __new__(mcs, name: str, bases: tuple, dct: dict):
        dct.update({"from_json": _hook_from_json(dct["from_json"])})
        return type.__new__(mcs, name, bases, dct)


class _Fetchable(metaclass=FetchableMeta):
    @classmethod
    def from_json(cls, obj):
        pass


class Fetchable(Generic[Typed], _Fetchable):
    """
    A fetchable object is any direction representation of returned JSON data
    from the BadDragon API

    As this is an abstract class, it is not to be instantiated on its own
    and should not be directly used
    """
    json: Typed

    @classmethod
    @abstractmethod
    def from_json(cls: Type[Self], obj: dict | Typed) -> Self:
        pass
