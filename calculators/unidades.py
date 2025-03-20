#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
CALCULATOR_NAME = "Calculadora de Conversiones de Unidades"
CALCULATOR_SHORTCUT = "Ctrl+N"

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Conversiones de Unidades")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # ComboBox para seleccionar la categoría de conversión
        self.category_combo = QComboBox()
        self.category_combo.addItems([
            "Longitud", "Masa", "Volumen", "Temperatura", "Área", "Velocidad"
        ])
        self.category_combo.currentTextChanged.connect(self.update_inputs)
        main_layout.addWidget(QLabel("Selecciona una categoría de conversión:"))
        main_layout.addWidget(self.category_combo)

        # Layout para los campos de entrada (valor, unidad de origen, unidad de destino)
        self.input_layout = QGridLayout()
        self.input_layout.setSpacing(5)
        main_layout.addLayout(self.input_layout)

        # Botón para realizar la conversión
        self.convert_button = QPushButton("Convertir")
        self.convert_button.clicked.connect(self.convert_units)
        main_layout.addWidget(self.convert_button)

        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("Resultado: ")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)
        self.update_inputs()  # Inicializa los campos de entrada

    def update_inputs(self):
        """Actualiza los campos de entrada dependiendo de la categoría seleccionada."""
        # Limpiar los campos de entrada previos
        for i in reversed(range(self.input_layout.count())):
            widget = self.input_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        selected_category = self.category_combo.currentText()

        self.input_fields = []

        if selected_category == "Longitud":
            units = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
        elif selected_category == "Masa":
            units = ["mg", "g", "kg", "t", "lb", "oz"]
        elif selected_category == "Volumen":
            units = ["ml", "L", "cm³", "m³", "gal", "pt", "cup"]
        elif selected_category == "Temperatura":
            units = ["°C", "°F", "K"]
        elif selected_category == "Área":
            units = ["cm²", "m²", "km²", "ft²", "yd²", "ac", "ha"]
        elif selected_category == "Velocidad":
            units = ["m/s", "km/h", "mph", "kn"]

        # Crear los campos de entrada
        self.value_input = QLineEdit()
        self.value_input.setAlignment(Qt.AlignRight)
        self.input_layout.addWidget(QLabel("Valor:"), 0, 0)
        self.input_layout.addWidget(self.value_input, 0, 1)

        # ComboBox para seleccionar la unidad de origen
        self.from_unit_combo = QComboBox()
        self.from_unit_combo.addItems(units)
        self.input_layout.addWidget(QLabel("De:"), 1, 0)
        self.input_layout.addWidget(self.from_unit_combo, 1, 1)

        # ComboBox para seleccionar la unidad de destino
        self.to_unit_combo = QComboBox()
        self.to_unit_combo.addItems(units)
        self.input_layout.addWidget(QLabel("Convertir a:"), 2, 0)
        self.input_layout.addWidget(self.to_unit_combo, 2, 1)

    def convert_units(self):
        """Convierte las unidades y muestra el resultado."""
        try:
            # Obtener la categoría seleccionada y el valor de entrada
            selected_category = self.category_combo.currentText()
            value = float(self.value_input.text())
            from_unit = self.from_unit_combo.currentText()
            to_unit = self.to_unit_combo.currentText()

            # Conversión según la categoría seleccionada
            if selected_category == "Longitud":
                result = self.convert_length(value, from_unit, to_unit)
            elif selected_category == "Masa":
                result = self.convert_mass(value, from_unit, to_unit)
            elif selected_category == "Volumen":
                result = self.convert_volume(value, from_unit, to_unit)
            elif selected_category == "Temperatura":
                result = self.convert_temperature(value, from_unit, to_unit)
            elif selected_category == "Área":
                result = self.convert_area(value, from_unit, to_unit)
            elif selected_category == "Velocidad":
                result = self.convert_speed(value, from_unit, to_unit)

            # Mostrar el resultado
            self.result_label.setText(f"Resultado: {result}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico válido.")
            self.result_label.setText("Resultado: ")

    def convert_length(self, value, from_unit, to_unit):
        """Convierte la longitud entre diferentes unidades."""
        length_units = {
            "mm": 1, "cm": 10, "m": 1000, "km": 1000000, "in": 25.4, "ft": 304.8, "yd": 914.4, "mi": 1609344
        }
        value_in_mm = value * length_units[from_unit]
        result = value_in_mm / length_units[to_unit]
        return result

    def convert_mass(self, value, from_unit, to_unit):
        """Convierte la masa entre diferentes unidades."""
        mass_units = {
            "mg": 1, "g": 1000, "kg": 1000000, "t": 1000000000, "lb": 453592.37, "oz": 28349.5231
        }
        value_in_mg = value * mass_units[from_unit]
        result = value_in_mg / mass_units[to_unit]
        return result

    def convert_volume(self, value, from_unit, to_unit):
        """Convierte el volumen entre diferentes unidades."""
        volume_units = {
            "ml": 1, "L": 1000, "cm³": 1, "m³": 1000000, "gal": 3785.41, "pt": 473.176, "cup": 240
        }
        value_in_ml = value * volume_units[from_unit]
        result = value_in_ml / volume_units[to_unit]
        return result

    def convert_temperature(self, value, from_unit, to_unit):
        """Convierte entre diferentes escalas de temperatura."""
        if from_unit == "°C":
            if to_unit == "°F":
                return (value * 9/5) + 32
            elif to_unit == "K":
                return value + 273.15
        elif from_unit == "°F":
            if to_unit == "°C":
                return (value - 32) * 5/9
            elif to_unit == "K":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "K":
            if to_unit == "°C":
                return value - 273.15
            elif to_unit == "°F":
                return (value - 273.15) * 9/5 + 32
        return value

    def convert_area(self, value, from_unit, to_unit):
        """Convierte entre diferentes unidades de área."""
        area_units = {
            "cm²": 1, "m²": 10000, "km²": 100000000, "ft²": 929.0304, "yd²": 8361.27, "ac": 40468564, "ha": 10000
        }
        value_in_cm2 = value * area_units[from_unit]
        result = value_in_cm2 / area_units[to_unit]
        return result

    def convert_speed(self, value, from_unit, to_unit):
        """Convierte entre diferentes unidades de velocidad."""
        speed_units = {
            "m/s": 1, "km/h": 3.6, "mph": 2.23694, "kn": 1.94384
        }
        value_in_ms = value * speed_units[from_unit]
        result = value_in_ms / speed_units[to_unit]
        return result

def get_calculator():
    return UnitConverter()
