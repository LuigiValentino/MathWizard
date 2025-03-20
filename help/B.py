#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt

HELP_NAME = "Instrucciones y Formatos"
HELP_SHORTCUT = "B"

def get_help():
    return InstructionsWidget()

class InstructionsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instrucciones y Formatos")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.textBrowser = QTextBrowser()
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setStyleSheet("""
            QTextBrowser {
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #333;
                background-color: #f9f9f9;
                border: none;
                padding: 10px;
            }
            h1 { color: #333; }
            h2 { color: #555; }
            table { width: 100%; border-collapse: collapse; margin-top: 10px; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #e0e0e0; }
            p { margin: 10px 0; }
            ul { margin: 10px 20px; }
        """)
        html_content = """
        <html>
          <head>
            <style>
              body { margin: 0; padding: 0; }
            </style>
          </head>
          <body>
            <h1>Instrucciones y Formatos</h1>
            <p><strong>MathWizard</strong> es una aplicación integral que integra calculadoras y graficadores.</p>
            <hr>
            <h2>Top Bar</h2>
            <p>En la barra superior encontrarás cuatro secciones:</p>
            <ul>
              <li><strong>Calculadoras (C)</strong>: Accede a diversas calculadoras matemáticas.</li>
              <li><strong>Gráficos (G)</strong>: Visualiza diferentes tipos de gráficos.</li>
              <li><strong>Herramientas (H)</strong>: Incluye utilidades como Notepad y Dibujo.</li>
              <li><strong>Ayuda (A)</strong>: Aquí encuentras instrucciones, glosario y otros recursos.</li>
            </ul>
            <br>
            <h2>Formato para uso</h2>
            <ul>
              <li>Utiliza <strong>coma (,)</strong> para separar números o valores dentro de un mismo grupo.</li>
              <li>Utiliza el <strong>pipe (|)</strong> para separar diferentes grupos de datos.</li>
              <li>Utiliza el <strong>punto y coma (;)</strong> para separar elementos dentro de un grupo (por ejemplo, en gráficos de violín o Gantt).</li>
              <li>Utiliza <strong>paréntesis ( )</strong> para agrupar coordenadas cuando sea necesario, como en gráficos de dispersión o burbuja.</li>
            </ul>
            <p>Estas son las instrucciones básicas para utilizar MathWizard. ¡Explora cada sección y experimenta con los diferentes formatos para aprovechar al máximo la herramienta!</p>
          </body>
        </html>
        """
        self.textBrowser.setHtml(html_content)
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)

