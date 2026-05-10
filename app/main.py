from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.converter import router
from pathlib import Path

_readme_path = Path(__file__).resolve().parents[1] / "README.md"
_description = _readme_path.read_text(encoding="utf-8") if _readme_path.exists() else "Units Converter API"

app = FastAPI(
    title="Units Converter",
    description=_description,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)