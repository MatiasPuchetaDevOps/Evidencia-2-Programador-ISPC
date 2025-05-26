from data import ventas

def ver_ventas():
    print("\n--- LISTA DE VENTAS ---")
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for v in ventas:
            print(f"Venta ID: {v['venta_id']}, Cliente: {v['cuit_cliente']}, Destino: {v['destino_id']}, Fecha: {v['fecha_venta']}, Costo: {v['costo']}, Estado: {v['estado']}")

def registrar_venta():
    print("\n--- REGISTRAR VENTA ---")
    print("Función no disponible en esta versión.")

def gestionar_ventas():
    while True:
        print("\n-- GESTIONAR VENTAS --")
        print("1. Registrar Venta")
        print("2. Ver Ventas")
        print("3. Volver al menú principal")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            ver_ventas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")