#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import math

CALCULATOR_NAME = "Calculadora"
CALCULATOR_SHORTCUT = "Ctrl+A"

class BasicCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(CALCULATOR_NAME)
        self.init_ui()

    def init_ui(self):
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        self.display.setStyleSheet("font-size: 16px; padding: 4px;")
        main_layout.addWidget(self.display)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(3)

        buttons = [
            ("7", self.button_clicked), ("8", self.button_clicked), ("9", self.button_clicked), ("/", self.button_clicked),
            ("4", self.button_clicked), ("5", self.button_clicked), ("6", self.button_clicked), ("*", self.button_clicked),
            ("1", self.button_clicked), ("2", self.button_clicked), ("3", self.button_clicked), ("-", self.button_clicked),
            ("0", self.button_clicked), (".", self.button_clicked), ("C", self.clear_display), ("+", self.button_clicked),
            ("sin", self.button_clicked), ("cos", self.button_clicked), ("tan", self.button_clicked), ("√", self.sqrt_clicked),
            ("log", self.log_clicked), ("ln", self.ln_clicked), ("π", self.pi_clicked), ("exp", self.exp_clicked),
            ("^", self.power_clicked), ("!", self.factorial_clicked), ("round", self.round_clicked), ("deg/rad", self.deg_rad_clicked),
            ("%", self.percent_clicked), ("±", self.change_sign_clicked), ("mem", self.memory_clicked),
            ("←", self.backspace_clicked) 
        ]

        button_size = 38 

        for index, (text, slot) in enumerate(buttons):
            row, col = divmod(index, 4)
            button = QPushButton(text)
            button.setFixedSize(button_size, button_size)
            button.setStyleSheet("font-size: 14px;")
            button.clicked.connect(lambda checked, t=text, s=slot: s(t))
            grid_layout.addWidget(button, row, col)


        equal_button = QPushButton("=")
        equal_button.setFixedHeight(button_size)
        equal_button.setStyleSheet("font-size: 14px; font-weight: bold;")
        equal_button.clicked.connect(self.calculate_result)
        grid_layout.addWidget(equal_button, 4, 0, 1, 4)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)
        

        self.setMinimumSize(self.sizeHint())
        self.adjustSize()  

        self.memory = None

    def button_clicked(self, value):
        self.display.setText(self.display.text() + value)

    def clear_display(self, _=None):
        self.display.clear()

    def calculate_result(self, _=None):
        try:
            expression = self.display.text()
            result = eval(expression, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt,
                                                              "log": math.log10, "ln": math.log, "exp": math.exp, "pi": math.pi, 
                                                              "pow": math.pow, "round": round, "factorial": math.factorial})
            self.display.setText(str(result))
        except Exception:
            QMessageBox.warning(self, "Error", "Expresión inválida")
            self.display.clear()

    def sqrt_clicked(self, _=None):
        try:
            value = float(self.display.text())
            result = math.sqrt(value)
            self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def log_clicked(self, _=None):
        try:
            value = float(self.display.text())
            result = math.log10(value)
            self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def ln_clicked(self, _=None):
        try:
            value = float(self.display.text())
            result = math.log(value)
            self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def pi_clicked(self, _=None):
        self.display.setText(str(math.pi))

    def exp_clicked(self, _=None):
        try:
            value = float(self.display.text())
            result = math.exp(value)
            self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def power_clicked(self, _=None):
        try:
            base, exponent = self.display.text().split("^")
            result = math.pow(float(base), float(exponent))
            self.display.setText(str(result))
        except Exception:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def factorial_clicked(self, _=None):
        try:
            value = int(self.display.text())
            if value < 0:
                raise ValueError("El valor no puede ser negativo")
            result = math.factorial(value)
            self.display.setText(str(result))
        except Exception:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def round_clicked(self, _=None):
        try:
            value = float(self.display.text())
            result = round(value, 2) 
            self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def deg_rad_clicked(self, _=None):
        try:
            value = float(self.display.text())
            if "deg" in self.display.text():
                result = math.radians(value)
                self.display.setText(str(result))
            else:
                result = math.degrees(value)
                self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def percent_clicked(self, _=None):
        try:
            value = float(self.display.text()) / 100
            self.display.setText(str(value))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def change_sign_clicked(self, _=None):
        try:
            value = float(self.display.text())
            result = -value
            self.display.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Operación inválida")
            self.display.clear()

    def memory_clicked(self, _=None):
        if self.memory is None:
            self.memory = float(self.display.text())
            self.display.clear()
        else:
            self.display.setText(str(self.memory))


    def backspace_clicked(self, _=None):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

def get_calculator():
    return BasicCalculator()
