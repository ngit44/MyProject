
from fastapi import FastAPI, HTTPException, status



#from app.schemas import SiteCreate, SiteResponse
#from app.sample_data import sites
from app.routers.sites import router as sites_router
 
app = FastAPI(title="Site Intelligence API")
app.include_router(sites_router)

@app.get("/")
def say_hello():
    return {"message": "Hello, AI Engineer!"}