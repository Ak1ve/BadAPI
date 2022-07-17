from prodict import Prodict


class ProductListAlias(Prodict):
    sku: str
    name: str


class CartLimitation(Prodict):
    limit: int
    isActive: bool


class ToyCartLimits(Prodict):
    inventoryToyLimit: CartLimitation
    customToyLimit: CartLimitation


class AllowCustomToys(Prodict):
    key: str
    value: str
    updated: str


class Sales(Prodict):
    salesTargetProgress: int
    salesTargetEnabled: bool


class ProductTotal(Prodict):
    total: str