#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
import math

CALCULATOR_NAME = "Ecuaciones Cuadráticas"
CALCULATOR_SHORTCUT = "Ctrl+F"

class QuadraticEquationCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Ecuaciones Cuadráticas")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.a_input = QLineEdit()
        self.b_input = QLineEdit()
        self.c_input = QLineEdit()
        self.result_area = QTextEdit()

        main_layout.addWidget(QLabel("Coeficiente a:"))
        main_layout.addWidget(self.a_input)
        main_layout.addWidget(QLabel("Coeficiente b:"))
        main_layout.addWidget(self.b_input)
        main_layout.addWidget(QLabel("Coeficiente c:"))
        main_layout.addWidget(self.c_input)

        self.calculate_button = QPushButton("Calcular Raíces")
        self.calculate_button.clicked.connect(self.calculate_roots)

        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(QLabel("Resultado:"))
        main_layout.addWidget(self.result_area)

        self.setLayout(main_layout)

    def calculate_roots(self):
        try:
            # Obtener los coeficientes de los campos de entrada
            a = self.a_input.text().strip()
            b = self.b_input.text().strip()
            c = self.c_input.text().strip()

            # Verificar que los campos no estén vacíos
            if not a or not b or not c:
                self.result_area.setText("Por favor, complete todos los campos.")
                return

            # Convertir las entradas a números
            a = float(a)
            b = float(b)
            c = float(c)

            # Calcular el discriminante
            discriminant = b ** 2 - 4 * a * c

            # Calcular las raíces dependiendo del discriminante
            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                self.result_area.setText(f"Raíces Reales: {root1} y {root2}")
            elif discriminant == 0:
                root = -b / (2 * a)
                self.result_area.setText(f"Raíz Doble: {root}")
            else:
                self.result_area.setText("La ecuación no tiene raíces reales.")
        except ValueError:
            # Capturar error si el valor no es numérico
            self.result_area.setText("Por favor, ingrese valores numéricos válidos para a, b y c.")
        except Exception as e:
            # Capturar cualquier otro error no esperado
            self.result_area.setText(f"Error al calcular las raíces: {e}")

def get_calculator():
    return QuadraticEquationCalculator()
