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