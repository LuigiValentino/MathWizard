#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Embudo"
GRAPH_SHORTCUT = "Ctrl+T"

class FunnelChart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Embudo")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada de datos
        self.data_input = QLineEdit()
        main_layout.addWidget(QLabel("Ingrese los datos en formato 'etapa,valor' separados por ';':"))
        main_layout.addWidget(self.data_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Embudo")
        plot_button.clicked.connect(self.plot_funnel_chart)
        main_layout.addWidget(plot_button)

        # Crear el área del gráfico
        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_funnel_chart(self):
        try:
            # Obtener datos
            text = self.data_input.text()
            stages, values = self.parse_data(text)

            # Graficar
            self.plot(stages, values)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_data(self, text):
        """Convierte la entrada en listas de etapas y valores"""
        items = text.split(";")
        data = []
        for item in items:
            try:
                stage, value = item.strip().split(",")
                data.append((stage.strip(), float(value)))
            except ValueError:
                raise ValueError(f"Formato incorrecto en: {item}")

        # Ordenar las etapas de mayor a menor valor
        data.sort(key=lambda x: x[1], reverse=True)
        stages, values = zip(*data)
        return list(stages), list(values)

    def plot(self, stages, values):
        """Dibuja el gráfico de Embudo"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

        # Crear un degradado de colores del más oscuro (inicio) al más claro (fin)
        colors = plt.cm.Blues_r(np.linspace(0.3, 1, len(values)))

        # Ancho máximo del embudo
        max_width = max(values)

        # Dibujar cada segmento del embudo
        for i, (stage, value) in enumerate(zip(stages, values)):
            ax.barh(stage, value, color=colors[i], edgecolor="black", height=0.7)

        ax.set_xlabel("Cantidad")
        ax.set_title("Gráfico de Embudo")
        ax.invert_yaxis()  # Invertir el eje Y para que la etapa más grande esté arriba
        ax.grid(axis="x", linestyle="--", alpha=0.6)

        self.canvas.draw()

def get_graph():
    return FunnelChart()
