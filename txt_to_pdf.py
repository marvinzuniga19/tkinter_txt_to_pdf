import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from reportlab.pdfgen import canvas



def convertir_archivo_a_pdf(): 

    # Crear ventana de selección de archivo
    Tk().withdraw()
    archivo = askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    
    # Obtener la ruta completa de la carpeta "Documentos"
    ruta_documentos = os.path.expanduser("~/Documentos")
    
    # Obtener el nombre del archivo PDF
    archivo_pdf = os.path.basename(archivo).replace('.txt', '.pdf')
    
    # Unir la ruta de la carpeta "Documentos" y el nombre del archivo PDF
    archivo_pdf_completo = os.path.join(ruta_documentos, archivo_pdf)
    
    # Convertir archivo de texto a PDF
    with open(archivo, 'r') as f:
        texto = f.read()
    
    # Crear objeto de lienzo de ReportLab
    pdf = canvas.Canvas(archivo_pdf_completo)
    
    # Agregar texto al lienzo
    pdf.drawString(100, 750, texto)
    
    # Guardar PDF
    pdf.save()

convertir_archivo_a_pdf()
