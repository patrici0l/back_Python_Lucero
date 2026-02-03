_vehiculos = []

def insertar(vehiculo: dict) -> dict:
    _vehiculos.append(vehiculo)
    return vehiculo

def listar() -> list:
    return _vehiculos
