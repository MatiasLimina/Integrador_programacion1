import csv
import os
from Manejo_csv import *
from Busqueda_por_nombre import *
from Filtrado_paises import *
from Ordenar_paises import *
from Estadisticas import *
from Sub_Menus import *
from utilidades import *
#Por hacer
#Revisar casos border(Agregar funcion recursiva que filtr en el directorio y me devuelva el archivo csv)


#MAIN
def main(paises): #Ejecuta el codigo principal
    salir = False
    
    while not salir: #Muestra el menú hasta que el usuario lo indique
        print("--- MENU ---")
        print(" 1) Busqueda por nombre\n 2) Filtrar países\n 3) Ordenar países\n 4) Mostrar estadísticas\n 5) Agregar país\n 6) Editar país\n 7) Salir")
        opc = opcion_menu_principal()
        match opc:
            case "1": #Busca pais por nombre (coincidencia parcial o exacta)
                sub_menu_busqueda_nombre(paises)
            case "2": #Filtra países por continente, rango de población o rango de superficie
                sub_menu_filtrar_paises(paises)
            case "3": #Ordenar países
                sub_menu_ordenar_paises(paises)
            case "4": #Mostrar estadísticas
                sub_menu_estadisticas(paises)
            case "5": #Agregar un nuevo país
                sub_menu_agregar_pais(paises)
            case "6": #Editar un país existente
                sub_menu_editar_pais(paises)
            case "7": #Salir
                print("¡Gracias por utilizar nuestro servicio!")
                salir = True
        if not salir:
            input("\nPresione Enter para volver al menú principal...")


# --- INICIO DEL PROGRAMA ---

# 1. Asegurarse de que el archivo CSV exista (si no, lo crea)
inicializar_csv_si_no_existe()

# 2. Cargar los datos del archivo
paises = leer_archivo() # Guarda los países como lista de diccionarios

if __name__ == "__main__":
    if paises is not None: # Solo ejecuta el main si la carga fue exitosa
        main(paises)
    else:
        print("El programa no puede continuar debido a un error de carga de datos. Finalizando.")
