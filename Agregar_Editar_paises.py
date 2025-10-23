import time
from Manejo_csv import (
    mostrar_lista_paises, 
    agregar_pais_al_csv, 
    _normalizar_texto as normalizar_para_csv, 
    reescribir_csv
)
from Busqueda_por_nombre import busqueda_nombre_parcial, elegir_nombre
from utilidades import limpiar_pantalla
 
def editar_pais(paises):
    limpiar_pantalla()
    print("--- EDITAR INFORMACIÓN DE UN PAÍS ---")

    # 1. Buscar el país a editar
    nombre_busqueda = input("Ingrese el nombre del país que desea editar: ").strip()
    if not nombre_busqueda:
        print("La búsqueda no puede estar vacía.")
        time.sleep(2)
        return

    paises_encontrados = busqueda_nombre_parcial(nombre_busqueda, paises)

    if not paises_encontrados:
        print("No se encontraron coincidencias para su búsqueda.")
        time.sleep(2)
        return
    
    if len(paises_encontrados) == 1:
        pais_a_editar = paises_encontrados[0]
    else:
        print("\nSe encontraron múltiples coincidencias:")
        pais_a_editar = elegir_nombre(paises_encontrados)

    # Hacemos una copia para poder cancelar la edición si es necesario
    pais_editado = pais_a_editar.copy()
    cambios_realizados = False

    while True:
        limpiar_pantalla()
        print("--- EDITANDO PAÍS ---")
        mostrar_lista_paises([pais_editado])
        print("\n¿Qué campo desea editar?")
        print("1) Nombre")
        print("2) Población")
        print("3) Superficie")
        print("4) Continente")
        print("5) Guardar cambios y salir")
        print("6) Cancelar y volver al menú principal")

        opc = input("Elija una opción: ").strip()

        match opc:
            case "1": # Editar Nombre
                while True:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip().capitalize()
                    if not nuevo_nombre:
                        print("ERROR: El nombre no puede estar vacío.")
                        continue
                    nombre_normalizado = normalizar_para_csv(nuevo_nombre)
                    # Permitir que el nombre sea el mismo, pero no otro que ya exista
                    if any(normalizar_para_csv(p['nombre']) == nombre_normalizado and p is not pais_a_editar for p in paises):
                        print(f"ERROR: El país '{nuevo_nombre}' ya existe.")
                    else:
                        pais_editado['nombre'] = nuevo_nombre
                        cambios_realizados = True
                        break
            case "2": # Editar Población
                while True:
                    poblacion_str = input("Ingrese la nueva población: ").strip()
                    try:
                        poblacion = int(poblacion_str)
                        if poblacion < 0:
                            print("ERROR: La población no puede ser negativa.")
                            continue
                        pais_editado['poblacion'] = poblacion
                        cambios_realizados = True
                        break
                    except ValueError:
                        print("ERROR: Ingrese un número entero válido.")
            case "3": # Editar Superficie
                while True:
                    superficie_str = input("Ingrese la nueva superficie: ").strip()
                    try:
                        superficie = float(superficie_str.replace(',', '.'))
                        if superficie < 0:
                            print("ERROR: La superficie no puede ser negativa.")
                            continue
                        pais_editado['superficie'] = superficie
                        cambios_realizados = True
                        break
                    except (ValueError, TypeError):
                        print("ERROR: Ingrese un número válido.")
            case "4": # Editar Continente
                nuevo_continente = input("Ingrese el nuevo continente: ").strip().capitalize()
                if not nuevo_continente:
                    print("ERROR: El continente no puede estar vacío.")
                else:
                    pais_editado['continente'] = nuevo_continente
                    cambios_realizados = True
            case "5": # Guardar y Salir
                if cambios_realizados:
                    # Actualizamos el diccionario original en la lista de países
                    pais_a_editar.update(pais_editado)
                    if reescribir_csv(paises):
                        print("\n¡Éxito! Los cambios han sido guardados correctamente.")
                    else:
                        print("\nERROR: No se pudieron guardar los cambios en el archivo.")
                else:
                    print("\nNo se realizó ningún cambio.")
                time.sleep(2)
                return
            case "6": # Cancelar
                print("\nEdición cancelada. No se guardaron los cambios.")
                time.sleep(2)
                return
            case _:
                print("Opción no válida. Intente de nuevo.")
                time.sleep(1)

def _validar_nombre_para_agregar(paises):
    """Solicita y valida el nombre para un nuevo país."""
    while True:
        nombre = input("Ingrese el nombre del país: ").strip().capitalize()
        if not nombre:
            print("ERROR: El nombre no puede estar vacío.")
            continue
        nombre_normalizado = normalizar_para_csv(nombre)
        if any(normalizar_para_csv(p['nombre']) == nombre_normalizado for p in paises):
            print(f"ERROR: El país '{nombre}' ya existe en la lista.")
        else:
            return nombre

def _validar_poblacion():
    """Solicita y valida la población."""
    while True:
        poblacion_str = input("Ingrese la población (número entero): ").strip()
        try:
            poblacion = int(poblacion_str)
            if poblacion < 0:
                print("ERROR: La población no puede ser un número negativo.")
                continue
            return poblacion
        except ValueError:
            print("ERROR: Ingrese un número entero válido para la población.")

def _validar_superficie():
    """Solicita y valida la superficie."""
    while True:
        superficie_str = input("Ingrese la superficie (puede usar '.' o ',' como decimal): ").strip()
        try:
            superficie = float(superficie_str.replace(',', '.'))
            if superficie < 0:
                print("ERROR: La superficie no puede ser un número negativo.")
                continue
            return superficie
        except (ValueError, TypeError):
            print("ERROR: Ingrese un número válido para la superficie.")

def _validar_continente():
    """Solicita y valida el continente."""
    while True:
        continente = input("Ingrese el continente: ").strip().capitalize()
        if continente:
            return continente
        print("ERROR: El continente no puede estar vacío.")

def agregar_pais(paises):
    limpiar_pantalla()
    print("--- AGREGAR NUEVO PAÍS ---")

    nombre = _validar_nombre_para_agregar(paises)
    poblacion = _validar_poblacion()
    superficie = _validar_superficie()
    continente = _validar_continente()

    nuevo_pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    
    if agregar_pais_al_csv(nuevo_pais):
        paises.append(nuevo_pais) # Agregamos el país a la lista en memoria
        print(f"\n¡Éxito! El país '{nombre}' ha sido agregado correctamente.")
    else:
        print(f"\nNo se pudo agregar el país '{nombre}' al archivo.")
    time.sleep(2) # Pausa para que el usuario lea el mensaje
