#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Radar"
GRAPH_SHORTCUT = "Ctrl+Z"

class RadarChartCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Radar")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.categories_input = QLineEdit()
        main_layout.addWidget(QLabel("Categorías (separadas por coma):"))
        main_layout.addWidget(self.categories_input)

        self.groups_names_input = QLineEdit()
        main_layout.addWidget(QLabel("Nombres de los grupos (separados por coma):"))
        main_layout.addWidget(self.groups_names_input)

        self.groups_values_input = QLineEdit()
        main_layout.addWidget(QLabel("Valores de cada grupo (separados por coma y '|'):"))
        main_layout.addWidget(self.groups_values_input)

        plot_button = QPushButton("Graficar Radar")
        plot_button.clicked.connect(self.plot_radar)
        main_layout.addWidget(plot_button)

        self.radar_canvas = FigureCanvas(plt.figure(figsize=(8, 8)))  
        main_layout.addWidget(self.radar_canvas)

        self.setLayout(main_layout)

    def plot_radar(self):
        try:
            categories_text = self.categories_input.text()
            categories = self.parse_categories(categories_text)

            groups_values_text = self.groups_values_input.text()
            groups_values = self.parse_groups_values(groups_values_text)

            groups_names_text = self.groups_names_input.text()
            groups_names = self.parse_groups_names(groups_names_text)

            if len(groups_values) != len(groups_names):
                raise ValueError("El número de grupos no coincide con el número de nombres de grupos.")

            colors = self.ask_for_colors(len(groups_values))

            self.plot(categories, groups_values, groups_names, colors)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_categories(self, text):
        """Convierte el texto de categorías en una lista."""
        categories = [cat.strip() for cat in text.split(",")]
        if len(categories) < 2:
            raise ValueError("Debe haber al menos 2 categorías.")
        return categories

    def parse_groups_values(self, text):
        """Convierte el texto de valores de grupos en una lista de listas de valores."""
        groups = text.split("|")
        parsed_groups = []
        for group in groups:
            values = [float(v.strip()) for v in group.split(",")]
            if len(values) != len(self.parse_categories(self.categories_input.text())):
                raise ValueError("El número de valores no coincide con el número de categorías.")
            parsed_groups.append(values)
        return parsed_groups

    def parse_groups_names(self, text):
        """Convierte el texto de nombres de grupos en una lista."""
        names = [name.strip() for name in text.split(",")]
        if len(names) < 1:
            raise ValueError("Debe haber al menos un nombre de grupo.")
        return names

    def ask_for_colors(self, num_groups):
        """Solicita un color para cada grupo mediante un cuadro de diálogo."""
        colors = []
        for i in range(num_groups):
            color = QColorDialog.getColor(title=f"Selecciona color para el Grupo {i+1}")
            if color.isValid():
                colors.append(color.name())
            else:
                colors.append("#000000")
        return colors

    def plot(self, categories, groups_values, groups_names, colors):
        """Dibuja el gráfico de radar con cada grupo en su color y nombre."""
        self.radar_canvas.figure.clear()
        ax = self.radar_canvas.figure.add_subplot(111, polar=True)

        num_categories = len(categories)
        angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

        groups_values = [group + [group[0]] for group in groups_values]
        angles += angles[:1]  

        for i, group_values in enumerate(groups_values):
            ax.plot(angles, group_values, color=colors[i], label=groups_names[i], linewidth=2, linestyle='solid')
            ax.fill(angles, group_values, color=colors[i], alpha=0.4)

        ax.set_title("Gráfico de Radar", size=20, color='blue', y=1.1)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=12)

        ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

        plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1)

        self.radar_canvas.draw()

def get_graph():
    return RadarChartCalculator()
