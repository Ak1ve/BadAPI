from ast import literal_eval
from typing import Type, TypedDict, TypeVar
from .abc.Fetchable import Fetchable, Typed
from prodict import Prodict


__all__ = ("text_from_dict_str", "convert_list")


def text_from_dict_str(obj: str) -> str:
    return "\n".join(x["text"] for x in literal_eval(obj)["blocks"])


T_Fetchable = TypeVar("T_Fetchable", bound=Fetchable)


def convert_list(type_: Type[T_Fetchable], lst: list[Typed]) -> list[T_Fetchable[Typed]]:
    return [type_.from_json(x) for x in lst]
