def ordenar_por_nombre(lista_de_diccionarios): #Ordena paises por nombre
    return sorted(lista_de_diccionarios, key=lambda pais: pais["nombre"])

def ordenar_por_poblacion(lista_de_diccionarios): #Ordena paises por la clave "poblacion" de forma ascendente
    return sorted(lista_de_diccionarios, key=lambda pais: pais["poblacion"])

def ordenar_por_superficie_ascendente(lista_de_diccionarios): #Ordena paises por superficie de forma ascendente
    return sorted(lista_de_diccionarios, key=lambda pais: pais["superficie"])

def ordenar_por_superficie_descendente(lista_de_diccionarios): #Ordena paises por superficie de forma descendente
    return sorted(lista_de_diccionarios, key=lambda pais: pais["superficie"],reverse=True)
