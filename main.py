
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="Site Intelligence API")


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

sites = {
    1783718: {
        "site_id": 1783718,
        "site_name": "Monitoring Site A",
        "status": "Active",
        "depth": 120.5
    },
    1785723: {
        "site_id": 1785723,
        "site_name": "Monitoring Site B",
        "status": "Inactive",
        "depth": 85.0
    },
    1789001: {
        "site_id": 1789001,
        "site_name": "Monitoring Site C",
        "status": "Inactive",
        "depth": 0.0
    }
}

# TODO: Implement your endpoints below.

@app.get("/")
def say_hello():
    return {"message": "Hello, AI Engineer!"}

@app.get("/sites", response_model=list[SiteResponse])
def get_all_sites(status: str | None = None):

    if status is None:
        return list(sites.values())

    # 1 & 2 & 3: Loop through, compare status, and return matches
    return [site for site in sites.values() if site["status"] == status]


@app.get("/sites/{site_id}", response_model=SiteResponse)
def get_site(site_id: int):
    if site_id not in sites:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )

    return sites[site_id]

# TODO 5: Implement POST /sites

from fastapi import status

@app.post(
    "/sites",
    response_model=SiteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_site(site: SiteCreate):

    # 1. Generate a unique site ID
    new_id = max(sites.keys(), default=0) + 1

    # 2. Convert Pydantic model to dictionary
    new_site = site.model_dump()

    # 3. Add the generated ID
    new_site["site_id"] = new_id

    # 4. Store the new site
    sites[new_id] = new_site

    # 5. Return the created site
    return new_site
