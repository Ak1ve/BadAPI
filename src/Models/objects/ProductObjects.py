from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass

from src.Models.typed_objs import Product as pro
from src.Models.abc.Fetchable import Fetchable
from src.Models.utils import text_from_dict_str


@dataclass(frozen=True, unsafe_hash=True)
class Product(Fetchable[pro.Product]):
    sku: str
    name: str
    description: str
    base_price: float
    base_weight: float
    type: str
    start_date: datetime
    seo_tile: str
    furry_description: str
    title: str
    furry_title: str
    disabled: bool

    @classmethod
    def from_json(cls, obj: pro.Product) -> Product:
        return cls(
            sku=obj.sku,
            name=obj.name,
            description=text_from_dict_str(obj.description),
            base_price=float(obj.basePrice),
            base_weight=float(obj.baseWeight),
            type=obj.type,
            start_date=datetime.fromisoformat(obj.startDate),
            seo_tile=obj.seoTitle,
            furry_description=text_from_dict_str(obj.furryDescription),
            title=obj.title,
            furry_title=obj.furryTitle,
            disabled=obj.disabled
        )
