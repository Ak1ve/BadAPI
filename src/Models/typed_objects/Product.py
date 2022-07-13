from typing import TypeAlias, Optional
from prodict import Prodict

"""
Obtained via /api/products
"""

dict_str: TypeAlias = str
link: TypeAlias = str


class ProductURL(Prodict):
    id: int
    url: link


class ProductScaleImage(Prodict):
    productId: str
    optionId: int
    imageId: int
    image: ProductURL


class ProductDescriptionImage(Prodict):
    productId: str
    thumbImageId: int
    fullImageId: int
    sortOrder: int
    type: str
    medImageId: Optional[str]
    thumbImage: ProductURL
    medImage: Optional[ProductURL]  # might not be present
    fullImage: ProductURL


class Product(Prodict):
    sku: str
    name: str
    description: dict_str
    basePrice: str
    baseWeight: str
    productImageId: int
    type: str
    previewImageId: Optional[int]
    previewBaseThreshold: Optional[str]
    previewBaseMargin: Optional[str]
    previewFadeGreenOnly: bool
    defaultHsCode: int
    startDate: str
    endDate: Optional[str]
    seoTitle: str
    furryDescription: dict_str
    title: str
    furryTitle: str
    previewModelId: int
    previewNormalMapId: int
    previewTextureMapId: int
    productVideoId: None
    sortOrder: int
    disabled: bool
    productTaxCode: Optional[int]
    internalProductionDisplayName: Optional[str]
    productImage: Optional[ProductURL]  # might not be present
    relatedProducts: list
    previewImage: Optional[ProductURL]  # might not be present
    scaleImages: list[ProductScaleImage]
    furryDescriptionImage: ProductDescriptionImage
    previewObjModel: Optional[ProductURL]  # might not be present
    previewTextureMap: Optional[ProductURL]  # might not be present
    previewNormalMap: Optional[ProductURL]  # might not be present
    descriptionImage: ProductDescriptionImage
    productThumbnails: list[ProductDescriptionImage]
