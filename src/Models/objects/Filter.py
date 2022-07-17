from __future__ import annotations
import enum
from dataclasses import dataclass, field
from typing import Literal, Optional


__all__ = ("Size", "Filter", "Firmness", "Category", "ProductType", )


class Size(enum.Enum):
    ONE_SIZE = "onesize"
    MINI = "mini"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extralarge"
    TWO_X_LARGE = "2xlarge"


class Firmness(enum.Enum):
    SOFT = "soft"
    MEDIUM = "medium"
    FIRM = "firm"
    SPLIT = "split"


class ProductType(enum.Enum):
    READY_MADE = "ready_made"
    FLOPS = "flop"


class Category(enum.Enum):
    ALL = ""
    DILDOS = "insertable"
    MASTURBATORS = "penetrable"
    PACKERS = "packer"
    LIL_SQUIRTS = "shooter"
    LIL_VIBES = "vibrator"
    WEARABLES = "wearable"


@dataclass(frozen=True, unsafe_hash=True)
class Filter:
    price_min: int = 0
    price_max: int = 300
    product_skus: list[str] = field(default_factory=list)
    sizes: list[Size] = field(default_factory=list)
    firmnesses: list[Firmness] = field(default_factory=list)
    product_types: list[ProductType] = field(default_factory=lambda: [ProductType.READY_MADE])
    category: Category = Category.ALL
    cumtube: Optional[bool] = None
    suction_cup: Optional[bool] = None
    no_features: Optional[bool] = None

    def assemble(self, type_: Literal["inventory", "total"], *, page: int = 1) -> str:
        ending = "?" if type_ == "inventory" else "/total?"
        base = f"https://bad-dragon.com/api/inventory-toys{ending}"

        fields: list[str] = [
            f"price[min]={self.price_min}",
            f"price[max]={self.price_max}"]

        if type_ == "inventory":
            # bad dragon flips out if you don't have a limit...
            # even if internally its never more or less than 60
            fields.append(f"page={page}&limit=60")

        fields.extend([f"skus[][]={sku}" for sku in self.product_skus])
        fields.extend([f"sizes[]={size.value}" for size in self.sizes])
        fields.extend([f"firmnessValues[]={firmness}" for firmness in self.firmnesses])
        fields.extend([f"type[]={product.value}" for product in self.product_types])

        if self.category != Category.ALL:
            fields.append(f"category={self.category.value}")

        if self.cumtube is not None and not self.no_features:
            fields.append(f"cumtube={int(self.cumtube)}")

        if self.suction_cup is not None and not self.no_features:
            fields.append(f"suctionCup={int(self.suction_cup)}")

        if self.no_features:
            fields.append("noAccessories=1")

        if type_ == "inventory":
            fields.append("sort[field]=price&=&sort[direction]=asc")

        return (base + "&".join(fields)).replace("[", "%5B").replace("]", "%5D")

    def inventory(self, page: int = 1) -> str:
        return self.assemble("inventory", page=page)

    @classmethod
    def default(cls) -> Filter:
        return cls()


