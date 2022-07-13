from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from src.Models.typed_objects import ProductOption as opt
from src.Models.abc.Fetchable import Fetchable
from src.Models.utils import convert_list


@dataclass(unsafe_hash=True)
class OptionColorTheme(Fetchable[opt.OptionColorTheme]):
    id: int
    name: str
    description: str
    price_modifier: float
    start_date: datetime

    @classmethod
    def from_json(cls, obj: dict | opt.OptionColorTheme) -> OptionColorTheme:
        return cls(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            price_modifier=float(obj.priceModifier),
            start_date=datetime.fromisoformat(obj.startDate)
        )


measurement_names: list[str] = ["circumference_testicles",
                                "diameter_testicles",
                                "diameter_widest_part",
                                "circumference_thickest_part_shaft",
                                "circumference_top",
                                "circumference_middle",
                                "diameter_narrowest_part",
                                "diameter_thickest_part_shaft",
                                "circumference_head",
                                "circumference_narrowest_part",
                                "internal_total_usable_length_2",
                                "small_toe_circumference",
                                "external_circumference_knot",
                                "internal_diameter_shaft",
                                "diameter_head",
                                "diameter_shaft",
                                "circumference_knot",
                                "circumference_lower_shaft",
                                "thickest_diameter",
                                "external_circumference_hood",
                                "large_toe_diameter",
                                "external_circumference_opening",
                                "external_circumference_thickest",
                                "ankle_diameter",
                                "external_diameter_thinnest",
                                "circumference_upper_shaft",
                                "circumference",
                                "paw_diameter",
                                "circumference_base",
                                "ankle_circumference",
                                "large_toe_circumference",
                                "diameter_upper_shaft",
                                "circumference_smallest_part_shaft",
                                "internal_usable_length",
                                "total_length",
                                "external_diameter_head",
                                "external_usable_length",
                                "circumference_bottom",
                                "circumference_widest_part",
                                "diameter_smallest_part_shaft",
                                "avg_diameter_bulb",
                                "diameter_medial_ring",
                                "external_diameter_knot",
                                "circumference_shaft_base",
                                "paw_circumference",
                                "external_diameter_thickest",
                                "external_circumference_thinnest",
                                "circumference_thinnest_part_shaft",
                                "circumference_shaft",
                                "diameter_base",
                                "circumference_largest_part_shaft",
                                "usable_length",
                                "internal_circumference_shaft",
                                "diameter_thinnest_part_shaft",
                                "usable_length",
                                "external_diameter_opening",
                                "diameter_bottom",
                                "diameter_top",
                                "diameter_lower_shaft",
                                "small_toe_diameter",
                                "diameter_largest_part_shaft",
                                "diameter_middle",
                                "diameter_knot",
                                "diameter_shaft_base",
                                "circumference_medial_ring",
                                "external_total_length",
                                "circumference_bulb",
                                "external_diameter_shaft",
                                "external_circumference_shaft",
                                "diameter"]


@dataclass(unsafe_hash=True)
class OptionDimensions(Fetchable[opt.OptionDimensions]):
    circumference_testicles: Optional[Measurement]
    diameter_testicles: Optional[Measurement]
    diameter_widest_part: Optional[Measurement]
    circumference_thickest_part_shaft: Optional[Measurement]
    circumference_top: Optional[Measurement]
    circumference_middle: Optional[Measurement]
    diameter_narrowest_part: Optional[Measurement]
    diameter_thickest_part_shaft: Optional[Measurement]
    circumference_head: Optional[Measurement]
    circumference_narrowest_part: Optional[Measurement]
    internal_total_usable_length_2: Optional[Measurement]
    small_toe_circumference: Optional[Measurement]
    external_circumference_knot: Optional[Measurement]
    internal_diameter_shaft: Optional[Measurement]
    diameter_head: Optional[Measurement]
    diameter_shaft: Optional[Measurement]
    circumference_knot: Optional[Measurement]
    circumference_lower_shaft: Optional[Measurement]
    thickest_diameter: Optional[Measurement]
    external_circumference_hood: Optional[Measurement]
    large_toe_diameter: Optional[Measurement]
    external_circumference_opening: Optional[Measurement]
    external_circumference_thickest: Optional[Measurement]
    ankle_diameter: Optional[Measurement]
    external_diameter_thinnest: Optional[Measurement]
    circumference_upper_shaft: Optional[Measurement]
    circumference: Optional[Measurement]
    paw_diameter: Optional[Measurement]
    circumference_base: Optional[Measurement]
    ankle_circumference: Optional[Measurement]
    large_toe_circumference: Optional[Measurement]
    diameter_upper_shaft: Optional[Measurement]
    circumference_smallest_part_shaft: Optional[Measurement]
    internal_usable_length: Optional[Measurement]
    total_length: Optional[Measurement]
    external_diameter_head: Optional[Measurement]
    external_usable_length: Optional[Measurement]
    circumference_bottom: Optional[Measurement]
    circumference_widest_part: Optional[Measurement]
    diameter_smallest_part_shaft: Optional[Measurement]
    avg_diameter_bulb: Optional[Measurement]
    diameter_medial_ring: Optional[Measurement]
    external_diameter_knot: Optional[Measurement]
    circumference_shaft_base: Optional[Measurement]
    paw_circumference: Optional[Measurement]
    external_diameter_thickest: Optional[Measurement]
    external_circumference_thinnest: Optional[Measurement]
    circumference_thinnest_part_shaft: Optional[Measurement]
    circumference_shaft: Optional[Measurement]
    diameter_base: Optional[Measurement]
    circumference_largest_part_shaft: Optional[Measurement]
    usable_length: Optional[Measurement]
    internal_circumference_shaft: Optional[Measurement]
    diameter_thinnest_part_shaft: Optional[Measurement]
    usable_length: Optional[Measurement]
    external_diameter_opening: Optional[Measurement]
    diameter_bottom: Optional[Measurement]
    diameter_top: Optional[Measurement]
    diameter_lower_shaft: Optional[Measurement]
    small_toe_diameter: Optional[Measurement]
    diameter_largest_part_shaft: Optional[Measurement]
    diameter_middle: Optional[Measurement]
    diameter_knot: Optional[Measurement]
    diameter_shaft_base: Optional[Measurement]
    circumference_medial_ring: Optional[Measurement]
    external_total_length: Optional[Measurement]
    circumference_bulb: Optional[Measurement]
    external_diameter_shaft: Optional[Measurement]
    external_circumference_shaft: Optional[Measurement]
    diameter: Optional[Measurement]

    @classmethod
    def from_json(cls, obj: dict | opt.OptionDimensions) -> OptionDimensions:
        def fix_typos(k: str) -> str:
            k = k.replace("-", "_")
            if k == "circuference_head":
                return "circumference_head"
            if k == "usuable_length":
                return "usable_length"
            return k
        obj = {fix_typos(k): v for k, v in obj.items()}
        for x in measurement_names:
            obj.update({x: Measurement.from_json(obj[x]) if x in obj else None})
        return cls(**obj)


