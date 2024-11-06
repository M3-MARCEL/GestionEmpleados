from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

class Informe:
    def __init__(self, id_informe, nombre_informe, fecha_creacion, creador, ubicacion):
        self.id_informe = id_informe
        self.nombre_informe = nombre_informe
        self.fecha_creacion = fecha_creacion
        self.creador = creador
        self.ubicacion = ubicacion

    def generar_pdf(self):
        # Define la ruta y el nombre del archivo PDF
        pdf_path = f"{self.nombre_informe}.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        
        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, f"Informe: {self.nombre_informe}")
        
        # Detalles del informe
        c.setFont("Helvetica", 12)
        c.drawString(100, 720, f"ID Informe: {self.id_informe}")
        c.drawString(100, 700, f"Fecha de Creación: {self.fecha_creacion}")
        c.drawString(100, 680, f"Creador: {self.creador.nombre}")

        # Cerrar y guardar el PDF
        c.save()
        print(f"PDF generado exitosamente en: {pdf_path}")

    def exportar_excel(self):
        # Crea un DataFrame con los datos del informe
        data = {
            "ID Informe": [self.id_informe],
            "Nombre Informe": [self.nombre_informe],
            "Fecha de Creación": [self.fecha_creacion],
            "Creador": [self.creador.nombre],
            "Ubicación": [self.ubicacion]
        }
        df = pd.DataFrame(data)
        
        # Define la ruta y el nombre del archivo Excel
        excel_path = f"{self.nombre_informe}.xlsx"
        df.to_excel(excel_path, index=False)
        print(f"Excel exportado exitosamente en: {excel_path}")