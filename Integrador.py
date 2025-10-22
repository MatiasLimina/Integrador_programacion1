import csv
import os
from Manejo_csv import *
from Busqueda_por_nombre import *
from Filtrado_paises import *
#Por hacer
#Falta chequear duplicados
#Agregar editar pais y agregar pais
#Busqueda parcial: falta que encuentr un pais cuando no pones el acento y pais mal escrito por ejemplo "irkn"
#Mover funciones a archivos aparte
#Cada opcion debe llamar una funcion
#Si inicializa sin csv creado que lo cree con header correspondientes
#Funciones manejo de csv
#manejar numeros como floats
#buscar forma de limpiar la terminal
#Revisar casos border(Agregar funcion recursiva que filtr en el directorio y me devuelva el archivo csv)


#Funciones ordenar paises
def sub_menu_ordenar_paises(dic_paises): #Muestra opciones y realiza el proceso de orden de paises
    print("=====================")
    print("Como desea prdenar los paises?")
    print("1) Nombre \n2)Población \n3)Superficie\n")
    opc = input("Elija una opción: ").strip()
    while not opc.isnumeric() or opc not in ["1", "2", "3"]: 
        print("Opción inválida. Por favor, elija 1, 2 o 3.")
        opc = input("Elija una opción: ").strip()
    match opc: 
        case "1":#Ordenar por nombre
            orden_por_nombre = ordenar_por_nombre(dic_paises)
            print("Paises ordenados de forma alfabetica:")
            print()
            mostrar_lista_paises(orden_por_nombre)
        case "2":#Ordenar por población
            orden_por_poblacion = ordenar_por_poblacion(dic_paises)
            print("Paises ordenados segun su población")
            print()
            mostrar_lista_paises(orden_por_poblacion)
        case "3":#Ordenar por superficie (Ascendente y Descendente)
            opc = input ("1) Orden Ascendente \n2) Orden Descendente \n")
            while not opc.isnumeric() or opc not in ["1", "2"]: 
                print("Opción inválida. Por favor, elija 1 o 2.")
                opc = input ("1) Orden Ascendente \n2) Orden Descendente \n")
            if opc == "1":
                orden_superficie_ascendente = ordenar_por_superficie_ascendente(dic_paises)
                print("Paises ordenados de manera ascendente segun su población")
                print()
                mostrar_lista_paises(orden_superficie_ascendente)
            elif opc == "2":
                orden_superficie_descendente = ordenar_por_superficie_descendente(dic_paises)
                print("Paises ordenados de manera descendente segun su población")
                print()
                mostrar_lista_paises(orden_superficie_descendente)

def ordenar_por_nombre(lista_de_diccionarios): #Ordena paises por nombre
    return sorted(lista_de_diccionarios, key=lambda pais: pais["nombre"])

def ordenar_por_poblacion(lista_de_diccionarios): #Ordena paises por la clave "poblacion" de forma ascendente
    return sorted(lista_de_diccionarios, key=lambda pais: pais["poblacion"])

def ordenar_por_superficie_ascendente(lista_de_diccionarios): #Ordena paises por superficie de forma ascendente
    return sorted(lista_de_diccionarios, key=lambda pais: pais["superficie"])

def ordenar_por_superficie_descendente(lista_de_diccionarios): #Ordena paises por superficie de forma descendente
    return sorted(lista_de_diccionarios, key=lambda pais: pais["superficie"],reverse=True)

#Funciones de estadísticas
def estadistica_mayor_menor_poblacion(paises): #Muestra el pais con menor y mayor población
    if not paises: 
        print("ERROR: No hay datos de países cargados.")
        return

    # Ordena por población (de mayor a menor)
    pais_mayor = max(paises, key=lambda x: x["poblacion"])
    pais_menor = min(paises, key=lambda x: x["poblacion"])

    print("\n=== PAÍSES CON MAYOR Y MENOR POBLACIÓN ===")
    print(f"País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
    print(f"País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")

def estadistica_promedio_poblacion(paises): #Calcula y muestra el promedio global de población
    if not paises: 
        print("ERROR: No hay datos de países cargados.")
        return

    total_poblacion = sum(p.get("poblacion", 0) for p in paises)
    cantidad_paises = len(paises)

    if cantidad_paises == 0: #Valida que hayan paises disponibles
        print("ERROR: No hay países cargados.")
        return

    promedio = total_poblacion / cantidad_paises

    print("\n=== PROMEDIO GLOBAL DE POBLACIÓN ===")
    print(f"Promedio de población: {round(promedio, 2)} habitantes")

def estadistica_promedio_superficie(paises): #Calcula y muestra el promedio global de superficie

    if not paises: 
        print("ERROR: No hay datos de países cargados.")
        return

    total_superficie = sum(p.get("superficie", 0) for p in paises)
    cantidad_paises = len(paises)

    if cantidad_paises == 0: 
        print("ERROR: No hay países cargados.")
        return

    promedio = total_superficie / cantidad_paises

    print("\n=== PROMEDIO GLOBAL DE SUPERFICIE ===")
    print(f"Promedio de superficie: {round(promedio, 2)} km²")

def estadistica_cant_paises_por_continente(paises): #Muestra la cantidad total de países por continente
    if not paises: 
        print("ERROR: No hay datos de países cargados.")
        return

    continentes = {} 
    for p in paises:
        cont = p.get("continente", "Desconocido").capitalize()
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\n=== CANTIDAD DE PAÍSES POR CONTINENTE ===")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")

