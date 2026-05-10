from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers.converter import router
from pathlib import Path
from fastapi.responses import RedirectResponse
from .registry import converters

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

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/categories")
def categories():
    return list(converters.keys())

@app.get("/categories/{category}/units")
def category_units(category: str):
    if category not in converters:
        raise HTTPException(status_code=404, detail=f"unknown category: {category}")
    return {
        "units": list(converters[category].factor.keys()),
        "aliases": converters[category].aliases
    }

app.include_router(router)