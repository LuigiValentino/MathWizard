#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt

CALCULATOR_NAME = "Calculadora de Potencia"
CALCULATOR_SHORTCUT = "Ctrl+K"

class PowerCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Potencia")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada de base
        self.base_input = QLineEdit()
        self.base_input.setAlignment(Qt.AlignRight)
        main_layout.addWidget(QLabel("Ingrese la base:"))
        main_layout.addWidget(self.base_input)

        # Entrada de exponente
        self.exponent_input = QLineEdit()
        self.exponent_input.setAlignment(Qt.AlignRight)
        main_layout.addWidget(QLabel("Ingrese el exponente:"))
        main_layout.addWidget(self.exponent_input)

        # Botón para calcular la potencia
        self.calculate_button = QPushButton("Calcular Potencia")
        self.calculate_button.clicked.connect(self.calculate_power)
        main_layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate_power(self):
        """Calcula la potencia de un número (base ^ exponente)."""
        try:
            # Obtener la base y el exponente
            base = float(self.base_input.text())
            exponent = float(self.exponent_input.text())

            # Calcular la potencia
            result = base ** exponent
            self.result_label.setText(f"Resultado: {result}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese valores numéricos válidos.")
            self.result_label.setText("Resultado: ")

def get_calculator():
    return PowerCalculator()
