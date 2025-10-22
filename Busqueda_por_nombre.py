import unicodedata

def _normalizar_texto(texto):
    """Convierte a minúsculas y quita acentos de un texto."""
    texto = texto.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

#Funciones buscar por nombre
def busqueda_nombre_parcial(termino_busqueda, diccionario): #Realiza la busqueda de coincidencias
    coincidencias = []
    termino_normalizado = _normalizar_texto(termino_busqueda)
    
    # Caso de búsqueda exacta (insensible a mayúsculas y acentos)
    for pais in diccionario:
        if _normalizar_texto(pais.get("nombre", "")) == termino_normalizado:
            return [pais]

    # Si no hay coincidencia exacta, busca coincidencias que comiencen con el término (insensible a mayúsculas y acentos)
    for pais in diccionario:
        if _normalizar_texto(pais.get("nombre", "")).startswith(termino_normalizado):
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