#MAIN
def main(): #Ejecuta el codigo principal
    salir = False
    
    while not salir: #Muestra el menú hasta que el usuario lo indique
        print("--- MENU ---")
        print(" 1) Busqueda por nombre\n 2) Filtrar países\n 3) Ordenar países\n 4) Mostrar estadísticas\n 5) Salir")
        opc = input("\n Elija una opción: ").strip()
        while not opc.isnumeric(): 
            print("Opción inválida. Por favor, ingrese un número.")
            opc = input("\n Elija una opción: ").strip()
        match opc:
            case "1": #Busca pais por nombre (coincidencia parcial o exacta)
                nombre = input("Ingrese un nombre ").capitalize().strip()
                paises_encontrados = busqueda_nombre_parcial(nombre,paises)
                if not paises_encontrados: 
                    print("No se encontraron coincidencias")
                elif len(paises_encontrados) == 1: 
                    mostrar_lista_paises(paises_encontrados)
                else:
                    pais_elegido = elegir_nombre(paises_encontrados)
                    mostrar_lista_paises([pais_elegido])
            case "2": #Filtra países por continente, rango de población o rango de superficie
                print("1) Filtrar por continente\n2) Filtrar por rango de población\n3) Filtrar por rango de superficie\n4) Salir")
                opc_categoria = input("Ingrese el filtro que desea aplicar: ").strip()
                while not opc_categoria.isnumeric(): 
                    print("Opción no disponible, ingrese un valor correcto: ")
                    opc_categoria = input("Ingrese el filtro que desea aplicar: ").strip()
                match opc_categoria: #Abre submenú con filtros aplicables
                    case "1": #Filtrar por continente
                        filtrar_por_continente(paises) 
                    case "2": #Filtrar por población
                        filtrar_por_poblacion(paises) 
                    case "3": #Filtrar por continente
                        filtrar_por_superficie(paises) 
                    case "4": #Salir
                        print("Volver al menú principal.")
                    case _:
                        print("Seleccione una opción válida.")
            case "3": #Ordenar países
                sub_menu_ordenar_paises(paises)
            case "4": #Mostrar estadísticas
                print("1) País con mayor y menor población")
                print("2) Promedio de población")
                print("3) Promedio de superficie")
                print("4) Cantidad de países por continente")
                print("5) Salir")
                opc_est = input("Ingrese la opción deseada: ").strip()

                while not opc_est.isnumeric(): # Valida que la entrada sea numérica
                    print("Opción inválida. Debe ingresar un número.")
                    opc_est = input("Ingrese la opción deseada: ").strip()

                match opc_est:
                    case "1":
                        estadistica_mayor_menor_poblacion(paises)
                    case "2":
                        estadistica_promedio_poblacion(paises)
                    case "3":
                        estadistica_promedio_superficie(paises)
                    case "4":
                        estadistica_cant_paises_por_continente(paises)
                    case "5":
                        print("Volver al menú principal.")
                    case _:
                        print("Seleccione una opción válida.")
            case "5": #Salir
                print("¡Gracias por utilizar nuestro servicio!")
                salir = True



paises = leer_archivo() # Guarda los países como lista
if paises is None:
    print("ERROR: No se pudo cargar el archivo de países. Asegúrese de que 'Paises.csv' existe en la misma carpeta y tiene el formato correcto.")
    paises = []

if __name__ == "__main__":
    if paises: # Solo ejecuta el main si la lista de países no está vacía
        main()
    else:
        print("El programa no puede continuar sin datos de países. Finalizando.")
