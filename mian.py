# Propósito del sistema: Sistema de Gestión de Pasajes Aéreos para SkyRoute S.R.L.

# Integrantes del grupo:
# Milena Casas Vallejo - DNI: 40683531
# Lucas Acosta - DNI: 36143955
# Martina Cortez - DNI: 48604208
# Matias Pucheta - DNI: 43871894
# Camila Rocio Virga - DNI: 46453956

from clientes import gestionar_clientes
from destinos import gestionar_destinos
from ventas import gestionar_ventas
from consultas import consultar_ventas
from reportes import ver_reporte_general


def mostrar_menu():
    print("\n=== SkyRoute S.R.L. - Sistema de Gestión de Pasajes Aéreos ===")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Ver Reportes")
    print("6. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_destinos()
        elif opcion == "3":
            gestionar_ventas()
        elif opcion == "4":
            consultar_ventas()
        elif opcion == "5":
            ver_reporte_general()
        elif opcion == "6":
            print("\n¡Gracias por usar SkyRoute! Hasta la próxima.")
            break
        else:
            print("Opción inválida, probá otra vez.")