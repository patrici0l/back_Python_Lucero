VOCALS = ("A", "E", "I", "O", "U")

def validar_placa(placa: str):
    if len(placa) < 4 or placa[3] != "-":
        raise ValueError("La placa debe tener '-' en la cuarta posición")

def calcular_impuesto(marca: str, fabricacion: int, valor: float) -> float:
    base = valor * 0.025

    if fabricacion < 2010:
        base += base * 0.10

    if marca.upper().startswith(VOCALS):
        base -= 30.0

    return 0.0 if base < 0 else base

def generar_codigo_revision(placa: str, propietario: str, fabricacion: int) -> str:
    return placa[:3] + str(len(propietario)) + str(fabricacion)[-1]

def procesar_vehiculo(data: dict) -> dict:
    validar_placa(data["placa"])
    data["impuesto"] = calcular_impuesto(
        data["marca"],
        data["fabricacion"],
        data["valor_comercial"]
    )
    data["codigo_revision"] = generar_codigo_revision(
        data["placa"],
        data["propietario"],
        data["fabricacion"]
    )
    return data

 