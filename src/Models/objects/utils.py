from ast import literal_eval
from typing import Type, TypeVar
from src.Models.abc.Fetchable import Fetchable, Typed


__all__ = ("text_from_dict_str", "convert_list")


def text_from_dict_str(obj: str) -> str:
    """
    Gets text from a dict encoded into a string
    mainly only used for description and furry descriptions
    of products
    :param obj: dict object encoded into a string
    :return:
    """
    return "\n".join(x["text"] for x in literal_eval(obj)["blocks"])


T_Fetchable = TypeVar("T_Fetchable", bound=Fetchable)


def convert_list(type_: Type[T_Fetchable], lst: list[Typed]) -> list[T_Fetchable[Typed]]:
    """
    Converts a list (lst) of json objects to a given type (type_)
    :param type_: type of Fetchable object to convert json
    :param lst: a list of json to convert
    :return:
    """
    return [type_.from_json(x) for x in lst]
