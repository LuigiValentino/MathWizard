#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Histograma"
GRAPH_SHORTCUT = "Ctrl+V"

class HistogramChartCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Histograma")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada de datos (números separados por coma)
        self.data_input = QLineEdit()
        main_layout.addWidget(QLabel("Datos (separados por coma):"))
        main_layout.addWidget(self.data_input)

        # Entrada opcional para número de bins
        self.bins_input = QLineEdit()
        self.bins_input.setPlaceholderText("Número de bins (opcional, default: 'auto')")
        main_layout.addWidget(QLabel("Número de bins (opcional):"))
        main_layout.addWidget(self.bins_input)

        # Botón para seleccionar color para las barras
        self.color_button = QPushButton("Seleccionar Color para el Histograma")
        self.color_button.clicked.connect(self.choose_color)
        main_layout.addWidget(self.color_button)
        self.selected_color = None

        # Botón para graficar el histograma
        plot_button = QPushButton("Graficar Histograma")
        plot_button.clicked.connect(self.plot_histogram)
        main_layout.addWidget(plot_button)

        # Lienzo para el gráfico
        self.hist_canvas = FigureCanvas(plt.figure(figsize=(8, 6)))
        main_layout.addWidget(self.hist_canvas)

        self.setLayout(main_layout)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color.name()
        else:
            self.selected_color = "#000000"  # Negro por defecto

    def plot_histogram(self):
        try:
            data_text = self.data_input.text().strip()
            if not data_text:
                raise ValueError("Ingrese los datos para el histograma.")
            data = [float(x.strip()) for x in data_text.split(",")]

            bins_text = self.bins_input.text().strip()
            bins = int(bins_text) if bins_text else "auto"

            # Usar el color seleccionado o un color por defecto
            bar_color = self.selected_color if self.selected_color is not None else "blue"

            # Limpiar el lienzo y graficar
            self.hist_canvas.figure.clear()
            ax = self.hist_canvas.figure.add_subplot(111)
            ax.hist(data, bins=bins, color=bar_color, edgecolor="black", alpha=0.7)
            ax.set_title("Histograma")
            ax.set_xlabel("Valores")
            ax.set_ylabel("Frecuencia")
            ax.grid(True)

            self.hist_canvas.draw()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

def get_graph():
    return HistogramChartCalculator()
