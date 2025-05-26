from data import ventas, clientes, destinos
from ventas import ver_ventas as _ver_ventas

def ver_todas_las_ventas():
    """Muestra todas las ventas con detalles de cliente y destino."""
    print("--- TODAS LAS VENTAS ---")
    _ver_ventas()


def ver_ventas_por_cliente():
    """Muestra ventas filtradas por CUIT de cliente, con datos legibles."""
    print("--- VENTAS POR CLIENTE ---")
    cuit = input("Ingrese CUIT: ")
    encontradas = [v for v in ventas if v['cuit_cliente'] == cuit]
    if encontradas:
        for v in encontradas:
            cli = clientes.get(v['cuit_cliente'], {'razon_social':'Desconocido'})
            dst = destinos.get(v['destino_id'], {'ciudad':'Desconocido','pais':'?'})
            print(f"Venta {v['venta_id']}: {cli['razon_social']} -> {dst['ciudad']}, {dst['pais']} | Fecha: {v['fecha_venta']} | Costo: ${v['costo']} | Estado: {v['estado']}")
    else:
        print("No hay ventas para ese cliente.")


def ver_ventas_por_destino():
    """Muestra ventas filtradas por ID de destino, con datos legibles."""
    print("--- VENTAS POR DESTINO ---")
    try:
        did = int(input("Ingrese ID destino: "))
    except ValueError:
        print("ID inválido.")
        return
    encontradas = [v for v in ventas if v['destino_id'] == did]
    if encontradas:
        for v in encontradas:
            cli = clientes.get(v['cuit_cliente'], {'razon_social':'Desconocido'})
            dst = destinos.get(v['destino_id'], {'ciudad':'Desconocido','pais':'?'})
            print(f"Venta {v['venta_id']}: {cli['razon_social']} -> {dst['ciudad']}, {dst['pais']} | Fecha: {v['fecha_venta']} | Costo: ${v['costo']} | Estado: {v['estado']}")
    else:
        print("No hay ventas para ese destino.")


def consultar_ventas():
    """Menú de consulta de ventas."""
    while True:
        print("-- CONSULTAR VENTAS --")
        print("1. Todas las ventas")
        print("2. Por cliente")
        print("3. Por destino")
        print("4. Volver al menú principal")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            ver_todas_las_ventas()
        elif opcion == "2":
            ver_ventas_por_cliente()
        elif opcion == "3":
            ver_ventas_por_destino()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
