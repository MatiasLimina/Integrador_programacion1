# 🗺️ Administrador de Datos de Países 🌎

---

## 📝 Descripción del Programa

Este programa en **Python** es una herramienta de administración que permite la gestión interactiva de una base de datos de países almacenada en un archivo **CSV**.

El sistema carga los datos al inicio (asegurándose de que el archivo CSV exista) y ofrece un **menú principal** con diversas funcionalidades para manipular, consultar y analizar la información de los países.

### ⚙️ Funcionalidades Principales

* **Búsqueda:** Buscar países por nombre (coincidencia parcial o exacta).
* **Filtrado:** Filtrar países por continente, rango de población o rango de superficie.
* **Ordenamiento:** Ordenar la lista de países según un criterio seleccionado.
* **Estadísticas:** Mostrar datos estadísticos sobre los países cargados.
* **CRUD Básico:**
    * Agregar un nuevo país a la base de datos.
    * Editar la información de un país existente.

El programa utiliza varios módulos (`Manejo_csv`, `Busqueda_por_nombre`, `Filtrado_paises`, `Ordenar_paises`, `Estadisticas`, `Sub_Menus`, `utilidades`) para mantener el código organizado y modular.

---

## 🚀 Instrucciones de Uso

### 1. Requisitos

* Tener instalado **Python 3.x**.
* Asegurarse de que todos los módulos (`Manejo_csv.py`, `Busqueda_por_nombre.py`, etc.) estén presentes en el mismo directorio que el archivo principal que contiene el código `main`.

### 2. Ejecución

1.  Guarda el código principal y todos los módulos en un mismo directorio.
2.  Abre una terminal o símbolo del sistema.
3.  Navega hasta el directorio donde guardaste los archivos.
4.  Ejecuta el programa con el siguiente comando:

    ```bash
    python3 nombre_del_archivo_principal.py 
    # O simplemente:
    python nombre_del_archivo_principal.py
    ```

### 3. Interacción

Una vez ejecutado, el programa mostrará el **Menú Principal**:

--- MENU ---

    Busqueda por nombre

    Filtrar países

    Ordenar países

    Mostrar estadísticas

    Agregar país

    Editar país

    Salir


1.  **Ingresa el número** de la opción deseada y presiona **Enter**.
2.  El programa te guiará a través de **submenús** o solicitará la entrada de datos (nombres, rangos, etc.) según la opción elegida.
3.  Al finalizar una operación, presiona **Enter** para volver al Menú Principal.
4.  Selecciona la opción **7) Salir** para finalizar el programa.

---

## 💻 Ejemplos de Entradas y Salidas

### 📌 Ejemplo de Menú Principal e Interacción

**Salida (Menú Principal):**

--- MENU ---

    Busqueda por nombre

    Filtrar países

    Ordenar países

    Mostrar estadísticas

    Agregar país

    Editar país

    Salir Ingrese su opción:


**Entrada (Usuario selecciona la opción 2 - Filtrar países):**

2


**Salida (Submenú de Filtrado):**

--- FILTRAR PAÍSES ---

    Por continente

    Por rango de población

    Por rango de superficie

    Volver Ingrese su opción:


**Entrada (Usuario selecciona la opción 2 - Rango de Población):**

2 Ingrese población mínima:


**Entrada (Usuario ingresa los rangos):**

10000000 Ingrese población máxima: 50000000


**Salida (Resultado del Filtrado - Ejemplo):**

Resultados del filtro de población [10000000 a 50000000]: | País | Continente | Población | Superficie (km²) | |---|---|---|---| | Colombia | América | 51000000 | 1141748 | | España | Europa | 47000000 | 505990 | ... Presione Enter para volver al menú principal...


---

## 👥 Participación de los Integrantes

| Rol/Módulo Principal | Integrante(s) |
| :--- | :--- |
| **Manejo_csv.py** (Inicialización, lectura, escritura) | [Limina Matias y Agüero Lautaro] |
| **Busqueda_por_nombre.py** (Búsqueda) | [Limina Matias y Agüero Lautaro] |
| **Filtrado_paises.py** (Filtros) | [Limina Matias y Agüero Lautaro] |
| **Ordenar_paises.py** (Ordenamiento) | [Limina Matias y Agüero Lautaro] |
| **Estadisticas.py** (Cálculos estadísticos) | [Limina Matias y Agüero Lautaro] |
| **Sub_Menus.py y utilidades.py** (Manejo de menús y validaciones) | [Limina Matias y Agüero Lautaro] |
| **Función main y estructura principal** | [Limina Matias y Agüero Lautaro] |
