from data import destinos

def ver_destinos():
    print("\n--- LISTA DE DESTINOS ---")
    if not destinos:
        print("No hay destinos registrados.")
    else:
        for id, dst in destinos.items():
            print(f"Destino ID: {id}, País: {dst['pais']}, Ciudad: {dst['ciudad']}, Costo Base: {dst['costo_base']}")

def agregar_destino():
    print("\n--- AGREGAR DESTINO ---")
    print("Función no disponible en esta versión.")

def modificar_destino():
    print("\n--- MODIFICAR DESTINO ---")
    print("Función no disponible en esta versión.")

def eliminar_destino():
    print("\n--- ELIMINAR DESTINO ---")
    print("Función no disponible en esta versión.")

def gestionar_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al menú principal")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            ver_destinos()
        elif opcion == "2":
            agregar_destino()
        elif opcion == "3":
            modificar_destino()
        elif opcion == "4":
            eliminar_destino()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")