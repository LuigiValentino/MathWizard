#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import math

CALCULATOR_NAME = "Calculadora de Raíz"
CALCULATOR_SHORTCUT = "Ctrl+L"

class RootCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Raíz")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada de número
        self.number_input = QLineEdit()
        self.number_input.setAlignment(Qt.AlignRight)
        main_layout.addWidget(QLabel("Ingrese el número:"))
        main_layout.addWidget(self.number_input)

        # ComboBox para seleccionar el tipo de raíz
        self.root_type_combo = QComboBox()
        self.root_type_combo.addItems(["Raíz Cuadrada", "Raíz Cúbica", "Raíz enésima"])
        main_layout.addWidget(QLabel("Selecciona el tipo de raíz:"))
        main_layout.addWidget(self.root_type_combo)

        # Entrada para el valor de "n" (solo para raíz enésima)
        self.n_input = QLineEdit()
        self.n_input.setAlignment(Qt.AlignRight)
        self.n_input.setPlaceholderText("Ingresa el valor de n (para raíz enésima)")
        self.n_input.setDisabled(True)  # Se habilita solo si se selecciona "Raíz enésima"
        main_layout.addWidget(self.n_input)

        # Botón para calcular la raíz
        self.calculate_button = QPushButton("Calcular Raíz")
        self.calculate_button.clicked.connect(self.calculate_root)
        main_layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        # Conectar la selección del tipo de raíz a la habilitación del campo "n"
        self.root_type_combo.currentTextChanged.connect(self.update_input_fields)

    def update_input_fields(self):
        """Habilita o deshabilita la entrada de 'n' según el tipo de raíz seleccionado."""
        if self.root_type_combo.currentText() == "Raíz enésima":
            self.n_input.setEnabled(True)
        else:
            self.n_input.setDisabled(True)
            self.n_input.clear()

    def calculate_root(self):
        """Calcula la raíz seleccionada (cuadrada, cúbica o enésima)."""
        try:
            # Obtener el número ingresado
            number = float(self.number_input.text())

            if number < 0 and self.root_type_combo.currentText() == "Raíz Cuadrada":
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

            # Obtener el tipo de raíz seleccionada
            root_type = self.root_type_combo.currentText()

            # Calcular según el tipo de raíz seleccionado
            if root_type == "Raíz Cuadrada":
                result = math.sqrt(number)
            elif root_type == "Raíz Cúbica":
                result = number ** (1/3)
            elif root_type == "Raíz enésima":
                n = float(self.n_input.text())
                if n == 0:
                    raise ValueError("El valor de n no puede ser cero.")
                result = number ** (1/n)

            # Mostrar el resultado
            self.result_label.setText(f"Resultado: {result:.4f}")

        except ValueError as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
            self.result_label.setText("Resultado: ")

def get_calculator():
    return RootCalculator()
