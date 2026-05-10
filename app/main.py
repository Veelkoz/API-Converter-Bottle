from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from decimal import Decimal
from converter import convert
from models import ConvertResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/convert")
def convert_endpoint(
    value: str,
    from_unit: str,
    to_unit: str,
    round_to: int = 10
):
    try:
        return ConvertResponse(
            result=convert(Decimal(value), from_unit, to_unit, round_to),
            from_unit=from_unit,
            to_unit=to_unit,
            input=float(Decimal(value))
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))