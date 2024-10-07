# Resumen de Archivos PDF, Word o Txt
Este repo está pensado para automatizar la creación de resúmenes de archivos **PDF, Word y TXT** GRATIS usando **Python** y **Ollama**. Está pensado para ser fácil de entender, incluso para quienes recién empiezan.

Incluye un **Jupyter Notebook** que explica paso a paso el proceso de generar resúmenes, y un script en Python listo para producción.
## Contenido

- **main.py**: Script principal para ejecutar nuestros resúmenes. 
- **lector_archivos.py**: Script adicional con funciones para leer y procesar los archivos de PDF, word o txt. 
- **requirements.txt**: Acá están todas las librerías que necesitás para que todo funcione sin problemas.
- **data/**: Es la carpeta donde tenés que poner el / los archivos que quieras resumir.

## Requisitos

### Generales

1. **Instalá Python** desde [Python](https://www.python.org/downloads/).

2. **Instalá Visual Studio Code** desde [VSC](https://code.visualstudio.com/download) o cualquier editor de código de tu preferencia. Recomiendo Visual Studio Code por su facilidad de uso y funcionalidades.

3. **Descargá e instalá Ollama** desde [Ollama](https://ollama.com/) y el modelo de lenguaje natural que prefieras desde [Library](https://ollama.com/library).

En nuestro código, tenemos seteado por default el modelo **phi3.5**, el cual podes descargar aquí: [Phi3.5](https://ollama.com/library/phi3.5). Para mejores resultados, recomendable usar **llama3**. Es recomendable ver los requisitos de cada modelo para ver cuál podes usar según tu PC. 

### Requisitos de ejecución

- Para el archivo **PDFpasoapaso.ipynb**, con esto ya debería ser suficiente para poder correrlo celda a celda.

- Para el archivo **PDFunificado.py**, también es necesario instalar las librerías correspondientes. En este caso, se puede hacer a través del siguiente comando desde la consola:

```bash
pip install pdfplumber
pip install python-docx
```
Sin embargo, es una buena práctica en este tipo de proyectos, crear un entorno virtual con todas las dependencias necesarias para evitar problemas de incompatibilidad entre versiones. Te dejo un ejemplo de cómo crear el entorno virtual, activarlo e instalar las dependencias necesarias:

1. **Creá un entorno virtual** con el siguiente comando:

  ```bash
  python -m venv "nombre_del_entorno"
  ```

2. **Activá el entorno virtual**:
  - En Windows:
    ```bash
    nombre_del_entorno\Scripts\activate
    ```
    > Puede que haya un error si es la primera vez que lo haces. Se soluciona ejecutando el siguiente comando:
    > ```bash
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    > ```
  - En macOS/Linux:
    ```bash
    source nombre_del_entorno/bin/activate
    ```

3. **Instalá las librerías** que están en `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

## Cómo usar cada archivo

- **main.py (Resúmenes para PDF)**: Si querés resumir un archivo rápidamente, usá este comando en la terminal (siempre estando sobre la carpeta donde está el archivo a ejecutar):
    ```bash
    python main.py
    ```
Asegurate de que el archivo PDF que querés resumir esté en la carpeta `data/`, y especificado en el archivo main. 

## Estructura del Proyecto

```bash
├── main.py                 # Script para ejecutar el resumen
├── lector_archivos.py         # Script con las funciones para leer los distintos tipos de archivo
├── requirements.txt        # Librerías necesarias
└── data/                   # Carpeta donde guardar el archivo a resumir
```
