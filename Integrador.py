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

def mostrar_linea(diccionario,linea):
    for pais in diccionario:
        if pais.get("nombre", "") == linea:
            return f"Pais: {pais["nombre"]} Población: {pais["poblacion"]} Superficie: {pais["superficie"]} Continente: {pais["continente"]}"

#Funciones buscar por nombre
def busqueda_nombre_parcial(nombre,diccionario): #Realiza la busqueda de coincidencias
    encontrado = False
    coincidencias = []
    for pais in diccionario:
        if pais.get("nombre", "") == nombre: #Si la busqueda es exacta
            return nombre
        if nombre in pais.get("nombre", "") :
            encontrado = True
            coincidencias.append(pais["nombre"])
    if encontrado == False:
        return "No encontrado"
    else:
        return coincidencias

def elegir_nombre(coincidencias,diccionario): #Muestra coincidencias al usuario
    print("Esta es la lista de paises que coinciden con su busqueda")
    for i in range(len(coincidencias)):
        print(f"ID: {i} Pais: {coincidencias[i]}")
    eleccion_id = id_busqueda(len(coincidencias)-1)
    pais_buscado = coincidencias[eleccion_id]
    return mostrar_linea(diccionario,pais_buscado)

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

#MAIN
def main():
    salir = True
    while salir:
        print("--- MENU ---")
        print(" 1) Busqueda por nombre\n 2) Filtrar países\n 3) Ordenar países\n 4) Mostrar estadísticas\n 5) Salir")
        opc = input("\n Eliga una opción... ")
        
        match opc:
            case "1":#Buscar pais por nombre (coincidencia parcial o exacta).
                nombre = input("Ingrese un nombre ").capitalize().strip()
                busqueda_posibles = busqueda_nombre_parcial(nombre,paises)
                if busqueda_posibles == "No encontrado":
                    print("No se encontraron coincidencias")
                elif busqueda_posibles in lista_paises:
                    print(mostrar_linea(paises,busqueda_posibles))
                else:
                    pais_buscado = elegir_nombre(busqueda_posibles,paises)
                    print (pais_buscado)
                    
            case "2":#Filtrar paises
                continue
            case "3":#Ordenar paises
                continue
            case "4":#mostrar estadisticas
                continue
            case "5":
                print("Gracias por utilizar nuestro servicio!")
                salir = False

# --- Construcción de la ruta de archivo de forma robusta ---
# Obtenemos la ruta absoluta del directorio donde se encuentra este script.
script_dir = os.path.dirname(os.path.abspath(__file__))
# Unimos la ruta del script con el nombre del archivo CSV para obtener la ruta completa.
RUTA_ARCHIVO = os.path.join(script_dir, "Paises.csv")

paises = leer_archivo()
lista_paises,lista_poblacion,lista_superficie,lista_continente = crear_listas_columnas(paises)

#main()
if __name__ == "__main__":
    main() # Ejecuta el programa principal
