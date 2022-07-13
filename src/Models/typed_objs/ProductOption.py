from typing import Optional, TypeAlias, TypedDict
from prodict import Prodict

"""
Obtained via /api/products/{product}/options
"""
dict_str: TypeAlias = str


class OptionImage(Prodict):
    id: int
    url: str


class ColorOptionValue(Prodict):
    id: int
    optionType: str
    value: str
    defaultPriceModifier: str
    sortOrder: int
    displayName: Optional[str]
    defaultWeightModifier: str


class OptionColorTheme(Prodict):
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
    startDate: str
    endDate: Optional[str]
    themePreviewOverrideImage: Optional[None]
    themeCustomTextureMap: None
    themeCustomModel: None
    themeCustomNormalMap: None
    themeCustomPreviewImage: Optional[None]
    bodyOptionValue: ColorOptionValue
    baseOptionValue: ColorOptionValue
    swatchImage: OptionImage


class OptionValue(Prodict):
    id: int
    optionValueId: int
    value: str
    priceModifier: str
    weightModifier: Optional[str]


class Options(Prodict):
    basecolortype: list[OptionValue]
    cumtube: list[OptionValue]
    suctionCup: list[OptionValue]
    bodycolortype: list[OptionValue]
    firmness: list[OptionValue]
    size: list[OptionValue]


class Measurement(Prodict):
    measurementType: str
    name: str
    size: str
    measurement: float
    dimensionSort: int


class OptionDimension(
    TypedDict(
        "OptionDimension",
        {
              'circumference-testicles': Measurement,
              'diameter-testicles': Measurement,
              'diameter-widest-part': Measurement,
              'circumference-thickest-part-shaft': Measurement,
              'circumference-top': Measurement,
              'circumference-middle': Measurement,
              'diameter-narrowest-part': Measurement,
              'diameter-thickest-part-shaft': Measurement,
              'circuference-head': Measurement,
              'circumference-narrowest-part': Measurement,
              'internal-total-usable-length-2': Measurement,
              'small-toe-circumference': Measurement,
              'external-circumference-knot': Measurement,
              'internal-diameter-shaft': Measurement,
              'diameter-head': Measurement,
              'diameter-shaft': Measurement,
              'circumference-knot': Measurement,
              'circumference-lower-shaft': Measurement,
              'thickest-diameter': Measurement,
              'external-circumference-hood': Measurement,
              'large-toe-diameter': Measurement,
              'external-circumference-opening': Measurement,
              'external-circumference-thickest': Measurement,
              'ankle-diameter': Measurement,
              'external-diameter-thinnest': Measurement,
              'circumference-upper-shaft': Measurement,
              'circumference': Measurement,
              'paw-diameter': Measurement,
              'circumference-base': Measurement,
              'ankle-circumference': Measurement,
              'large-toe-circumference': Measurement,
              'diameter-upper-shaft': Measurement,
              'circumference-smallest-part-shaft': Measurement,
              'internal-usable-length': Measurement,
              'total-length': Measurement,
              'external-diameter-head': Measurement,
              'external-usable-length': Measurement,
              'circumference-bottom': Measurement,
              'circumference-widest-part': Measurement,
              'diameter-smallest-part-shaft': Measurement,
              'avg-diameter-bulb': Measurement,
              'diameter-medial-ring': Measurement,
              'external-diameter-knot': Measurement,
              'circumference-shaft-base': Measurement,
              'paw-circumference': Measurement,
              'external-diameter-thickest': Measurement,
              'external-circumference-thinnest': Measurement,
              'circumference-thinnest-part-shaft': Measurement,
              'circumference-shaft': Measurement,
              'diameter-base': Measurement,
              'circumference-largest-part-shaft': Measurement,
              'usuable-length': Measurement,
              'internal-circumference-shaft': Measurement,
              'diameter-thinnest-part-shaft': Measurement,
              'usable-length': Measurement,
              'external-diameter-opening': Measurement,
              'diameter-bottom': Measurement,
              'diameter-top': Measurement,
              'diameter-lower-shaft': Measurement,
              'small-toe-diameter': Measurement,
              'diameter-largest-part-shaft': Measurement,
              'diameter-middle': Measurement,
              'diameter-knot': Measurement,
              'diameter-shaft-base': Measurement,
              'circumference-medial-ring': Measurement,
              'external-total-length': Measurement,
              'circumference-bulb': Measurement,
              'external-diameter-shaft': Measurement,
              'external-circumference-shaft': Measurement,
              'diameter': Measurement
              })):
    ...


class OptionDimensions(Prodict):
    small: Optional[OptionDimension]  # may not be present
    medium: Optional[OptionDimension]  # may not be present
    large: Optional[OptionDimension]  # may not be present
    extralarge: Optional[OptionDimension]  # may not be present
    mini: Optional[OptionDimension]  # may not be present
    onesize: Optional[OptionDimension]  # may not be present


class OptionExceptionValue(Prodict):
    id: int
    optionType: str
    value: str
    defaultPriceModifier: str
    sortOrder: int
    displayName: str
    defaultWeightModifier: Optional[str]
    _pivot_exception_id: int
    _pivot_option_value_id: int


class OptionException(TypedDict(
    "OptionException",
    {
        "id": int,
        "productId": Optional[int],
        "global": bool,
        "message": str,
        "colorThemeId": Optional[str],
        "optionValues": list[OptionExceptionValue]
    }
)):
    ...


class ProductOptions(Prodict):
    options: Options
    colorThemes: list[OptionColorTheme]
    dimensions: OptionDimensions
    optionExceptions: list[OptionException]
