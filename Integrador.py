import csv
import os
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
                    try:
                        paises.append(linea_valida)
                    except :
                        pass
            return paises
    except FileNotFoundError:
        return None

def crear_listas_columnas(dic_paises): #Crea listas con los datos en cada columna
    lista_paises = []
    lista_poblacion=[]
    lista_superficie = []
    lista_continente = []
    for d in dic_paises:
        lista_paises.append(d.get("nombre"))
        lista_poblacion.append(d.get("poblacion"))
        lista_superficie.append(d.get("superficie"))
        lista_continente.append(d.get("continente"))
    return lista_paises,lista_poblacion,lista_superficie,lista_continente

def mostrar_lista_paises(lista_de_paises):
    """Recorre una lista de diccionarios de países y los imprime de forma formateada."""
    for pais in lista_de_paises:
        print(f"Pais: {pais['nombre']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']}, Continente: {pais['continente']}")

def validar_csv(linea):
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
        print(f"ERROR: {poblacion} datos inválidos, el campo ¨poblacion¨ espera un número")
        return None
    try:
        superficie = int(superficie)
    except ValueError:
        print(f"ERROR: {superficie} datos inválidos, el campo ¨superficie¨ espera un número")
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
            return [pais] # Devuelve una lista con el único resultado exacto

    # Si no hay coincidencia exacta, busca coincidencias parciales
    for pais in diccionario:
        if termino_busqueda_lower in pais.get("nombre", "").lower():
            coincidencias.append(pais) # Agrega el diccionario completo
            
    return coincidencias

def elegir_nombre(coincidencias): #Muestra coincidencias al usuario
    print("Esta es la lista de paises que coinciden con su busqueda")
    for i in range(len(coincidencias)):
        print(f"ID: {i} Pais: {coincidencias[i]['nombre']}")
    eleccion_id = id_busqueda(len(coincidencias)-1)
    return coincidencias[eleccion_id] # Devuelve el diccionario del país elegido

def id_busqueda (max): #Validacion del ID
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

#Funciones ordenar paises
def sub_menu_ordenar_paises(dic_paises):
    print("=====================")
    print("Como desea prdenar los paises?")
    print("1) Nombre \n2)Población \n3)Superficie\n")
    opc = input("Elija una opción").capitalize().strip()
    
    match opc:
        case "1":#Ordenar por nombre
            orden_por_nombre = ordenar_por_nombre(dic_paises)
            print("Paises ordenados de forma alfabetica:")
            print()
            mostrar_lista_paises(orden_por_nombre)
        case "2":#Ordenar por poblacion
            # Ordenamos la lista completa de diccionarios usando la clave 'poblacion'
            paises_ordenados_poblacion = ordenar_por_poblacion(dic_paises)
            print("Paises ordenados segun su población")
            print()
            # Pasamos la nueva lista de diccionarios ya ordenada para mostrarla
            mostrar_lista_paises(paises_ordenados_poblacion)

        case "3":#Ordenar por superficie(Acendente y Descendente)
            pass

def ordenar_por_nombre(lista_de_diccionarios):
    return sorted(lista_de_diccionarios, key=lambda pais: pais["nombre"])

def ordenar_por_poblacion(lista_de_diccionarios):
    """Ordena una lista de diccionarios de países por la clave 'poblacion' de forma ascendente."""
    # La función lambda le dice a sorted() que use el valor de la clave 'poblacion' para ordenar
    return sorted(lista_de_diccionarios, key=lambda pais: pais["poblacion"])



#MAIN
def main():
    salir = True
    while salir:
        print("--- MENU ---")
        print(" 1) Busqueda por nombre\n 2) Filtrar países\n 3) Ordenar países\n 4) Mostrar estadísticas\n 5) Salir")
        opc = input("\n Elija una opción... ")
        
        match opc:
            case "1":#Buscar pais por nombre (coincidencia parcial o exacta).
                nombre = input("Ingrese un nombre ").capitalize().strip()
                paises_encontrados = busqueda_nombre_parcial(nombre,paises)
                if not paises_encontrados: # Si la lista está vacía
                    print("No se encontraron coincidencias")
                elif len(paises_encontrados) == 1: # Si solo hay una coincidencia (exacta o parcial)
                    mostrar_lista_paises(paises_encontrados)
                else:
                    pais_elegido = elegir_nombre(paises_encontrados)
                    mostrar_lista_paises([pais_elegido]) # La pasamos como lista para reutilizar la función

            case "2":#Filtrar paises
                continue
            case "3": #Ordenar paises
                sub_menu_ordenar_paises(paises)
                    
            case "4": #Mostrar estadisticas
                continue
            case "5": #Salir
                print("Gracias por utilizar nuestro servicio!")
                salir = False


script_dir = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(script_dir, "Paises.csv")

paises = leer_archivo()
lista_paises,lista_poblacion,lista_superficie,lista_continente = crear_listas_columnas(paises)

#main()
if __name__ == "__main__":
    main() # Ejecuta el programa principal
