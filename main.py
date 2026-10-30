
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Site Intelligence API")


sites = {
    1783718: {
        "site_id": 1783718,
        "site_name": "Monitoring Site A",
        "municipality": "Mississauga",
        "status": "active",
        "depth_mm": 120.5
    },
    1785723: {
        "site_id": 1785723,
        "site_name": "Monitoring Site B",
        "municipality": "Brampton",
        "status": "maintenance",
        "depth_mm": 85.0
    },
    1789001: {
        "site_id": 1789001,
        "site_name": "Monitoring Site C",
        "municipality": "Caledon",
        "status": "inactive",
        "depth_mm": 0.0
    }
}

# TODO: Implement your endpoints below.

@app.get("/")
def say_hello():
    return {"message": "Hello, AI Engineer!"}

@app.get("/sites")
def get_all_sites(status: str | None = None):

    if status is None:
        return list(sites.values())

    # 1 & 2 & 3: Loop through, compare status, and return matches
    return [site for site in sites.values() if site["status"] == "active"]


@app.get("/sites/{site_id}")
def get_site(site_id: int):
    if site_id not in sites:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )

    return sites[site_id]
