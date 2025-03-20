#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
import sympy as sp

CALCULATOR_NAME = "Sistema de Ecuaciones Lineales"
CALCULATOR_SHORTCUT = "Ctrl+H"

class LinearEquationsCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Sistema de Ecuaciones Lineales")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.equation_inputs = []  # Lista para guardar los campos de entrada de las ecuaciones
        self.result_area = QTextEdit()

        # Crear campos para ingresar ecuaciones
        self.create_equation_input()

        # Botón para calcular el sistema
        self.calculate_button = QPushButton("Calcular Solución")
        self.calculate_button.clicked.connect(self.calculate_solution)

        main_layout.addWidget(QLabel("Ecuaciones del sistema (Ejemplo: 2*x + 3*y = 5)"))
        for equation_input in self.equation_inputs:
            main_layout.addWidget(equation_input)

        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(QLabel("Resultado:"))
        main_layout.addWidget(self.result_area)

        self.setLayout(main_layout)

    def create_equation_input(self):
        """Crea un campo para ingresar una nueva ecuación."""
        equation_input = QLineEdit()
        equation_input.setPlaceholderText("Ecuación (Ejemplo: 2*x + 3*y = 5)")
        self.equation_inputs.append(equation_input)

    def calculate_solution(self):
        try:
            # Recoger las ecuaciones introducidas por el usuario
            equations = [eq.text() for eq in self.equation_inputs]
            if not all(equations):
                self.result_area.setText("Por favor, ingrese todas las ecuaciones.")
                return

            # Procesar las ecuaciones usando SymPy
            parsed_equations = []
            for eq in equations:
                parsed_equations.append(sp.sympify(eq.replace('=', '-')))  # Convertir las ecuaciones a la forma correcta

            # Resolver el sistema de ecuaciones
            variables = sp.symbols('x y z')  # Puedes agregar más variables si es necesario
            solution = sp.linsolve(parsed_equations, variables)

            if solution:
                self.result_area.setText(f"Solución: {solution}")
            else:
                self.result_area.setText("El sistema no tiene solución.")

        except Exception as e:
            self.result_area.setText(f"Error al calcular la solución: {e}")

def get_calculator():
    return LinearEquationsCalculator()
