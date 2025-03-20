#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import math

# Variables globales para que el main pueda detectar este módulo
CALCULATOR_NAME = "Calculadora de Áreas"
CALCULATOR_SHORTCUT = "Ctrl+C"

class AreaCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(CALCULATOR_NAME)
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # ComboBox para seleccionar la figura
        self.figure_combo = QComboBox()
        self.figure_combo.addItems(["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo", "Trapecio", "Polígono Regular"])
        self.figure_combo.currentTextChanged.connect(self.update_inputs)
        main_layout.addWidget(self.figure_combo)

        # Layout para los campos de entrada
        self.input_layout = QGridLayout()
        self.input_layout.setSpacing(5)
        main_layout.addLayout(self.input_layout)

        # ComboBox para seleccionar la unidad de medida
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["cm", "m", "km", "mm"])
        main_layout.addWidget(QLabel("Selecciona la unidad:"))
        main_layout.addWidget(self.unit_combo)

        # Botón para calcular el área
        self.calculate_button = QPushButton("Calcular Área")
        self.calculate_button.clicked.connect(self.calculate_area)
        main_layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Área: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)
        self.update_inputs()  # Inicializa los campos de entrada

    def update_inputs(self):
        """Actualiza los campos de entrada dependiendo de la figura seleccionada."""
        # Limpiar los campos de entrada previos
        for i in reversed(range(self.input_layout.count())):
            widget = self.input_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Obtener la figura seleccionada
        selected_figure = self.figure_combo.currentText()

        self.input_fields = []  # Limpiar los campos de entrada

        if selected_figure == "Rectángulo" or selected_figure == "Paralelogramo":
            self.input_fields.append(self.create_input_field("Base:"))
            self.input_fields.append(self.create_input_field("Altura:"))
        elif selected_figure == "Cuadrado":
            self.input_fields.append(self.create_input_field("Lado:"))
        elif selected_figure == "Triángulo":
            self.input_fields.append(self.create_input_field("Base:"))
            self.input_fields.append(self.create_input_field("Altura:"))
        elif selected_figure == "Círculo":
            self.input_fields.append(self.create_input_field("Radio:"))
        elif selected_figure == "Trapecio":
            self.input_fields.append(self.create_input_field("Base Mayor:"))
            self.input_fields.append(self.create_input_field("Base Menor:"))
            self.input_fields.append(self.create_input_field("Altura:"))
        elif selected_figure == "Polígono Regular":
            self.input_fields.append(self.create_input_field("Perímetro:"))
            self.input_fields.append(self.create_input_field("Apotema:"))

    def create_input_field(self, label_text):
        """Crea un campo de entrada con su respectiva etiqueta."""
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setAlignment(Qt.AlignRight)
        self.input_layout.addWidget(label)
        self.input_layout.addWidget(input_field)
        return input_field
        
    def calculate_area(self):
        """Calcula el área según la figura seleccionada."""
        try:
            # Obtener la figura seleccionada
            selected_figure = self.figure_combo.currentText()

            # Leer los valores de entrada directamente desde los campos
            inputs = [field.text().strip() for field in self.input_fields]

            # Eliminar valores vacíos
            inputs = [i for i in inputs if i != ""]

            if not inputs:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
                return

            # Convertir los valores de entrada a float
            try:
                inputs = [float(i) for i in inputs]
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores numéricos válidos.")
                return

            # Obtener la unidad seleccionada
            unit = self.unit_combo.currentText()

            # Cálculos de áreas
            if selected_figure == "Rectángulo":
                if len(inputs) < 2:
                    QMessageBox.warning(self, "Error", "Faltan valores. Se requieren base y altura.")
                    return
                base, altura = inputs
                area = base * altura
            elif selected_figure == "Cuadrado":
                if len(inputs) < 1:
                    QMessageBox.warning(self, "Error", "Falta el valor del lado.")
                    return
                lado = inputs[0]
                area = lado ** 2
            elif selected_figure == "Triángulo":
                if len(inputs) < 2:
                    QMessageBox.warning(self, "Error", "Faltan valores. Se requieren base y altura.")
                    return
                base, altura = inputs
                area = (base * altura) / 2
            elif selected_figure == "Círculo":
                if len(inputs) < 1:
                    QMessageBox.warning(self, "Error", "Falta el valor del radio.")
                    return
                radio = inputs[0]
                area = math.pi * (radio ** 2)
            elif selected_figure == "Paralelogramo":
                if len(inputs) < 2:
                    QMessageBox.warning(self, "Error", "Faltan valores. Se requieren base y altura.")
                    return
                base, altura = inputs
                area = base * altura
            elif selected_figure == "Trapecio":
                if len(inputs) < 3:
                    QMessageBox.warning(self, "Error", "Faltan valores. Se requieren base mayor, base menor y altura.")
                    return
                base_mayor, base_menor, altura = inputs
                area = (base_mayor + base_menor) * altura / 2
            elif selected_figure == "Polígono Regular":
                if len(inputs) < 2:
                    QMessageBox.warning(self, "Error", "Faltan valores. Se requieren perímetro y apotema.")
                    return
                perimetro, apotema = inputs
                area = (perimetro * apotema) / 2

            # Mostrar el resultado
            self.result_label.setText(f"Área: {area:.2f} {unit}²")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese valores numéricos válidos.")
            self.result_label.setText("Área: ")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un error: {str(e)}")
            self.result_label.setText("Área: ")

def get_calculator():
    return AreaCalculator()
