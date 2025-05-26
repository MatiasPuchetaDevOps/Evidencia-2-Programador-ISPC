from data import clientes

def ver_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cuit, cliente in clientes.items():
            print(f"CUIT: {cuit}, Razón Social: {cliente['razon_social']}, Correo: {cliente['correo_contacto']}")

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    print("Función no disponible en esta versión.")

def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")
    print("Función no disponible en esta versión.")

def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    print("Función no disponible en esta versión.")

def gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al menú principal")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            ver_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")