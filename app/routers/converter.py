from fastapi import APIRouter, HTTPException
from ..registry import converters
from ..models import ConvertResponse
router = APIRouter()

@router.get("/{category}/convert")
def convert_endpoint(category: str, value: float, from_unit: str, to_unit: str, round_to: int = 10):
    if category not in converters:
        raise HTTPException(status_code=404, detail=f"unknown category: {category}")
    try:
        return ConvertResponse(
            result=converters[category].convert(value, from_unit, to_unit, round_to),
            from_unit=from_unit,
            to_unit=to_unit,
            input=value
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))