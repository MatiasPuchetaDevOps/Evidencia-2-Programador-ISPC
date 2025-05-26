from data import ventas
from data import clientes
from data import destinos

def generar_reporte_ventas():
    print("\n--- REPORTE DE VENTAS ---")
    total = sum(v['costo'] for v in ventas if v['estado']=="Activa")
    for v in ventas:
        c = clientes.get(v['cuit_cliente'], {})
        d = destinos.get(v['destino_id'], {})
        print(f"{v['venta_id']} - {c.get('razon_social','Desconocido')} -> {d.get('ciudad','?')} | ${v['costo']} | {v['estado']}")
    print(f"Total: ${total}")

def generar_reporte_clientes():
    print("\n--- REPORTE DE CLIENTES ---")
    for cuit, c in clientes.items():
        cnt = sum(1 for v in ventas if v['cuit_cliente']==cuit and v['estado']=="Activa")
        print(f"{cuit} - {c['razon_social']}: {cnt} ventas activas")

def generar_reporte_destinos():
    print("\n--- REPORTE DE DESTINOS ---")
    for did, d in destinos.items():
        cnt = sum(1 for v in ventas if v['destino_id']==did and v['estado']=="Activa")
        print(f"{did} - {d['ciudad']},{d['pais']}: {cnt} ventas activas")


def ver_reporte_general():
    while True:
        print("\n-- REPORTE GENERAL --")
        print("1. Ventas")
        print("2. Clientes")
        print("3. Destinos")
        print("4. Volver")
        opcion = input("Seleccione opción: ")
        if opcion == "1": generar_reporte_ventas()
        elif opcion == "2": generar_reporte_clientes()
        elif opcion == "3": generar_reporte_destinos()
        elif opcion == "4": break
        else: print("Opción inválida.")