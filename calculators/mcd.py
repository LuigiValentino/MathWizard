#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import math

# Variables globales para que el main pueda detectar este módulo
CALCULATOR_NAME = "Calculadora de MCD, MCM y Estadísticas"
CALCULATOR_SHORTCUT = "Ctrl+J"

class StatsCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(CALCULATOR_NAME)
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Campo de entrada para los números
        self.numbers_input = QLineEdit()
        self.numbers_input.setPlaceholderText("Introduce los números separados por comas (ej. 12, 15, 30)")
        main_layout.addWidget(self.numbers_input)

        # ComboBox para seleccionar la operación
        self.operation_combo = QComboBox()
        self.operation_combo.addItems(["MCD (Máximo Común Divisor)", "MCM (Mínimo Común Múltiplo)", "Media", "Mediana", "Desviación Estándar", "Varianza"])
        main_layout.addWidget(self.operation_combo)

        # Botón para calcular
        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate(self):
        try:
            # Obtener los números del campo de entrada
            numbers_str = self.numbers_input.text().strip()
            if not numbers_str:
                QMessageBox.warning(self, "Error", "Por favor, ingrese al menos un número.")
                return

            # Convertir la entrada en una lista de números
            numbers = [int(x) for x in numbers_str.split(',')]

            # Obtener la operación seleccionada
            operation = self.operation_combo.currentText()

            # Calcular según la operación seleccionada
            if operation == "MCD (Máximo Común Divisor)":
                result = self.calculate_mcd(numbers)
            elif operation == "MCM (Mínimo Común Múltiplo)":
                result = self.calculate_mcm(numbers)
            elif operation == "Media":
                result = self.calculate_mean(numbers)
            elif operation == "Mediana":
                result = self.calculate_median(numbers)
            elif operation == "Desviación Estándar":
                result = self.calculate_std_deviation(numbers)
            elif operation == "Varianza":
                result = self.calculate_variance(numbers)

            # Mostrar el resultado
            self.result_label.setText(f"Resultado: {result}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese solo números válidos.")
            self.result_label.setText("Resultado: ")

    def calculate_mcd(self, numbers):
        """Calcula el MCD (Máximo Común Divisor) de una lista de números."""
        def mcd(a, b):
            while b:
                a, b = b, a % b
            return a
        result = numbers[0]
        for num in numbers[1:]:
            result = mcd(result, num)
        return result

    def calculate_mcm(self, numbers):
        """Calcula el MCM (Mínimo Común Múltiplo) de una lista de números."""
        def mcm(a, b):
            return abs(a * b) // self.calculate_mcd([a, b])
        result = numbers[0]
        for num in numbers[1:]:
            result = mcm(result, num)
        return result

    def calculate_mean(self, numbers):
        """Calcula la media de los números."""
        return sum(numbers) / len(numbers)

    def calculate_median(self, numbers):
        """Calcula la mediana de los números."""
        numbers.sort()
        n = len(numbers)
        if n % 2 == 1:
            return numbers[n // 2]
        else:
            return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    def calculate_std_deviation(self, numbers):
        """Calcula la desviación estándar de los números."""
        mean = self.calculate_mean(numbers)
        variance = self.calculate_variance(numbers)
        return math.sqrt(variance)

    def calculate_variance(self, numbers):
        """Calcula la varianza de los números."""
        mean = self.calculate_mean(numbers)
        return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def get_calculator():
    return StatsCalculator()
