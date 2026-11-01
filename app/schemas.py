from pydantic import BaseModel, Field
from typing import Literal

# TODO 1: Define SiteCreate
class SiteCreate(BaseModel):
    site_name: str = Field(min_length=3)
    status: Literal["Active", "Inactive"]
    depth: float = Field(ge=0)

# TODO 2: Define SiteResponse
class SiteResponse(BaseModel):
    site_id: int
    site_name: str = Field(min_length=3)
    status: Literal["Active", "Inactive"]
    depth: float = Field(ge=0)