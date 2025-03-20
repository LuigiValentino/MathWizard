#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt

HELP_NAME = "Glosario"
HELP_SHORTCUT = "A"

def get_help():
    return HelpGlossaryWidget()

class HelpGlossaryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glosario de Herramientas")
        self.init_ui()
        self.setGeometry(0, 0, 1200, 600)

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
            h5 { font-size: 24px; }
            h1 { color: #333; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #e0e0e0; }
        """)
        html_content = """
        <html>
          <head>
            <style>
              body { margin: 0; padding: 0; }
            </style>
          </head>
          <body>
            <h1>Glosario de Herramientas</h1>
            <p>A continuación se listan las principales secciones de MathWizard:</p>
            <hr>
            <h2>Calculadoras</h2>
            
            <h5><u>Calculadora</u> (Ctrl + A)</h5>
            <h5><u>Calculadora de ángulos</u> (Ctrl + B)</h5>
            <h5><u>Calculadora de áreas</u> (Ctrl + C)</h5>
            <h5><u>Combinaciones y permutaciones</u> (Ctrl + D)</h5>
            <h5><u>Derivadas e integrales</u> (Ctrl + E)</h5>
            <h5><u>Ecuaciones cuadráticas</u> (Ctrl + F)</h5>
            <h5><u>Calculadora de Factorial</u> (Ctrl + G)</h5>
            <h5><u>Sistema de ecuaciones lineales</u> (Ctrl + H)</h5>
            <h5><u>Logaritmos</u> (Ctrl + I)</h5>
            <h5><u>Calculadora de MCD, MCM y estadísticas</u> (Ctrl + J)</h5>
            <h5><u>Calculadora de potencia</u> (Ctrl + K)</h5>
            <h5><u>Calculadora de raíz</u> (Ctrl + L)</h5>
            <h5><u>Calculadora de sucesiones y series</u> (Ctrl + M)</h5>
            <h5><u>Calculadora de conversiones de unidades</u> (Ctrl + N)</h5>
            <hr>
            <h2>Graficadoras</h2>
            
            <h5><u>Grafico de área</u> (Ctrl + O)</h5>
            <h5><u>Grafico de burbujas</u> (Ctrl + P)</h5>
            <h5><u>Grafico de cajas</u> (Ctrl + Q)</h5>
            h5><u>Grafico de calor</u> (Ctrl + R)</h5>
            <h5><u>Grafico de dispersión complejo</u> (Ctrl + S)</h5>
            <h5><u>Grafico de embudo</u> (Ctrl + T)</h5>
            <h5><u>Grafico de interactivos</u> (Ctrl + U)</h5>
            <h5><u>Histograma</u> (Ctrl + V)</h5>
            <h5><u>Grafico de líneas múltiples</u> (Ctrl + W)</h5>
            <h5><u>Grafico de matríz de correlación</u> (Ctrl + X)</h5>
            <h5><u>Grafico de pareto</u> (Ctrl + Y)</h5>
            <h5><u>Grafico de radar</u> (Ctrl + Z)</h5>
            <h5><u>Grafico de línea de tendencia</u> (Ctrl + 1)</h5>
            <h5><u>Grafico de velocímetro</u> (Ctrl + 2)</h5>
            <h5><u>Grafico de violín</u> (Ctrl + 3)</h5>
          </body>
        </html>
        """
        self.textBrowser.setHtml(html_content)
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)



