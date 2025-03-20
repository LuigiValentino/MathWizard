#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
import sympy as sp

CALCULATOR_NAME = "Derivadas e Integrales"
CALCULATOR_SHORTCUT = "Ctrl+E"

class DerivativeIntegralCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(CALCULATOR_NAME)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Campo de entrada de expresión matemática
        self.expression_input = QLineEdit()
        self.result_area = QTextEdit()

        main_layout.addWidget(QLabel("Expresión (en términos de x) EJ; x**2 + 3*x + 5"))
        main_layout.addWidget(self.expression_input)

        # Botones para calcular derivada e integral
        self.derivative_button = QPushButton("Calcular Derivada")
        self.integral_button = QPushButton("Calcular Integral")

        self.derivative_button.clicked.connect(self.calculate_derivative)
        self.integral_button.clicked.connect(self.calculate_integral)

        # Agregar botones y área de resultados
        main_layout.addWidget(self.derivative_button)
        main_layout.addWidget(self.integral_button)
        main_layout.addWidget(QLabel("Resultado:"))
        main_layout.addWidget(self.result_area)

        self.setLayout(main_layout)

    def calculate_derivative(self):
        """Calcula la derivada de la expresión introducida."""
        try:
            expr = self.expression_input.text().strip()
            if not expr:
                raise ValueError("La expresión no puede estar vacía.")

            # Convertir la expresión a una forma simbólica
            sym_expr = sp.sympify(expr)

            # Calcular la derivada con respecto a 'x'
            derivative = sp.diff(sym_expr, sp.symbols('x'))

            # Mostrar el resultado
            self.result_area.setText(f"Derivada: {derivative}")
        except Exception as e:
            self.result_area.setText(f"Error al calcular la derivada: {e}")

    def calculate_integral(self):
        """Calcula la integral de la expresión introducida."""
        try:
            expr = self.expression_input.text().strip()
            if not expr:
                raise ValueError("La expresión no puede estar vacía.")

            # Convertir la expresión a una forma simbólica
            sym_expr = sp.sympify(expr)

            # Calcular la integral indefinida con respecto a 'x'
            integral = sp.integrate(sym_expr, sp.symbols('x'))

            # Mostrar el resultado
            self.result_area.setText(f"Integral: {integral}")
        except Exception as e:
            self.result_area.setText(f"Error al calcular la integral: {e}")

def get_calculator():
    return DerivativeIntegralCalculator()


