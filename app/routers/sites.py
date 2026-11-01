from fastapi import APIRouter, HTTPException, status

from app.schemas import SiteCreate, SiteResponse
from app.sample_data import sites

router = APIRouter(prefix="/sites", tags=["Sites"])





# TODO: Implement your endpoints below.

@router.get("", response_model=list[SiteResponse])
def get_all_sites(status: str | None = None):

    if status is None:
        return list(sites.values())

    # 1 & 2 & 3: Loop through, compare status, and return matches
    return [site for site in sites.values() if site["status"] == status]


@router.get("/{site_id}", response_model=SiteResponse)
def get_site(site_id: int):
    if site_id not in sites:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )

    return sites[site_id]

# TODO 5: Implement POST /sites


@router.post(
    "/{site_id}",
    response_model=SiteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_site(site_id: int, site: SiteCreate):

    # 1. Check for duplicates
    if site_id in sites:
        raise HTTPException(
            status_code=409,
            detail="Site already exists"
        )

    # 2. Convert Pydantic model to dictionary
    new_site = site.model_dump()

    # 3. Add site ID
    new_site["site_id"] = site_id

    # 4. Save new site
    sites[site_id] = new_site

    return new_site
