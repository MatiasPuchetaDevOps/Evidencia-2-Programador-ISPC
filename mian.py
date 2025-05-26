# Propósito del sistema: Sistema de Gestión de Pasajes Aéreos para SkyRoute S.R.L.

# Cómo instalar y ejecutar:
# 1. Asegúrate de tener Python instalado.
# 3. Ejecuta el archivo main.py en un editor de codigo.

# Integrantes del grupo:
# Milena Casas Vallejo - DNI: 40683531
# Lucas Acosta - DNI: 36143955
# Martina Cortez - DNI: 48604208
# Matias Pucheta - DNI: 43871894
# Camila Rocio Virga - DNI: 46453956


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

# Menú principal
def mostrar_menu():
    print("\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Salir del Sistema")

# Submenú para Gestionar Clientes
def gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")

        opcion_cliente = input("\nSeleccione una opción: ")

        if opcion_cliente == "1":
            print(">> Eligió opción 1: Ver Clientes")
            ver_clientes()
        elif opcion_cliente == "2":
            print(">> Eligió opción 2: Agregar Cliente")
            agregar_cliente()
        elif opcion_cliente == "3":
            print(">> Eligió opción 3: Modificar Cliente")
            modificar_cliente()
        elif opcion_cliente == "4":
            print(">> Eligió opción 4: Eliminar Cliente")
            eliminar_cliente()
        elif opcion_cliente == "5":
            print(">> Salió de 'Gestionar Clientes'")
            return
        else:
            print("Opción no válida.")

def ver_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cuit, cliente in clientes.items():
            print(f"CUIT: {cuit}, Razón Social: {cliente['razon_social']}, Correo: {cliente['correo_contacto']}")

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    print("No se encuentra habilitada esta funcion en esta version.")

def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")
    print("No se encuentra habilitada esta funcion en esta version.")


def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    print("No se encuentra habilitada esta funcion en esta version.")

# Submenú para Gestionar Destinos
def gestionar_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")

        opcion_destino = input("\nSeleccione una opción: ")

        if opcion_destino == "1":
            print(">> Eligió opción 1: Ver Destinos")
            ver_destinos()
        elif opcion_destino == "2":
            print(">> Eligió opción 2: Agregar Destino")
            agregar_destino()
        elif opcion_destino == "3":
            print(">> Eligió opción 3: Modificar Destino")
            modificar_destino()
        elif opcion_destino == "4":
            print(">> Eligió opción 4: Eliminar Destino")
            eliminar_destino()
        elif opcion_destino == "5":
            print(">> Salió de 'Gestionar Destinos'")
            return
        else:
            print("Opción no válida.")

def ver_destinos():
    print("\n--- LISTA DE DESTINOS ---")
    if not destinos:
        print("No hay destinos registrados.")
    else:
        for destino_id, destino in destinos.items():
            print(f"Destino ID: {destino_id}, País: {destino['pais']}, Ciudad: {destino['ciudad']}, Costo Base: {destino['costo_base']}")

def agregar_destino():
    print("\n--- AGREGAR DESTINO ---")
    print("No se encuentra habilitada esta funcion en esta version.")

def modificar_destino():
    print("\n--- MODIFICAR DESTINO ---")
    print("No se encuentra habilitada esta funcion en esta version.")

def eliminar_destino():
    print("\n--- ELIMINAR DESTINO ---")
    print("No se encuentra habilitada esta funcion en esta version.")

# Submenú para Gestionar Ventas
def gestionar_ventas():
    while True:  
        print("\n-- GESTIONAR VENTAS --")
        print("1. Registrar Venta")
        print("2. Ver Ventas")
        print("3. Volver al Menú Principal")

        opcion_venta = input("\nSeleccione una opción: ")

        if opcion_venta == "1":
            print(">> Eligió opción 1: Registrar Venta")
            registrar_venta()
        elif opcion_venta == "2":
            print(">> Eligió opción 2: Ver Ventas")
            ver_ventas()
        elif opcion_venta == "3":
            print(">> Salió de 'Gestionar Ventas'")
            return
        else:
            print("Opción no válida.")

def registrar_venta():
    print("\n--- REGISTRAR VENTA ---")
    print("No se encuentra habilitada esta funcion en esta version.")

