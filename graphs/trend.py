#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QFormLayout, QHBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from matplotlib.lines import Line2D

GRAPH_NAME = "Gráfico de Línea de Tendencia"
GRAPH_SHORTCUT = "Ctrl+1"

class TrendlineChart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Línea de Tendencia")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.names_input = QLineEdit()
        form_layout.addRow("Nombres de las líneas (separados por coma):", self.names_input)

        self.data_input = QLineEdit()
        form_layout.addRow("Datos de las líneas (cada grupo separado por coma y con puntos separados por espacio):", self.data_input)

        self.colors = []
        self.color_buttons = []

        main_layout.addLayout(form_layout)

        plot_button = QPushButton("Graficar Línea de Tendencia")
        plot_button.clicked.connect(self.plot_trendline_chart)
        main_layout.addWidget(plot_button)

        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_trendline_chart(self):
        try:
            
            names = self.names_input.text().split(',')
            data_text = self.data_input.text().split(',')

            if len(names) != len(data_text):
                raise ValueError("El número de nombres debe coincidir con el número de conjuntos de datos.")

            data = []
            for group in data_text:
                points = np.array([float(x) for x in group.strip().split()])
                data.append(points)

            
            colors = [QColorDialog.getColor().name() for _ in range(len(data))]
            if None in colors:
                raise ValueError("Es necesario elegir un color para cada línea.")

            
            self.plot(names, data, colors)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot(self, names, data, colors):
        """Dibuja el gráfico de líneas de tendencia con los colores y nombres"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

    
        for i, (name, points) in enumerate(zip(names, data)):
            x = np.arange(len(points))
            ax.plot(x, points, label=name, color=colors[i], lw=2)  

        ax.set_title("Gráfico de Línea de Tendencia")
        ax.set_xlabel("Índice")
        ax.set_ylabel("Valor")
        ax.legend()
        ax.grid(True)

        self.canvas.draw()

def get_graph():
    return TrendlineChart()
