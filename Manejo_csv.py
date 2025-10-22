import csv
import os
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
        print(f"Pais: {pais['nombre']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']}km2, Continente: {pais['continente']}")

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
        superficie = float(superficie) #Rechequar esto
    except ValueError: 
        print(f"ERROR: {superficie} datos inválidos, el campo ¨superficie¨ espera un entero")
        return None
    linea_validada = {"nombre":pais,"poblacion":poblacion,"superficie":superficie,"continente":continente}
    return linea_validada
#RUTA DEL CSV
script_dir = os.path.dirname(os.path.abspath(__file__)) 
RUTA_ARCHIVO = os.path.join(script_dir, "Paises.csv")