def ver_ventas():
    print("\n--- LISTA DE VENTAS ---")
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Destino ID: {venta['destino_id']}, Fecha: {venta['fecha_venta']}, Costo: {venta['costo']}, Estado: {venta['estado']}")

# Submenú para Consultar Ventas
def consultar_ventas():
    while True:
        print("\n-- CONSULTAR VENTAS --")
        print("1. Ver Todas las Ventas")
        print("2. Ver Ventas por Cliente")
        print("3. Ver Ventas por Destino")
        print("4. Ver Ventas por Estado")
        print("5. Ver Ventas por Fecha")
        print("6. Volver al Menú Principal")

        opcion_consulta = input("\nSeleccione una opción: ")

        if opcion_consulta == "1":
            print(">> Eligió opción 1: Ver Todas las Ventas")
            ver_todas_las_ventas()
        elif opcion_consulta == "2":
            print(">> Eligió opción 2: Ver Ventas por Cliente")
            ver_ventas_por_cliente()
        elif opcion_consulta == "3":
            print(">> Eligió opción 3: Ver Ventas por Destino")
            ver_ventas_por_destino()
        elif opcion_consulta == "4":
            print(">> Eligió opción 4: Ver Ventas por Estado")
            ver_ventas_por_estado()
        elif opcion_consulta == "5":
            print(">> Eligió opción 5: Ver Ventas por Fecha")
            ver_ventas_por_fecha()
        elif opcion_consulta == "6":
            print(">> Salió de 'Consultar Ventas'")
            return
        else:
            print("Opción no válida.")

def ver_todas_las_ventas():
    ver_ventas() 

def ver_ventas_por_cliente():
    print("\n--- VENTAS POR CLIENTE ---")
    cuit_cliente = input("Ingrese el CUIT del cliente: ")
    encontradas = False
    for venta in ventas:
        if venta["cuit_cliente"] == cuit_cliente:
            print(f"Venta ID: {venta['venta_id']},  Cliente: {cuit_cliente}, Destino ID: {venta['destino_id']}, Fecha: {venta['fecha_venta']}, Costo: {venta['costo']}, Estado: {venta['estado']}")
            encontradas = True
    if not encontradas:
        print("No se encontraron ventas para ese cliente.")
    print(f"\n>> Ingresó el CUIT: {cuit_cliente}")

def ver_ventas_por_destino():
    print("\n--- VENTAS POR DESTINO ---")
    destino_id = int(input("Ingrese el ID del destino: "))
    encontradas = False
    for venta in ventas:
        if venta["destino_id"] == destino_id:
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Fecha: {venta['fecha_venta']}, Costo: {venta['costo']}, Estado: {venta['estado']}")
            encontradas = True
    if not encontradas:
        print("No se encontraron ventas para ese destino.")
    print(f"\n>> Ingresó el ID destino: {destino_id}")

def ver_ventas_por_estado():
    print("\n--- VENTAS POR ESTADO ---")
    estado = input("Ingrese el estado (Activa o Anulada): ")
    encontradas = False
    for venta in ventas:
        if venta["estado"].lower() == estado.lower():
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Destino ID: {venta['destino_id']}, Fecha: {venta['fecha_venta']}, Costo: {venta['costo']}, Estado: {venta['estado']}")
            encontradas = True
    if not encontradas:
        print("No se encontraron ventas con ese estado.")
    print(f"\n>> Ingresó el Estado: {estado}")

def ver_ventas_por_fecha():
    print("\n--- VENTAS POR FECHA ---")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    encontradas = False
    for venta in ventas:
        if venta["fecha_venta"] == fecha:
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Destino ID: {venta['destino_id']}, Costo: {venta['costo']}, Estado: {venta['estado']}")
            encontradas = True
    if not encontradas:
        print("No se encontraron ventas para esa fecha.")
    print(f"\n>> Ingresó la fecha: {fecha}")


