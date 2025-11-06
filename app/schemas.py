from pydantic import BaseModel, AnyUrl, ConfigDict
from typing import List, Optional
from uuid import UUID
from enum import Enum


class OfferName(str, Enum):
    credit = "credit"
    loan = "loan"
    insurance = "insurance"


class OfferOut(BaseModel):
    id: int
    uuid: UUID
    url: str
    is_active: bool
    name: OfferName
    sum_to: Optional[int]
    term_to: Optional[int]
    percent_rate: Optional[float]

    model_config = ConfigDict(from_attributes=True)

#     class Config:
#         orm_mode = True


class OfferWallOut(BaseModel):
    id: int
    token: UUID
    name: str
    url: Optional[str]
    description: Optional[str]
    offers: List[OfferOut]

    model_config = ConfigDict(from_attributes=True)

#     class Config:
#         orm_mode = True

# class OfferOut(BaseModel):
#     id: int
#     name: str
#
#     model_config = ConfigDict(from_attributes=True)
#
#
# class OfferWallOut(BaseModel):
#     id: int
#     token: str
#     url: str
#     offers: list[OfferOut] = []
#
#     model_config = ConfigDict(from_attributes=True)