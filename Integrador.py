import csv
import os
#Funciones manejo de csv
def leer_archivo():
    try:
        with open(RUTA_ARCHIVO,"r",encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = []
            for linea in lector:
                try:
                    paises.append(linea)
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

def main():
    salir = True
    while salir:
        print("--- MENU ---")
        print("1) Buscar país por nombre\n 2) Filtrar países\n 3) Ordenar países\n 4) Mostrar estadísticas\n 5) Salir")
        opc = input("\n Eliga una opción... ")
        
        match opc:
            case "1": #Buscar pais por nombre
                continue
            case "2": #Filtrar paises
                continue
            case "3": #Ordenar paises
                continue
            case "4": #Mostrar estadisticas
                continue
            case "5": #Salir
                print("Gracias por utilizar nuestro servicio!")
                salir = False

RUTA_ARCHIVO = "Programacion 1/Integrador_programacion1/Paises.csv"
paises = leer_archivo()
lista_paises,lista_poblacion,lista_superficie,lista_continente = crear_listas_columnas(paises)

#main()
if __name__ == "__main__":
    main() # Ejecuta el programa principal
