#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# El nombre y atajo de teclado de la calculadora
GRAPH_NAME = "Gráfico de Líneas Múltiples"
GRAPH_SHORTCUT = "Ctrl+W"

class MultipleLineGraphCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Líneas Múltiples")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada para las series de datos
        self.series_input = QLineEdit()
        main_layout.addWidget(QLabel("Valores de las series (X1,Y1),(X2,Y2),... :"))
        main_layout.addWidget(self.series_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Líneas Múltiples")
        plot_button.clicked.connect(self.plot_multiple_lines)
        main_layout.addWidget(plot_button)

        # Crear un lienzo para el gráfico
        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_multiple_lines(self):
        """Genera el gráfico de líneas múltiples."""
        try:
            # Limpiar y ajustar la entrada
            series_data = self.series_input.text().strip()
            series_data = series_data.replace("),(", ")-(")  # Asegurarse de que los datos estén correctamente separados
            series_data = series_data.strip('()')  # Eliminar los paréntesis externos

            # Separar las series individuales
            series_list = series_data.split(")-(")
            
            x_values_list = []
            y_values_list = []

            for series in series_list:
                # Limpiar posibles espacios y paréntesis sobrantes
                series = series.strip("()")

                # Separar las coordenadas X y Y
                series_values = series.split(',')
                x_values = list(map(float, series_values[0].split(';')))
                y_values = list(map(float, series_values[1].split(';')))
                x_values_list.append(x_values)
                y_values_list.append(y_values)

            self.plot_lines(x_values_list, y_values_list)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot_lines(self, x_values_list, y_values_list):
        """Dibuja múltiples líneas en el lienzo."""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

        # Graficar cada serie de datos
        for x_values, y_values in zip(x_values_list, y_values_list):
            ax.plot(x_values, y_values)

        ax.set_title("Gráfico de Líneas Múltiples")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.grid(True)
        self.canvas.draw()

def get_graph():
    return MultipleLineGraphCalculator()
