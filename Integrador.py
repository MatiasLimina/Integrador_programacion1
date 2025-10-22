import csv
import os
from Manejo_csv import *
from Busqueda_por_nombre import *
from Filtrado_paises import *
from Ordenar_paises import *
from Estadisticas import *
from Sub_Menus import *
#Por hacer
#Falta chequear duplicados
#Agregar editar pais y agregar pais
#Busqueda parcial: falta que encuentr un pais cuando no pones el acento y pais mal escrito por ejemplo "irkn"
#Mover funciones a archivos aparte
#Si inicializa sin csv creado que lo cree con header correspondientes
#Funciones manejo de csv
#manejar numeros como floats
#Revisar casos border(Agregar funcion recursiva que filtr en el directorio y me devuelva el archivo csv)
def limpiar_pantalla():
    # Limpia la pantalla de la terminal. 'cls' para Windows, 'clear' para otros.
    os.system('cls' if os.name == 'nt' else 'clear')

#MAIN
def main(): #Ejecuta el codigo principal
    salir = False
    
    while not salir: #Muestra el menú hasta que el usuario lo indique
        print("--- MENU ---")
        print(" 1) Busqueda por nombre\n 2) Filtrar países\n 3) Ordenar países\n 4) Mostrar estadísticas\n 5) Salir")
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
            case "5": #Salir
                print("¡Gracias por utilizar nuestro servicio!")
                salir = True
        if not salir:
            input("\nPresione Enter para volver al menú principal...")


paises = leer_archivo() # Guarda los países como lista
if paises is None:
    print("ERROR: No se pudo cargar el archivo de países. Asegúrese de que 'Paises.csv' existe en la misma carpeta y tiene el formato correcto.")
    paises = []

if __name__ == "__main__":
    if paises: # Solo ejecuta el main si la lista de países no está vacía
        main()
    else:
        print("El programa no puede continuar sin datos de países. Finalizando.")
