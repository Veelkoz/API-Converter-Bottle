from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import length, weight, temperature, volume, area, time, speed, pressure, energy, data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

# Register routers with prefixes
app.include_router(length.router, prefix="/length", tags=["length"])
app.include_router(weight.router, prefix="/weight", tags=["weight"])
app.include_router(temperature.router, prefix="/temperature", tags=["temperature"])
app.include_router(volume.router, prefix="/volume", tags=["volume"])
app.include_router(area.router, prefix="/area", tags=["area"])
app.include_router(time.router, prefix="/time", tags=["time"])
app.include_router(speed.router, prefix="/speed", tags=["speed"])
app.include_router(pressure.router, prefix="/pressure", tags=["pressure"])
app.include_router(energy.router, prefix="/energy", tags=["energy"])
app.include_router(data.router, prefix="/data", tags=["data"])