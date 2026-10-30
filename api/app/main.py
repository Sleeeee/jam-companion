from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

router = APIRouter(prefix="/api")

@router.get("/")
async def root():
    return {"message": "Hello to Svelte from FastAPI !"}

app.include_router(router)