# Submenú para Botón de Arrepentimiento
def boton_arrepentimiento():
    while True:
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        print("1. Anular Venta")
        print("2. Ver Ventas Anuladas")
        print("3. Volver al Menú Principal")

        opcion_arrepentimiento = input("\nSeleccione una opción: ")

        if opcion_arrepentimiento == "1":
            print(">> Eligió opción 1: Anular Venta")
            anular_venta()
        elif opcion_arrepentimiento == "2":
            print(">> Eligió opción 2: Ver Ventas Anuladas")
            ver_ventas_anuladas()
        elif opcion_arrepentimiento == "3":
            print(">> Salió de 'Boton de Arrepentimiento'")
            return
        else:
            print("Opción no válida.")

def anular_venta():
    print("\n--- ANULAR VENTA ---")
    print("No se encuentra habilitada esta funcion en esta version.")

def ver_ventas_anuladas():
    print("\n--- VENTAS ANULADAS ---")
    encontradas = False
    for venta in ventas:
        if venta["estado"] == "Anulada":
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Destino ID: {venta['destino_id']}, Fecha: {venta['fecha_venta']}, Costo: {venta['costo']}")
            encontradas = True
    if not encontradas:
        print("No hay ventas anuladas.")

def ver_reporte_general():
    while True:
        print("\n-- REPORTE GENERAL --")
        print("1. Generar Reporte de Ventas")
        print("2. Generar Reporte de Clientes")
        print("3. Generar Reporte de Destinos")
        print("4. Volver al Menú Principal")

        opcion_reporte = input("\nSeleccione una opción: ")

        if opcion_reporte == "1":
            print(">> Eligió opción 1: Generar Reporte de Ventas")
            generar_reporte_ventas()
        elif opcion_reporte == "2":
            print(">> Eligió opción 2: Generar Reporte de Clientes")
            generar_reporte_clientes()
        elif opcion_reporte == "3":
            print(">> Eligió opción 3: Generar Reporte de Destinos")
            generar_reporte_destinos()
        elif opcion_reporte == "4":
            print(">> Salió de 'Ver Reporte General'")
            return
        else:
            print("Opción no válida.")

def generar_reporte_ventas():
    print("\n--- REPORTE DE VENTAS ---")
    total = 0
    for venta in ventas:
        cliente = clientes.get(venta['cuit_cliente'], {"razon_social": "Desconocido"})
        destino = destinos.get(venta['destino_id'], {"ciudad": "Desconocido", "pais": "Desconocido"})
        print(f"Venta ID: {venta['venta_id']}, Cliente: {cliente['razon_social']} ({venta['cuit_cliente']}), Destino: {destino['ciudad']}, {destino['pais']}, Fecha: {venta['fecha_venta']}, Costo: ${venta['costo']}, Estado: {venta['estado']}")
        if venta["estado"] == "Activa":
            total += venta["costo"]
    print(f"\nTotal vendido (ventas activas): ${total}")


def generar_reporte_clientes():
    print("\n--- REPORTE DE CLIENTES ---")
    for cuit, cliente in clientes.items():
        cantidad = 0
        for venta in ventas:
            if venta['cuit_cliente'] == cuit and venta['estado'] == "Activa":
                cantidad += 1
        print(f"CUIT: {cuit}, Razón Social: {cliente['razon_social']}, Ventas activas: {cantidad}")

def generar_reporte_destinos():
    print("\n--- REPORTE DE DESTINOS ---")
    for destino_id, destino in destinos.items():
        cantidad = 0
        for venta in ventas:
            if venta['destino_id'] == destino_id and venta['estado'] == "Activa":
                cantidad += 1
        print(f"Destino: {destino['ciudad']} ({destino['pais']}), Ventas activas: {cantidad}")


# Flujo principal del programa
while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        print(">> Eligió 'Gestionar Clientes'")
        gestionar_clientes()
    elif opcion == "2":
        print(">> Eligió 'Gestionar Destinos'")
        gestionar_destinos()
    elif opcion == "3":
        print(">> Eligió 'Gestionar Ventas'")
        gestionar_ventas()
    elif opcion == "4":
        print(">> Eligió 'Consultar Ventas'")
        consultar_ventas()
    elif opcion == "5":
        print(">> Eligió 'Botón de Arrepentimiento'")
        boton_arrepentimiento()
    elif opcion == "6":
        print(">> Eligió 'Ver Reporte General'")
        ver_reporte_general()
    elif opcion == "7":
        print("\n>> Eligió 'Salir del Sistema'.")
        print("\nSaliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
