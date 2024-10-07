# file_reader.py
import pdfplumber  # Asegúrate de tener instalado pdfplumber
from docx import Document  # Para manejar archivos Word (.docx)

def leer_archivo(ruta_archivo):
    """Lee un archivo PDF, DOCX o TXT y retorna su contenido en formato de texto."""
    if ruta_archivo.endswith('.pdf'):
        return leer_pdf(ruta_archivo)
    elif ruta_archivo.endswith('.docx'):
        return leer_docx(ruta_archivo)
    elif ruta_archivo.endswith('.txt'):
        return leer_txt(ruta_archivo)
    else:
        raise ValueError("Formato de archivo no soportado. Solo se aceptan PDF, DOCX y TXT.")

def leer_pdf(ruta_archivo):
    """Lee un archivo PDF y extrae su texto."""
    with pdfplumber.open(ruta_archivo) as pdf:
        return '\n'.join(page.extract_text() for page in pdf.pages)

def leer_docx(ruta_archivo):
    """Lee un archivo DOCX y extrae su texto."""
    doc = Document(ruta_archivo)
    return '\n'.join(para.text for para in doc.paragraphs)

def leer_txt(ruta_archivo):
    """Lee un archivo TXT y extrae su texto."""
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        return file.read()
