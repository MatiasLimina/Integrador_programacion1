# Integrador_programacion1

Este es el módulo principal de un sistema de gestión de datos de países. Su objetivo es proporcionar una interfaz de **menú interactivo** para que el usuario pueda manipular una base de datos de países almacenada en formato **CSV**.

El sistema permite realizar operaciones comunes como búsqueda, filtrado, ordenamiento, visualización de estadísticas, y la gestión de registros (agregar y editar países).

---

## ⚙️ Requisitos y Estructura

### 1. Requisitos
* **Python 3.10+** (Necesario para la estructura `match-case`).
* Las librerías estándar de Python `csv` y `os`.

### 2. Módulos del Sistema
| Archivo | Propósito Principal |
| :--- | :--- |
| `main.py` | Controla el flujo del programa y el bucle del menú principal. |
| `Manejo_csv.py` | Funciones para leer, inicializar y guardar el archivo CSV. |
| `Busqueda_por_nombre.py` | Lógica para buscar países por coincidencia de nombre. |
| `Filtrado_paises.py` | Lógica para filtrar por continente, población o superficie. |
| `Ordenar_paises.py` | Lógica para ordenar la lista de países. |
| `Estadisticas.py` | Funciones para el cálculo y la presentación de estadísticas. |
| `Sub_Menus.py` | Maneja las interacciones del usuario en los submenús de cada funcionalidad. |
| `utilidades.py` | Funciones auxiliares (ej. validación de entrada). |
| `[Datos].csv` | Archivo donde se almacenan los datos de los países. |

---

## 🚀 Instalación y Ejecución

1.  Asegúrese de que todos los archivos `.py` (incluyendo los módulos importados) y el archivo de datos CSV estén en el mismo directorio.
2.  Ejecute el programa principal desde la terminal:

    ```bash
    python main.py
    ```
    
El programa iniciará automáticamente inicializando el CSV si no existe y cargando los datos.

---

## 🧭 Menú de Funcionalidades

Al ejecutar el programa, se presentará el siguiente menú:

| Opción | Descripción |
| :---: | :--- |
| **1** | **Búsqueda por nombre** (Coincidencia parcial o exacta) |
| **2** | **Filtrar países** (Por continente, rango de población o rango de superficie) |
| **3** | **Ordenar países** (Por diferentes campos) |
| **4** | **Mostrar estadísticas** |
| **5** | **Agregar país** (Crear un nuevo registro) |
| **6** | **Editar país** (Modificar un registro existente) |
| **7** | **Salir** |

---

## 📝 Notas del Flujo Principal

El programa utiliza un bucle **`while not salir`** para mantener el menú activo. Cada opción llama a un módulo específico (a través de la función `sub_menu_...`) para gestionar la lógica de interacción, manteniendo el archivo `main.py` limpio y enfocado en la navegación.

Si la carga inicial de datos (`paises = leer_archivo()`) falla, el programa mostrará un mensaje de error y terminará sin entrar al menú principal.
