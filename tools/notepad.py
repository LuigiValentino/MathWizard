from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt


TOOL_NAME = "Notepad"

def get_tool():
    
    widget = QWidget()
    widget.setWindowTitle("Notepad (Herramienta de Notas)")

    layout = QVBoxLayout()

   
    text_edit = QTextEdit()
    text_edit.setPlaceholderText("Escribe aquí tus notas...")
    layout.addWidget(text_edit)



    widget.setLayout(layout)
    return widget
