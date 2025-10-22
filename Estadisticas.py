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