@dataclass(unsafe_hash=True)
class Measurement(Fetchable[opt.Measurement]):
    measurement_type: str
    name: str
    size: str
    measurement: float

    @classmethod
    def from_json(cls, obj: dict | opt.Measurement) -> Measurement:
        return cls(
            measurement_type=obj.measurementType,
            name=obj.name,
            size=obj.size,
            measurement=obj.measurement
        )


@dataclass(unsafe_hash=True)
class OptionExceptionValue(Fetchable[opt.OptionExceptionValue]):
    id: int
    option_type: str
    value: str
    sort_order: int
    display_name: str

    @classmethod
    def from_json(cls, obj: dict | opt.OptionExceptionValue) -> OptionExceptionValue:
        return cls(
            id=obj.id,
            option_type=obj.optionType,
            value=obj.value,
            sort_order=obj.sortOrder,
            display_name=obj.displayName
        )


@dataclass(unsafe_hash=True)
class OptionException(Fetchable[opt.OptionException]):
    id: int
    product_id: Optional[int]
    is_global: bool
    message: str
    color_theme_id: Optional[int]
    option_values: list[OptionExceptionValue]

    @classmethod
    def from_json(cls, obj: opt.OptionException) -> OptionException:
        return cls(
            id=obj["id"],
            product_id=obj["productId"],
            is_global=obj["global"],
            message=obj["message"],
            color_theme_id=obj["colorThemeId"],
            option_values=convert_list(OptionExceptionValue, obj["optionValues"])
        )


@dataclass(unsafe_hash=True)
class OptionValue(Fetchable[opt.OptionValue]):
    id: int
    option_value_id: int
    value: str
    price_modifier: float
    weight_modifier: float

    @classmethod
    def from_json(cls, obj: dict | opt.OptionValue) -> OptionValue:
        return cls(
            id=obj.id,
            option_value_id=obj.optionValueId,
            value=obj.value,
            price_modifier=float(obj.priceModifier),
            weight_modifier=float(obj.weightModifier) if obj.weightModifier is not None else 0.0
        )


@dataclass(unsafe_hash=True)
class OptionSet(Fetchable[opt.Options]):
    base_color_type: list[OptionValue]
    cumtube: list[OptionValue]
    suction_cup: list[OptionValue]
    body_color_type: list[OptionValue]
    size: list[OptionValue]

    @classmethod
    def from_json(cls, obj: dict | opt.Options) -> OptionSet:
        return cls(
            base_color_type=convert_list(OptionValue, obj.basecolortype),
            cumtube=convert_list(OptionValue, obj.cumtube),
            suction_cup=convert_list(OptionValue, obj.suctionCup),
            body_color_type=convert_list(OptionValue, obj.bodycolortype),
            size=convert_list(OptionValue, obj.size)
        )


@dataclass(unsafe_hash=True)
class Options(Fetchable[opt.ProductOptions]):
    options: OptionSet
    color_themes: list[OptionColorTheme]
    dimensions: OptionDimensions
    option_exceptions: list[OptionException]

    @classmethod
    def from_json(cls, obj: dict | opt.ProductOptions) -> Options:
        return cls(
            options=OptionSet.from_json(obj.options),
            color_themes=convert_list(OptionColorTheme, obj.colorThemes),
            dimensions=obj.dimensions,
            option_exceptions=convert_list(OptionException, obj.optionExceptions)
        )
