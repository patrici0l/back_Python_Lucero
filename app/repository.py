from .import db

class VehiculoRepository:

    def crear(self, vehiculo: dict) -> dict:
        return db.insertar(vehiculo)

    def listar(self) -> list:
        return db.listar()
