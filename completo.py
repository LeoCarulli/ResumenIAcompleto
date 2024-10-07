# main.py
from file_reader import read_file  # Importamos las funciones del archivo separado
import subprocess

# Función para generar un resumen del texto cargado usando subprocess
def generar_resumen_con_subprocess(texto):
    # Preparamos el mensaje que se enviará al modelo
    mensaje = f"Por favor, haceme un resumen detallado en español del siguiente texto:\n\n{texto}"
    
    # Ejecutamos el comando de Ollama usando subprocess
    resultado = subprocess.run(
        ['ollama', 'run', 'phi3.5'],  # Comando para ejecutar el modelo
        input=mensaje,                # El mensaje con el texto
        text=True,                    # Indicamos que el input es texto
        capture_output=True,          # Capturamos la salida
        encoding='utf-8'              # Codificación para manejar caracteres especiales
    )
    
    return resultado.stdout  # Retornamos el resultado del resumen

# Main
ruta_archivo = "data/teemo.pdf"  # Define la ruta de tu archivo aquí

# Cargamos el contenido del archivo (ya sea txt, docx o pdf)
texto = read_file(ruta_archivo)

# Generamos el resumen del contenido usando subprocess
resumen = generar_resumen_con_subprocess(texto)

# Mostramos el resumen en pantalla
print(resumen)
