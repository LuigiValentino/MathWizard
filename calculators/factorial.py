#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt

CALCULATOR_NAME = "Calculadora de Factorial"
CALCULATOR_SHORTCUT = "Ctrl+G"

class FactorialCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Factorial")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada de valor
        self.value_input = QLineEdit()
        self.value_input.setAlignment(Qt.AlignRight)
        main_layout.addWidget(QLabel("Ingrese un número entero:"))
        main_layout.addWidget(self.value_input)

        # Botón para calcular el factorial
        self.calculate_button = QPushButton("Calcular Factorial")
        self.calculate_button.clicked.connect(self.calculate_factorial)
        main_layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate_factorial(self):
        """Calcula el factorial de un número ingresado."""
        try:
            # Obtener el número ingresado
            number = int(self.value_input.text())

            if number < 0:
                raise ValueError("El número debe ser positivo o cero.")
            
            # Calcular el factorial
            result = self.factorial(number)
            self.result_label.setText(f"Resultado: {result}")

        except ValueError as e:
            QMessageBox.warning(self, "Error", f"Entrada no válida. {str(e)}")
            self.result_label.setText("Resultado: ")

    def factorial(self, n):
        """Calcula el factorial de un número de manera recursiva."""
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

def get_calculator():
    return FactorialCalculator()
