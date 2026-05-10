from pydantic import BaseModel

class ConvertResponse(BaseModel):
    result: float
    from_unit: str
    to_unit: str
    input: float

class ErrorResponse(BaseModel):
    error: str
    detail: str
