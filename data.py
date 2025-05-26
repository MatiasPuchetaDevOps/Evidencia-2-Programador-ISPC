
# data.py
clientes = {
    "40683531": {"razon_social": "VolarFlash", "correo_contacto": "volarflash@gmail.com"},
    "36143955": {"razon_social": "AerolineasArg", "correo_contacto": "aerolineasarg@gmail.com"},
    "48604208": {"razon_social": "AlCielo", "correo_contacto": "alcielo@gmail.com"},
}

destinos = {
    1: {"pais": "Argentina", "ciudad": "Bariloche", "costo_base": 80000},
    2: {"pais": "Brasil", "ciudad": "Río de Janeiro", "costo_base": 150000},
    3: {"pais": "España", "ciudad": "Madrid", "costo_base": 350000},
}

ventas = [
    {"venta_id": 1, "cuit_cliente": "40683531", "destino_id": 1, "fecha_venta": "2024-06-01", "costo": 80000, "estado": "Activa"},
    {"venta_id": 2, "cuit_cliente": "36143955", "destino_id": 2, "fecha_venta": "2024-06-02", "costo": 150000, "estado": "Activa"},
    {"venta_id": 3, "cuit_cliente": "48604208", "destino_id": 3, "fecha_venta": "2024-06-03", "costo": 350000, "estado": "Anulada"},
]
