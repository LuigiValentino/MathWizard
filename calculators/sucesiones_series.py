#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import sympy as sp

# Variables globales para que el main pueda detectar este módulo
CALCULATOR_NAME = "Calculadora de Sucesiones y Series"
CALCULATOR_SHORTCUT = "Ctrl+M"

class SequenceSeriesCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(CALCULATOR_NAME)
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Campo de entrada para los números de la sucesión
        self.sequence_input = QLineEdit()
        self.sequence_input.setPlaceholderText("Introduce los términos de la sucesión (ej. 1, 4, 7, 10)")
        main_layout.addWidget(self.sequence_input)

        # ComboBox para seleccionar el tipo de serie
        self.series_combo = QComboBox()
        self.series_combo.addItems(["Aritmética", "Geométrica"])
        main_layout.addWidget(self.series_combo)

        # Botón para calcular
        self.calculate_button = QPushButton("Calcular Sucesión/Serie")
        self.calculate_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate(self):
        try:
            # Obtener los términos de la sucesión
            sequence_str = self.sequence_input.text().strip()
            if not sequence_str:
                QMessageBox.warning(self, "Error", "Por favor, ingrese al menos un término.")
                return

            # Convertir la entrada en una lista de números
            terms = [int(x) for x in sequence_str.split(',')]

            # Obtener el tipo de serie seleccionada
            series_type = self.series_combo.currentText()

            # Calcular según el tipo de serie seleccionada
            if series_type == "Aritmética":
                result = self.calculate_arithmetic(terms)
            elif series_type == "Geométrica":
                result = self.calculate_geometric(terms)

            # Mostrar el resultado
            self.result_label.setText(f"Resultado: {result}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese solo números válidos.")
            self.result_label.setText("Resultado: ")

    def calculate_arithmetic(self, terms):
        """Calcula la sucesión aritmética, verifica la diferencia común."""
        if len(terms) < 2:
            return "Se requieren al menos 2 términos para calcular la sucesión aritmética."

        # Calcular la diferencia común
        difference = terms[1] - terms[0]

        # Verificar que la diferencia común es la misma en toda la secuencia
        for i in range(1, len(terms) - 1):
            if terms[i+1] - terms[i] != difference:
                return "Los términos no siguen una sucesión aritmética."

        # La fórmula de la suma de n términos de una sucesión aritmética
        n = len(terms)
        first_term = terms[0]
        last_term = terms[-1]
        sum_of_terms = (n * (first_term + last_term)) / 2

        return f"Suma de los primeros {n} términos: {sum_of_terms}"

    def calculate_geometric(self, terms):
        """Calcula la sucesión geométrica, verifica la razón común."""
        if len(terms) < 2:
            return "Se requieren al menos 2 términos para calcular la sucesión geométrica."

        # Calcular la razón común
        ratio = terms[1] / terms[0]

        # Verificar que la razón común es la misma en toda la secuencia
        for i in range(1, len(terms) - 1):
            if terms[i+1] / terms[i] != ratio:
                return "Los términos no siguen una sucesión geométrica."

        # Fórmula para la suma de los primeros n términos de una sucesión geométrica
        n = len(terms)
        first_term = terms[0]
        if ratio == 1:
            sum_of_terms = first_term * n
        else:
            sum_of_terms = first_term * (1 - ratio**n) / (1 - ratio)

        return f"Suma de los primeros {n} términos: {sum_of_terms}"

def get_calculator():
    return SequenceSeriesCalculator()
