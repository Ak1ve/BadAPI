from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from typing import Optional, ClassVar

from src.Models.typed_objs import Inventory as inv
from src.Models.abc.Fetchable import Fetchable
from src.Models.utils import convert_list


@dataclass(frozen=True, unsafe_hash=True)
class InventoryImage(Fetchable[inv.InventoryImage]):
    id: int
    toy_id: int
    created: datetime
    image_full: str
    image_450: str
    image_240: str
    image_1200: str
    image_150: str
    is_flop_photo: bool

    @classmethod
    def from_json(cls, obj: inv.InventoryImage) -> InventoryImage:
        return cls(
            id=obj.id,
            toy_id=obj.inventoryToyId,
            created=datetime.fromisoformat(obj.created),
            image_full=obj.imageUrlFull,
            image_450=obj.imageUrl450,
            image_150=obj.imageUrl150,
            image_240=obj.imageUrl240,
            image_1200=obj.imageUrl1200,
            is_flop_photo=obj.isFlopPhoto
        )


@dataclass(frozen=True, unsafe_hash=True)
class InventoryColorTheme(Fetchable[inv.InventoryColorTheme]):
    id: int
    name: str
    description: str
    price_modifier: float
    start_date: datetime

    @classmethod
    def from_json(cls, obj: inv.InventoryColorTheme) -> InventoryColorTheme:
        return cls(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            price_modifier=float(obj.priceModifier),
            start_date=datetime.fromisoformat(obj.startDate)
        )


@dataclass(frozen=True, unsafe_hash=True)
class InventoryToy(Fetchable[inv.InventoryToy]):
    size_map: ClassVar[dict[int, str]] = {270: 'paw-twopack', 6: 'onesize', 120: 'macebundle', 119: 'morale',
                                          269: 'paw-single', 1: 'small', 118: 'discipline', 2: 'medium',
                                          3: 'extralarge', 10: 'mini', 287: '2xlarge', 8: 'large'}
    firmness_map: ClassVar[dict[int, str]] = {123: 'Firm Shaft, Soft Base', 121: 'Soft Shaft, Medium Base',
                                              124: 'Firm Shaft, Medium Base', 9: 'Firm', 4: 'Medium',
                                              7: 'Soft', 11: 'Med Shaft, Firm Base', 12: 'Soft Shaft, Firm Base',
                                              122: 'Medium Shaft, Soft Base', 5: 'Extra Soft'}
    id: int
    sku: str
    price: float
    size: str
    firmness: str
    has_cumtube: bool
    has_suction_cup: bool
    color_theme: Optional[InventoryColorTheme]
    created: datetime
    weight: float
    is_flop: bool
    flop_reason: Optional[str]
    color_name: str
    original_price: float
    images: list[InventoryImage]

    @classmethod
    def from_json(cls, obj: inv.InventoryToy) -> InventoryToy:
        color_name = obj["color_display"] if "colorTheme" not in obj else obj["colorTheme"]["name"]
        return cls(
            id=obj.id,
            sku=obj.sku,
            price=float(obj.price),
            size=cls.size_map[obj.size],
            firmness=cls.firmness_map[obj.firmness],
            has_cumtube=obj.cumtube != 18,
            has_suction_cup=obj.suction_cup == 23,
            color_theme=InventoryColorTheme.from_json(obj.colorTheme) if "colorTheme" in obj else None,
            created=datetime.fromisoformat(obj.created),
            weight=float(obj.weight),
            is_flop=obj.is_flop,
            flop_reason=obj.external_flop_reason,
            color_name=color_name,
            original_price=float(obj.original_price),
            images=convert_list(InventoryImage, obj.images)
        )


@dataclass(frozen=True, unsafe_hash=True)
class InventoryPage(Fetchable[inv.InventoryPage]):
    limit: int
    page: int
    toys: list[InventoryToy]

    @classmethod
    def from_json(cls, obj: inv.InventoryPage) -> InventoryPage:
        return cls(
            limit=int(obj.limit),
            page=int(obj.page),
            toys=convert_list(InventoryToy, obj.toys)
        )
