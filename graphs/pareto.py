#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Pareto"
GRAPH_SHORTCUT = "Ctrl+Y"

class ParetoChart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Pareto")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.data_input = QLineEdit()
        main_layout.addWidget(QLabel("Ingrese los datos en formato 'categoría,valor' separados por ';':"))
        main_layout.addWidget(self.data_input)

        plot_button = QPushButton("Graficar Pareto")
        plot_button.clicked.connect(self.plot_pareto_chart)
        main_layout.addWidget(plot_button)

        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_pareto_chart(self):
        try:
            text = self.data_input.text()
            categories, values = self.parse_data(text)

            self.plot(categories, values)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_data(self, text):
        """Convierte la entrada en listas de categorías y valores"""
        items = text.split(";")
        data = []
        for item in items:
            try:
                category, value = item.strip().split(",")
                data.append((category.strip(), float(value)))
            except ValueError:
                raise ValueError(f"Formato incorrecto en: {item}")

        data.sort(key=lambda x: x[1], reverse=True)
        categories, values = zip(*data)
        return list(categories), list(values)

    def plot(self, categories, values):
        """Dibuja el gráfico de Pareto"""
        self.canvas.figure.clear()
        ax1 = self.canvas.figure.add_subplot(111)

        cumulative = np.cumsum(values) / sum(values) * 100

        ax1.bar(categories, values, color="skyblue", label="Frecuencia", alpha=0.7)
        ax1.set_ylabel("Frecuencia")
        ax1.set_xticklabels(categories, rotation=45, ha="right")

        ax2 = ax1.twinx()
        ax2.plot(categories, cumulative, color="red", marker="o", linestyle="-", linewidth=2, label="Acumulado (%)")
        ax2.set_ylabel("Porcentaje Acumulado")
        ax2.set_ylim(0, 110)

        for i, txt in enumerate(cumulative):
            ax2.text(i, txt + 2, f"{txt:.1f}%", ha="center", fontsize=9)

        ax1.set_title("Gráfico de Pareto")
        ax1.grid(axis="y", linestyle="--", alpha=0.6)

        ax1.legend(loc="upper left")
        ax2.legend(loc="upper right")
        self.canvas.draw()

def get_graph():
    return ParetoChart()
