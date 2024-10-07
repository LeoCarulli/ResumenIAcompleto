# file_reader.py
import pdfplumber  # Asegúrate de tener instalado pdfplumber
from docx import Document  # Para manejar archivos Word (.docx)

def read_file(file_path):
    """Lee un archivo PDF, DOCX o TXT y retorna su contenido en formato de texto."""
    if file_path.endswith('.pdf'):
        return read_pdf(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    elif file_path.endswith('.txt'):
        return read_txt(file_path)
    else:
        raise ValueError("Formato de archivo no soportado. Solo se aceptan PDF, DOCX y TXT.")

def read_pdf(file_path):
    """Lee un archivo PDF y extrae su texto."""
    with pdfplumber.open(file_path) as pdf:
        return '\n'.join(page.extract_text() for page in pdf.pages)

def read_docx(file_path):
    """Lee un archivo DOCX y extrae su texto."""
    doc = Document(file_path)
    return '\n'.join(para.text for para in doc.paragraphs)

def read_txt(file_path):
    """Lee un archivo TXT y extrae su texto."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
