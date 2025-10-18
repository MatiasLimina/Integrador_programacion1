import csv
import os
#Funciones manejo de csv
def leer_archivo(): #Leer Archivo CSV
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

def main(): #Menú completo
    salir = True
    while salir:
        print("--- MENU ---")
        print(" \n 1) Filtrar países\n 2) Ordenar países\n 3) Mostrar estadísticas\n 4) Salir")
        opc = input("\n Eliga una opción... ")
        
        match opc:
            case "1":#Buscar pais por nombre
                continue
            case "2":#Filtrar paises
                print("1) Filtrar por nombre\n2) Filtrar por pobalción\n3) Filtrar por superficie\n4) Filtrar por Contiente\n5) Salir")
                opc_categoria=int(input("Ingrese el filtro que desea aplicar: ")) #Seleccionar Filtro
                match opc_categoria:
                    case "1": #Filtrar por nombre
                        print("entra opc 1")
                    case "2": #Filtrar por población
                        print("entra opc 2")
                    case "3": #Filtrar por superficie
                        print("entra opc 3")
                    case "4": #Filtrar por continente
                        print("entra opc 4")
                    case "5": #Salir
                        print("Volver al menú principal.")
                    case _: #Eror
                        print("Selecciones una opción válida.")
            case "3":#Ordenar paises
                continue
            case "4":#mostrar estadisticas
                continue
            case "5":
                print("Gracias por utilizar nuestro servicio!")
                salir = False

script_dir = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(script_dir, "Paises.csv") #Selecciona lugar de origen del CSV
paises = leer_archivo()
lista_paises,lista_poblacion,lista_superficie,lista_continente = crear_listas_columnas(paises)

#main()
if __name__ == "__main__":
    main() # Ejecuta el programa principal

