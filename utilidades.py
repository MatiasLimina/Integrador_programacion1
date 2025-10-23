import os
def limpiar_pantalla():
    #Limpia la pantalla de la terminal. 'cls' para Windows, 'clear' para otros.
    os.system('cls' if os.name == 'nt' else 'clear')