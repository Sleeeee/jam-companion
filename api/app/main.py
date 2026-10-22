from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter(prefix="/api")

@router.get("/")
async def root():
    return {"message": "Hello to Svelte from FastAPI !"}

app.include_router(router)
