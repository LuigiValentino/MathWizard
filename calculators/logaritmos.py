#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
import math

CALCULATOR_NAME = "Logaritmos"
CALCULATOR_SHORTCUT = "Ctrl+I"

class LogarithmCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Logaritmos")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.number_input = QLineEdit()
        self.base_input = QLineEdit()
        self.result_area = QTextEdit()

        main_layout.addWidget(QLabel("Número:"))
        main_layout.addWidget(self.number_input)
        main_layout.addWidget(QLabel("Base (opcional, predeterminado es 10):"))
        main_layout.addWidget(self.base_input)

        self.calculate_button = QPushButton("Calcular Logaritmo")
        self.calculate_button.clicked.connect(self.calculate_logarithm)

        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(QLabel("Resultado:"))
        main_layout.addWidget(self.result_area)

        self.setLayout(main_layout)

    def calculate_logarithm(self):
        try:
            # Obtener el número del campo de entrada
            number = float(self.number_input.text())
            if number <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            
            # Obtener la base, si está vacía se usa la base 10 por defecto
            base_text = self.base_input.text().strip()
            base = float(base_text) if base_text else 10

            if base <= 0:
                raise ValueError("La base debe ser mayor que 0.")

            # Calcular el logaritmo
            result = math.log(number, base)

            # Mostrar el resultado en el área de texto
            self.result_area.setText(f"Logaritmo: {result}")
        except ValueError as e:
            self.result_area.setText(f"Error: {e}")
        except Exception as e:
            self.result_area.setText(f"Error al calcular el logaritmo: {e}")

def get_calculator():
    return LogarithmCalculator()
