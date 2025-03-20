#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Área"
GRAPH_SHORTCUT = "Ctrl+O"

class AreaChartCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Área")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada de datos de los conjuntos de valores
        self.data_input = QLineEdit()
        self.names_input = QLineEdit()

        main_layout.addWidget(QLabel("Datos de los conjuntos (separados por |, valores separados por coma):"))
        main_layout.addWidget(self.data_input)

        main_layout.addWidget(QLabel("Nombres de los conjuntos (separados por |):"))
        main_layout.addWidget(self.names_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Área")
        plot_button.clicked.connect(self.plot_area)
        main_layout.addWidget(plot_button)

        # Lienzo para el gráfico
        self.area_canvas = FigureCanvas(plt.figure(figsize=(8, 6)))
        main_layout.addWidget(self.area_canvas)

        self.setLayout(main_layout)

    def plot_area(self):
        try:
            data_text = self.data_input.text()
            names_text = self.names_input.text()

            # Convertir los datos ingresados en listas de valores
            datasets = self.parse_data(data_text)
            names = self.parse_names(names_text)

            if len(datasets) != len(names):
                raise ValueError("La cantidad de conjuntos de datos no coincide con la cantidad de nombres.")

            # Elegir colores
            colors = self.ask_for_colors(len(datasets))

            # Generar gráfico
            self.plot(datasets, names, colors)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_data(self, text):
        """Convierte el texto en listas de datos numéricos."""
        groups = text.split("|")
        parsed_data = []
        for group in groups:
            values = [float(v.strip()) for v in group.split(",")]
            parsed_data.append(values)
        return parsed_data

    def parse_names(self, text):
        """Convierte el texto en una lista de nombres."""
        return [name.strip() for name in text.split("|")]

    def ask_for_colors(self, num_colors):
        """Solicita colores para cada conjunto de datos."""
        colors = []
        for i in range(num_colors):
            color = QColorDialog.getColor()
            if color.isValid():
                colors.append(color.name())  # Formato hexadecimal
            else:
                colors.append("#000000")  # Negro por defecto si cancelan
        return colors

    def plot(self, datasets, names, colors):
        """Dibuja el gráfico de área"""
        self.area_canvas.figure.clear()
        ax = self.area_canvas.figure.add_subplot(111)

        # Generar X (secuencias automáticas desde 1)
        x_values = list(range(1, len(datasets[0]) + 1))

        # Graficar cada conjunto con su color
        for i, (data, name) in enumerate(zip(datasets, names)):
            ax.fill_between(x_values, data, color=colors[i], alpha=0.6, label=name)

        # Configuración del gráfico
        ax.set_title("Gráfico de Área", fontsize=18)
        ax.set_xlabel("Índice", fontsize=12)
        ax.set_ylabel("Valores", fontsize=12)
        ax.legend()
        ax.grid(True)

        # Ajustar diseño y dibujar
        self.area_canvas.figure.tight_layout()
        self.area_canvas.draw()

def get_graph():
    return AreaChartCalculator()
