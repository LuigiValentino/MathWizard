#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import math

CALCULATOR_NAME = "Calculadora de Ángulos"
CALCULATOR_SHORTCUT = "Ctrl+B"

class AngleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Ángulos")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada de ángulo
        self.angle_input = QLineEdit()
        self.angle_input.setAlignment(Qt.AlignRight)
        main_layout.addWidget(QLabel("Ingrese el ángulo:"))
        main_layout.addWidget(self.angle_input)

        # ComboBox para seleccionar la unidad de entrada (Grados o Radianes)
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Grados", "Radianes"])
        main_layout.addWidget(QLabel("Selecciona la unidad del ángulo:"))
        main_layout.addWidget(self.unit_combo)

        # Botón para convertir el ángulo
        self.convert_button = QPushButton("Convertir Ángulo")
        self.convert_button.clicked.connect(self.convert_angle)
        main_layout.addWidget(self.convert_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        # Botones para calcular funciones trigonométricas
        self.sine_button = QPushButton("Seno")
        self.sine_button.clicked.connect(self.calculate_sine)
        main_layout.addWidget(self.sine_button)

        self.cosine_button = QPushButton("Coseno")
        self.cosine_button.clicked.connect(self.calculate_cosine)
        main_layout.addWidget(self.cosine_button)

        self.tangent_button = QPushButton("Tangente")
        self.tangent_button.clicked.connect(self.calculate_tangent)
        main_layout.addWidget(self.tangent_button)

        self.setLayout(main_layout)

    def convert_angle(self):
        """Convierte entre grados y radianes."""
        try:
            angle = float(self.angle_input.text())
            unit = self.unit_combo.currentText()

            if unit == "Grados":
                # Convertir de grados a radianes
                result = math.radians(angle)
                self.result_label.setText(f"Resultado: {result:.4f} radianes")

            elif unit == "Radianes":
                # Convertir de radianes a grados
                result = math.degrees(angle)
                self.result_label.setText(f"Resultado: {result:.4f} grados")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico válido.")
            self.result_label.setText("Resultado: ")

    def calculate_sine(self):
        """Calcula el seno del ángulo ingresado."""
        try:
            angle = float(self.angle_input.text())
            unit = self.unit_combo.currentText()

            if unit == "Grados":
                angle = math.radians(angle)  # Convertir a radianes
            result = math.sin(angle)
            self.result_label.setText(f"Seno: {result:.4f}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico válido.")
            self.result_label.setText("Resultado: ")

    def calculate_cosine(self):
        """Calcula el coseno del ángulo ingresado."""
        try:
            angle = float(self.angle_input.text())
            unit = self.unit_combo.currentText()

            if unit == "Grados":
                angle = math.radians(angle)  # Convertir a radianes
            result = math.cos(angle)
            self.result_label.setText(f"Coseno: {result:.4f}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico válido.")
            self.result_label.setText("Resultado: ")

    def calculate_tangent(self):
        """Calcula la tangente del ángulo ingresado."""
        try:
            angle = float(self.angle_input.text())
            unit = self.unit_combo.currentText()

            if unit == "Grados":
                angle = math.radians(angle)  # Convertir a radianes
            result = math.tan(angle)
            self.result_label.setText(f"Tangente: {result:.4f}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico válido.")
            self.result_label.setText("Resultado: ")

def get_calculator():
    return AngleCalculator()
