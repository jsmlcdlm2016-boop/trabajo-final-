gastos= []
#se genera dataset para pruebas,
"""gastos = [
{'placa': 'ASD123', 'concepto': 'PEAJE', 'valor': 20000.0},
{'placa': 'ASD123', 'concepto': 'GASOLINA', 'valor': 50000.0},
{'placa': 'ASD111', 'concepto': 'PEAJE', 'valor': 10000.0},
{'placa': 'ASD111', 'concepto': 'GASOLINA', 'valor': 12000.0},
{'placa': 'QWE456', 'concepto': 'GASOLINA', 'valor': 45000.0},
{'placa': 'QWE456', 'concepto': 'PEAJE', 'valor': 9000.0},
{'placa': 'RTY789', 'concepto': 'GASOLINA', 'valor': 60000.0},
{'placa': 'RTY789', 'concepto': 'PEAJE', 'valor': 11000.0},
{'placa': 'JKL222', 'concepto': 'GASOLINA', 'valor': 52000.0},
{'placa': 'JKL222', 'concepto': 'PEAJE', 'valor': 8000.0},
{'placa': 'POI333', 'concepto': 'GASOLINA', 'valor': 47000.0},
{'placa': 'POI333', 'concepto': 'PEAJE', 'valor': 10000.0},
{'placa': 'ASD123', 'concepto': 'PEAJE', 'valor': 7000.0},
{'placa': 'ASD111', 'concepto': 'PEAJE', 'valor': 6000.0},
{'placa': 'QWE456', 'concepto': 'GASOLINA', 'valor': 55000.0},
{'placa': 'RTY789', 'concepto': 'GASOLINA', 'valor': 49000.0},
{'placa': 'JKL222', 'concepto': 'PEAJE', 'valor': 12000.0},
{'placa': 'POI333', 'concepto': 'GASOLINA', 'valor': 65000.0},
{'placa': 'ASD123', 'concepto': 'GASOLINA', 'valor': 53000.0},
{'placa': 'QWE456', 'concepto': 'PEAJE', 'valor': 9500.0}
]"""

def menu():
    while True:
        print("  SISTEMA DE CONTROL DE GASTOS")
        print("═" * 33)
        print(" 1. Registrar gasto de vehículo")
        print(" 2. Buscar gastos por placa     ")
        print(" 3. Calcular total acumulado    ")
        print(" 4. Salir                      ")
        

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gastos()
        elif opcion == "2":
            calcular_gastos()
        elif opcion == "3":
            total_gastos()
        elif opcion == "4":
            print("\nSaliendo del programa.")
            break
        else:
            print("\nError: Opción no válida, intente de nuevo.")

def registrar_gastos():
    placa = input("Ingrese la placa del vehículo: ").upper()
    concepto = input("Ingrese el concepto (Gasolina, Peaje): ").upper()
    valor = int(input("Ingrese el valor del gasto: "))

    gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }

    gastos.append(gasto)
    
    print(gastos)

    print("Gasto registrado correctamente\n")

def calcular_gastos():
    placa = input("Ingrese la placa del vehículo: ").upper()
    suma=0
    for gasto in gastos:
        if gasto["placa"] == placa:
            suma = suma + gasto["valor"]
    print("---------------------")
    print("Gastos de la placa", placa, ":")
    print("$", int(suma))
    print("---------------------")
    input("\nPresione ENTER para continuar...")

def total_gastos():
    suma=0
    for gasto in gastos:
            suma = suma + gasto["valor"]
    print("---------------------")
    print("Gastos totales: ")
    print("$", int(suma))
    print("---------------------")
    input("\nPresione ENTER para continuar...")
menu() 
