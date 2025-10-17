import csv
import os

def main():
    salir = True
    while salir:
        print("--- MENU ---")
        print("1) Filtrar países\n 2) Ordenar países\n 3) Mostrar estadísticas\n 4) Salir")
        opc = input("\n Eliga una opción... ")
        
        match opc:
            case "1":
                continue
            case "2":
                continue
            case "3":
                continue
            case "4":
                print("Gracias por utilizar nuestro servicio!")
                salir = False

main()
