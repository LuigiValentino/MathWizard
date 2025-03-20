#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt

HELP_NAME = "Acerca de MathWizard"
HELP_SHORTCUT = "C"

def get_help():
    return AboutMathWizardWidget()

class AboutMathWizardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acerca de MathWizard")
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
            p { margin: 10px 0; }
            ul { margin: 10px 20px; }
            a { color: #3498db; text-decoration: none; }
            a:hover { text-decoration: underline; }
        """)
        html_content = """
        <html>
          <head>
            <style>
              body { margin: 0; padding: 0; }
            </style>
          </head>
          <body>
            <h1>Acerca de MathWizard</h1>
            <p><strong>MathWizard</strong> es un software integral que combina calculadoras y herramientas de graficación, diseñado para facilitar el análisis matemático y la visualización de datos de manera interactiva y modular.</p>
            <h2>Tecnologías y Programación</h2>
            <p>MathWizard está desarrollado utilizando:</p>
            <ul>
              <li><strong>Python</strong> como lenguaje de programación.</li>
              <li><strong>PyQt5</strong> para la interfaz gráfica de usuario.</li>
              <li><strong>Matplotlib</strong> y <strong>Seaborn</strong> para la visualización de datos.</li>
            </ul>
            <h2>Autor</h2>
            <p>Desarrollado por <strong>Luigi Adducci</strong>.</p>
            <hr>
            <p>Para reportar bugs, dudas o sugerencias, por favor contacta a: <a href="mailto:luigiadduccidev@gmail.com">luigiadduccidev@gmail.com</a></p>
            <h2>Licencia y Condiciones</h2>
            <p>MathWizard se distribuye bajo una licencia de software libre. Se prohíbe alterar o redistribuir el código sin autorización. Al usar este software, aceptas las siguientes condiciones:</p>
            <ul>
              <li>No modificar el código fuente sin autorización.</li>
              <li>No redistribuir versiones modificadas sin el consentimiento del autor.</li>
            </ul>
            <p>Gracias por usar MathWizard y contribuir a la comunidad de análisis y visualización de datos.</p>
          </body>
        </html>
        """
        self.textBrowser.setHtml(html_content)
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)
