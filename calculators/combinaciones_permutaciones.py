#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
import math

CALCULATOR_NAME = "Combinaciones y Permutaciones"
CALCULATOR_SHORTCUT = "Ctrl+D"

class CombinationsPermutationsCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Combinaciones y Permutaciones")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.n_input = QLineEdit()
        self.r_input = QLineEdit()
        self.result_area = QTextEdit()

        main_layout.addWidget(QLabel("Valor de n:"))
        main_layout.addWidget(self.n_input)
        main_layout.addWidget(QLabel("Valor de r:"))
        main_layout.addWidget(self.r_input)

        self.combination_button = QPushButton("Calcular Combinaciones")
        self.permutation_button = QPushButton("Calcular Permutaciones")

        self.combination_button.clicked.connect(self.calculate_combinations)
        self.permutation_button.clicked.connect(self.calculate_permutations)

        main_layout.addWidget(self.combination_button)
        main_layout.addWidget(self.permutation_button)
        main_layout.addWidget(QLabel("Resultado:"))
        main_layout.addWidget(self.result_area)

        self.setLayout(main_layout)

    def calculate_combinations(self):
        try:
            n = self.n_input.text().strip()
            r = self.r_input.text().strip()

            if not n or not r:
                self.result_area.setText("Por favor, complete ambos campos.")
                return

            n = int(n)
            r = int(r)

            if n < 0 or r < 0:
                self.result_area.setText("Los valores de n y r deben ser números enteros no negativos.")
                return

            if r > n:
                self.result_area.setText("El valor de r no puede ser mayor que el valor de n.")
                return

            result = math.comb(n, r)
            self.result_area.setText(f"Combinaciones (nCr): {result}")
        except ValueError:
            self.result_area.setText("Por favor, ingrese valores numéricos válidos para n y r.")
        except Exception as e:
            self.result_area.setText(f"Error al calcular combinaciones: {e}")

    def calculate_permutations(self):
        try:
            n = self.n_input.text().strip()
            r = self.r_input.text().strip()

            if not n or not r:
                self.result_area.setText("Por favor, complete ambos campos.")
                return

            n = int(n)
            r = int(r)

            if n < 0 or r < 0:
                self.result_area.setText("Los valores de n y r deben ser números enteros no negativos.")
                return

            if r > n:
                self.result_area.setText("El valor de r no puede ser mayor que el valor de n.")
                return

            result = math.perm(n, r)
            self.result_area.setText(f"Permutaciones (nPr): {result}")
        except ValueError:
            self.result_area.setText("Por favor, ingrese valores numéricos válidos para n y r.")
        except Exception as e:
            self.result_area.setText(f"Error al calcular permutaciones: {e}")

def get_calculator():
    return CombinationsPermutationsCalculator()
