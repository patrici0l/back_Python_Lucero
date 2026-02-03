from fastapi import FastAPI, HTTPException
from .schemas import VehiculoIn, VehiculoOut
from .service import procesar_vehiculo
from .repository import VehiculoRepository

app = FastAPI()
repo = VehiculoRepository()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/vehiculos", response_model=VehiculoOut, status_code=201)
def crear_vehiculo(dto: VehiculoIn):
    try:
        data = procesar_vehiculo(dto.model_dump())
        return repo.crear(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/vehiculos", response_model=list[VehiculoOut])
def listar_vehiculos():
    return repo.listar()
