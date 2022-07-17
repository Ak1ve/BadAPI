from typing import TypeAlias, Optional
from prodict import Prodict


"""
Obtained via /inventory api thing
"""


link: TypeAlias = str
dict_str: TypeAlias = str


class InventoryColorTheme(Prodict):
    id: int
    name: str
    description: str
    bodyOptionId: int
    baseOptionId: int
    priceModifier: str
    singleProduct: bool
    specification: dict_str
    isSurpriseMe: bool
    globalPreviewOverrideImage: None
    swatchImageId: int
    sort_order: int
    startDate: Optional[str]
    endDate: Optional[str]


class InventoryImage(Prodict):
    id: int
    inventoryToyId: int
    created: str
    sortOrder: int
    imageUrlFull: link
    imageUrl450: link
    imageUrl240: link
    imageUrl1200: link
    imageUrl150: link
    isFlopPhoto: bool


class InventoryToy(Prodict):
    id: int
    id_list: str
    sku: str
    price: str
    size: int
    firmness: int
    cumtube: int
    suction_cup: int
    color_theme: Optional[int]
    colorTheme: Optional[InventoryColorTheme]
    created: str
    weight: str
    is_flop: bool
    external_flop_reason: Optional[str]
    color_display: str
    original_price: Optional[str]
    images: list[InventoryImage]


class InventoryPage(Prodict):
    limit: str
    page: str
    toys: list[InventoryToy]

