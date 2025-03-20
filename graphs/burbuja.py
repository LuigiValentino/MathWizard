#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Burbujas"
GRAPH_SHORTCUT = "Ctrl+P"

class BubbleChart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Burbujas")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada de datos
        self.data_input = QLineEdit()
        main_layout.addWidget(QLabel("Ingrese los puntos en formato (x,y,tamaño,nombre grupo) separados por ';':"))
        main_layout.addWidget(self.data_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Burbuja")
        plot_button.clicked.connect(self.plot_bubble_chart)
        main_layout.addWidget(plot_button)

        # Crear el área del gráfico
        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_bubble_chart(self):
        try:
            # Obtener datos
            text = self.data_input.text()
            groups = self.parse_groups(text)

            # Obtener colores para cada grupo
            unique_groups = list(set(group for _, _, _, group in groups))
            colors = self.ask_for_colors(len(unique_groups))
            color_map = {group: colors[i] for i, group in enumerate(unique_groups)}

            # Graficar
            self.plot(groups, color_map)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_groups(self, text):
        """Convierte la entrada en una lista de puntos con tamaño y nombre de grupo"""
        points = text.split(";")
        parsed_data = []
        for point in points:
            try:
                x, y, size, group = point.strip().replace("(", "").replace(")", "").split(",")
                parsed_data.append((float(x), float(y), float(size), group.strip()))
            except ValueError:
                raise ValueError(f"Formato incorrecto en: {point}")
        return parsed_data

    def ask_for_colors(self, num_colors):
        """Solicita colores para cada grupo"""
        colors = []
        for _ in range(num_colors):
            color = QColorDialog.getColor()
            if color.isValid():
                colors.append(color.name())  # Color en hexadecimal
            else:
                colors.append("#000000")  # Negro por defecto
        return colors

    def plot(self, groups, color_map):
        """Dibuja el gráfico de burbujas"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

        for group in set(g for _, _, _, g in groups):
            x_vals = [x for x, y, s, g in groups if g == group]
            y_vals = [y for x, y, s, g in groups if g == group]
            sizes = [s for x, y, s, g in groups if g == group]
            ax.scatter(x_vals, y_vals, s=sizes, color=color_map[group], label=group, alpha=0.6, edgecolors="w")

        ax.set_title("Gráfico de Burbujas")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.legend()
        ax.grid(True)
        self.canvas.draw()

def get_graph():
    return BubbleChart()
