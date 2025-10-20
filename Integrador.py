import csv
import os
#Falta duplicar duplicados
#Funciones manejo de csv
def leer_archivo(): 
    try: 
        with open(RUTA_ARCHIVO,"r",encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = []
            for linea in lector: 
                linea_valida = validar_csv(linea)
                if linea_valida == None:
                    pass
                else:
                    paises.append(linea_valida) #Si la línea es válida la agrega a la lista
            return paises
    except FileNotFoundError: 
        return None

def crear_listas_columnas(dic_paises): #Crea listas con los datos en cada columna
    lista_paises = []
    lista_poblacion=[]
    lista_superficie = []
    lista_continente = []
    for d in dic_paises: #Extrae el valor de cada key y las añade a las listas correspondientes
        lista_paises.append(d.get("nombre"))
        lista_poblacion.append(d.get("poblacion"))
        lista_superficie.append(d.get("superficie"))
        lista_continente.append(d.get("continente"))
    return lista_paises,lista_poblacion,lista_superficie,lista_continente 

def mostrar_lista_paises(lista_de_paises): #Pasa la lista de diccionarios e imprime cada línea formateada
    for pais in lista_de_paises:
        print(f"Pais: {pais['nombre']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']}, Continente: {pais['continente']}")

def validar_csv(linea): #Valida cada línea del csv antes de agregarlo a la lista de diccionarios
    pais = linea.get("nombre")
    poblacion = linea.get("poblacion") 
    superficie = linea.get("superficie")
    continente = linea.get("continente")
    if pais == "": 
        print("ERROR: El campo ¨nombre¨ no debe estar vacío")
        return None
    if continente == "": 
        print("ERROR: El campo ¨continente¨ no debe estar vacío")
        return None
    try: 
        poblacion = int(poblacion)
    except ValueError: 
        print(f"ERROR: {poblacion} datos inválidos, el campo ¨poblacion¨ espera un entero")
        return None
    try: 
        superficie = int(superficie)
    except ValueError: 
        print(f"ERROR: {superficie} datos inválidos, el campo ¨superficie¨ espera un entero")
        return None
    linea_validada = {"nombre":pais,"poblacion":poblacion,"superficie":superficie,"continente":continente}
    return linea_validada

#Funciones buscar por nombre
def busqueda_nombre_parcial(termino_busqueda, diccionario): #Realiza la busqueda de coincidencias
    coincidencias = []
    termino_busqueda_lower = termino_busqueda.lower().strip()
    
    # Caso de búsqueda exacta primero
    for pais in diccionario:
        if pais.get("nombre", "").lower() == termino_busqueda_lower:
            return [pais]

    # Si no hay coincidencia exacta, busca coincidencias parciales
    for pais in diccionario:
        if termino_busqueda_lower in pais.get("nombre", "").lower():
            coincidencias.append(pais) 
    return coincidencias

def elegir_nombre(coincidencias): #Muestra coincidencias al usuario
    print("Esta es la lista de paises que coinciden con su búsqueda: ")
    for i in range(len(coincidencias)): #Muestra la lista de coincidencias
        print(f"ID: {i} Pais: {coincidencias[i]['nombre']}")
    eleccion_id = id_busqueda(len(coincidencias)-1) #Da a elegir un país de la lista por ID
    return coincidencias[eleccion_id] 

def id_busqueda (max): #Valida el ID de los país
    while True: 
        identificador_str = input(f"Ingrese el ID del país que desea (0 - {max}): ") 
        try: 
            identificador_int = int(identificador_str)
            if 0 <= identificador_int <= max: 
                return identificador_int
            else:
                print(f"Error: El número debe estar entre 0 y {max}.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

#Funciones filtrado
def filtrar_por_continente(dic_paises): #Filtra paises por continente
    continentes_disponibles = [] 
    for pais in dic_paises:
        continente_actual = pais.get("continente")
        if continente_actual not in continentes_disponibles:
            continentes_disponibles.append(continente_actual)
    print("=== CONTINENTES DISPONIBLES ===")
    for i in range(len(continentes_disponibles)):
        print(f"{i}) {continentes_disponibles[i]}")
    print("===============================")   
    while True: # Solicita al usuario que elija un continente por ID con validaciones
        entrada = input(f"Ingrese el ID del continente (0 - {len(continentes_disponibles)-1}): ").strip()
        if entrada == "": 
            print("ERROR: El campo no debe estar vacío.")
            continue
        try: 
            entrada_int = int(entrada)
            if 0 <= entrada_int < len(continentes_disponibles): 
                continente_elegido = continentes_disponibles[entrada_int]
                break
            else:
                print("ERROR: El número está fuera del rango permitido.")
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")

    # Filtra los países que pertenecen al continente seleccionado
    paises_filtrados = []
    for pais in dic_paises:
        if pais.get("continente", "").lower() == continente_elegido.lower():
            paises_filtrados.append(pais)

    # Muestra los países filtrados
    print(f"\nPaíses del continente {continente_elegido}:")
    if len(paises_filtrados) > 0:
        mostrar_lista_paises(paises_filtrados)
    else:
        print("No se encontraron países en este continente.")

def filtrar_por_poblacion(dic_paises): #Filtra paises por población
    while True: 
        minimo_str = input("Ingrese la población mínima: ").strip()
        if minimo_str == "": 
            print("ERROR: No puede dejar la población mínima vacía.")
            continue
        try: 
            minimo = int(minimo_str)
            break
        except ValueError:
            print("ERROR: La población mínima debe ser un número entero.")
    while True: 
        maximo_str = input("Ingrese la población máxima: ").strip()
        if maximo_str == "": 
            print("ERROR: No puede dejar la población máxima vacía.")
            continue
        try: 
            maximo = int(maximo_str)
            if maximo < minimo:
                print("ERROR: La población máxima no puede ser menor que la mínima.")
                continue
            break
        except ValueError:
            print("ERROR: La población máxima debe ser un número entero.")

    # Filtra los países dentro del rango ingresado
    paises_filtrados = []
    for pais in dic_paises:
        poblacion_actual = pais.get("poblacion")
        if minimo <= poblacion_actual <= maximo:
            paises_filtrados.append(pais)

    # Muestra los resultados
    print(f"\nPaíses con población entre {minimo} y {maximo}:")
    if len(paises_filtrados) > 0:
        mostrar_lista_paises(paises_filtrados)
    else:
        print("No se encontraron países dentro de ese rango de población.")

def filtrar_por_superficie(dic_paises): #Filtra paises por superficie
    while True:
        minimo_str = input("Ingrese la superficie mínima: ").strip()
        if minimo_str == "": 
            print("ERROR: No puede dejar la superficie mínima vacía.")
            continue
        try: 
            minimo = int(minimo_str)
            break
        except ValueError:
            print("ERROR: La superficie mínima debe ser un número entero.")
    while True: 
        maximo_str = input("Ingrese la superficie máxima: ").strip()
        if maximo_str == "":
            print("ERROR: No puede dejar la superficie máxima vacía.")
            continue
        try: 
            maximo = int(maximo_str)
            if maximo < minimo: 
                print("ERROR: La superficie máxima no puede ser menor que la mínima.")
                continue
            break
        except ValueError:
            print("ERROR: La superficie máxima debe ser un número entero.")

    # Filtra los países dentro del rango ingresado
    paises_filtrados = []
    for pais in dic_paises:
        superficie_actual = pais.get("superficie")
        if minimo <= superficie_actual <= maximo:
            paises_filtrados.append(pais)

    # Muestra los resultados con el formato solicitado
    print(f"\nPaíses con superficie entre {minimo} y {maximo}:")
    if len(paises_filtrados) > 0:
        for pais in paises_filtrados:
            print(f"País: {pais['nombre']}, Superficie: {pais['superficie']}")
    else:
        print("No se encontraron países dentro de ese rango de superficie.")
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

#RUTA DEL CSV
script_dir = os.path.dirname(os.path.abspath(__file__)) 
RUTA_ARCHIVO = os.path.join(script_dir, "Paises.csv")

paises = leer_archivo() # Guarda los países como lista
if paises is None:
    print("ERROR: No se pudo cargar el archivo de países. Asegúrese de que 'Paises.csv' existe en la misma carpeta y tiene el formato correcto.")
    paises = []

if __name__ == "__main__":
    if paises: # Solo ejecuta el main si la lista de países no está vacía
        main()
    else:
        print("El programa no puede continuar sin datos de países. Finalizando.")
