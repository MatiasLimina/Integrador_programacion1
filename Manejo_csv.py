import csv
import os
import unicodedata

NOMBRES_COLUMNAS = ["nombre", "poblacion", "superficie", "continente"]
ENCABEZADOS = ["nombre", "poblacion", "superficie", "continente"]

def inicializar_csv_si_no_existe():
    """Verifica si el archivo CSV existe. Si no, lo crea con las cabeceras."""
    if not os.path.exists(RUTA_ARCHIVO):
        try:
            with open(RUTA_ARCHIVO, 'w', encoding="UTF-8", newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=NOMBRES_COLUMNAS)
                escritor.writeheader()
            print(f"AVISO: No se encontró el archivo '{os.path.basename(RUTA_ARCHIVO)}'. Se ha creado uno nuevo y vacío.")
        except IOError as e:
            print(f"ERROR CRÍTICO: No se pudo crear el archivo CSV: {e}")

def leer_archivo():
    try: 
        with open(RUTA_ARCHIVO,"r",encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = []
            nombres_vistos = set() # Conjunto para rastrear nombres de países ya vistos
            for i, linea in enumerate(lector, start=2): # Empezamos en 2 para contar la línea del CSV (1 es cabecera)
                # Pasamos el conjunto de nombres vistos para que la función valide duplicados
                linea_valida = validar_csv(linea, nombres_vistos, i)
                if linea_valida:
                    paises.append(linea_valida) #Si la línea es válida la agrega a la lista
            return paises
    except FileNotFoundError: 
        return None

def agregar_pais_al_csv(nuevo_pais):
    """Agrega un nuevo país (diccionario) al final del archivo CSV."""
    try:
        # Verificamos si el archivo existe y no está vacío para chequear el último carácter.
        needs_newline = False
        if os.path.exists(RUTA_ARCHIVO) and os.path.getsize(RUTA_ARCHIVO) > 0:
            with open(RUTA_ARCHIVO, 'r', encoding="UTF-8") as f:
                f.seek(0, os.SEEK_END) # Ir al final del archivo
                f.seek(f.tell() - 1, os.SEEK_SET) # Retroceder un carácter
                if f.read(1) != '\n':
                    needs_newline = True # El archivo no termina con un salto de línea

        # 'a' para append (agregar), newline='' para evitar líneas en blanco entre filas
        with open(RUTA_ARCHIVO, "a", encoding="UTF-8", newline='') as archivo:
            if needs_newline:
                archivo.write('\n') # Agregamos el salto de línea que faltaba
            # DictWriter necesita los nombres de las columnas para escribir correctamente
            escritor = csv.DictWriter(archivo, fieldnames=NOMBRES_COLUMNAS)
            escritor.writerow(nuevo_pais)
        return True
    except IOError as e:
        print(f"ERROR: No se pudo escribir en el archivo CSV: {e}")
        return False

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

def _normalizar_texto(texto):
    """Convierte a minúsculas, quita acentos y espacios extra de un texto."""
    texto = texto.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def validar_csv(linea, nombres_vistos, numero_linea): #Valida cada línea del csv antes de agregarlo a la lista de diccionarios
    pais = linea.get("nombre")
    poblacion = linea.get("poblacion") 
    superficie = linea.get("superficie")
    continente = linea.get("continente")
    if not pais: 
        print(f"ADVERTENCIA: Línea {numero_linea}: El campo 'nombre' está vacío. Se omite la línea.")
        return None
    if not continente: 
        print(f"ADVERTENCIA: Línea {numero_linea}: El campo 'continente' para '{pais}' está vacío. Se omite la línea.")
        return None
    try: 
        poblacion = int(poblacion)
    except ValueError: 
        print(f"ADVERTENCIA: Línea {numero_linea}: Dato de población inválido ('{poblacion}') para '{pais}'. Se omite la línea.")
        return None
    try: 
        # Reemplazamos la coma por un punto para poder convertir a float sin problemas.
        superficie = float(str(superficie).replace(',', '.'))
    except (ValueError, TypeError): 
        print(f"ADVERTENCIA: Línea {numero_linea}: Dato de superficie inválido ('{superficie}') para '{pais}'. Se omite la línea.")
        return None
    
    # Verificación de duplicados
    nombre_normalizado = _normalizar_texto(pais)
    if nombre_normalizado in nombres_vistos:
        print(f"ADVERTENCIA: Línea {numero_linea}: País duplicado encontrado ('{pais}'). Se omite la línea.")
        return None
    nombres_vistos.add(nombre_normalizado) # Si no es duplicado, se agrega al conjunto

    linea_validada = {"nombre":pais,"poblacion":poblacion,"superficie":superficie,"continente":continente}
    return linea_validada
#RUTA DEL CSV
script_dir = os.path.dirname(os.path.abspath(__file__)) 
RUTA_ARCHIVO = os.path.join(script_dir, "Paises.csv")