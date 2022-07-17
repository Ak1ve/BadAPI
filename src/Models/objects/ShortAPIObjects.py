from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass

import src.Models.typed_objects.ShortAPI as pro
from src.Models.abc.Fetchable import Fetchable
from src.Models.objects.utils import from_iso


__all__ = ("ProductAlias", "CartLimit", "ToyCartLimits", "AllowCustomToys", "Sales", "InventoryToyTotal")


@dataclass(unsafe_hash=True)
class ProductAlias(Fetchable[pro.ProductListAlias]):
    """
    A map for the sku of toys to the display name of them

    A list of them is obtained via /api/product-list
    """
    sku: str
    name: str

    @classmethod
    def from_json(cls, obj: dict | pro.ProductListAlias) -> ProductAlias:
        return cls(
            sku=obj.sku,
            name=obj.name
        )


@dataclass(unsafe_hash=True)
class CartLimit(Fetchable[pro.CartLimitation]):
    """
    A limit restricting how much of a certain item you can put in your cart
    """
    limit: int
    is_active: bool

    @classmethod
    def from_json(cls, obj: dict | pro.CartLimitation) -> CartLimit:
        return cls(
            limit=obj.limit,
            is_active=obj.isActive
        )


@dataclass(unsafe_hash=True)
class ToyCartLimits(Fetchable[pro.ToyCartLimits]):
    """
    Limits of how many toys you can put in your cart
    """
    inventory_toy_limit: CartLimit
    custom_toy_limit: CartLimit

    @classmethod
    def from_json(cls, obj: dict | pro.ToyCartLimits) -> ToyCartLimits:
        return cls(
            inventory_toy_limit=CartLimit.from_json(obj.inventoryToyLimit),
            custom_toy_limit=CartLimit.from_json(obj.customToyLimit)
        )


@dataclass(unsafe_hash=True)
class AllowCustomToys(Fetchable[pro.AllowCustomToys]):
    """
    Whether the shop allows custom toys to be purchased
    """
    is_enabled: bool
    updated: datetime

    @classmethod
    def from_json(cls, obj: dict | pro.AllowCustomToys) -> AllowCustomToys:
        return cls(
            is_enabled=obj.value != "false",
            updated=from_iso(obj.updated)
        )


@dataclass(unsafe_hash=True)
class Sales(Fetchable[pro.Sales]):
    """
    How close the custom toys are to full
    """
    target_progress: int
    enabled: bool

    @classmethod
    def from_json(cls, obj: dict | pro.Sales) -> Sales:
        return cls(
            target_progress=obj.salesTargetProgress,
            enabled=obj.salesTargetEnabled
        )


@dataclass(unsafe_hash=True)
class InventoryToyTotal(Fetchable[pro.ProductTotal]):
    total: int

    @classmethod
    def from_json(cls, obj: dict | pro.ProductTotal) -> InventoryToyTotal:
        return cls(total=int(obj.total))