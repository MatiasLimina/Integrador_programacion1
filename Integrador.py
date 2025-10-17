import csv
import os


def leer_archivo():
    try:
        with open(RUTA_ARCHIVO,"r",encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = []
            for linea in lector:
                try:
                    paises.append(linea)
                except :
                    pass
            return paises
    except FileNotFoundError:
        return None

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

RUTA_ARCHIVO = "Programacion 1/Integrador_programacion1/Paises.csv"
paises = leer_archivo()
#main()
