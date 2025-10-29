from Manejo_csv import mostrar_lista_paises
from Ordenar_paises import (ordenar_por_nombre, ordenar_por_poblacion, 
                            ordenar_por_superficie_ascendente, ordenar_por_superficie_descendente)
from Busqueda_por_nombre import busqueda_nombre_parcial, elegir_nombre
from Filtrado_paises import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from Estadisticas import (estadistica_mayor_menor_poblacion, estadistica_promedio_poblacion, 
                        estadistica_promedio_superficie, estadistica_cant_paises_por_continente)
from utilidades import limpiar_pantalla
from Agregar_Editar_paises import agregar_pais, editar_pais


def sub_menu_ordenar_paises(dic_paises): #Muestra opciones y realiza el proceso de orden de paises
    limpiar_pantalla()
    print("=====================")
    print("Como desea ordenar los paises?")
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

def sub_menu_busqueda_nombre(paises):
    limpiar_pantalla()
    nombre = input("Ingrese un nombre: ").capitalize().strip()
    paises_encontrados = busqueda_nombre_parcial(nombre,paises)
    if not paises_encontrados: 
        print("No se encontraron coincidencias")
    elif len(paises_encontrados) == 1: 
        mostrar_lista_paises(paises_encontrados)
    else:
        pais_elegido = elegir_nombre(paises_encontrados)
        mostrar_lista_paises([pais_elegido])

def opcion_menu_principal():
    opc = input("\n Elija una opción: ").strip()
    while not opc.isnumeric(): 
        print("Opción inválida. Por favor, ingrese un número.")
        opc = input("\n Elija una opción: ").strip()
    return opc

def sub_menu_filtrar_paises(paises):
    limpiar_pantalla()
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

def sub_menu_agregar_pais(paises):
    agregar_pais(paises)

def sub_menu_editar_pais(paises):
    editar_pais(paises)

def sub_menu_estadisticas(paises):
    limpiar_pantalla()
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