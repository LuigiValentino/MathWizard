#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Cajas"
GRAPH_SHORTCUT = "Ctrl+Q"

class BoxPlotCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Cajas")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada para los datos de los grupos
        self.groups_input = QLineEdit()
        self.groups_names_input = QLineEdit()
        
        main_layout.addWidget(QLabel("Datos de los grupos (separados por |, valores separados por coma) EJ: 1,2,3|4,5,6|7,8,9"))
        main_layout.addWidget(self.groups_input)

        main_layout.addWidget(QLabel("Nombres de los grupos (separados por |) EJ: Grupo 1|Grupo 2|Grupo 3"))
        main_layout.addWidget(self.groups_names_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Caja")
        plot_button.clicked.connect(self.plot_box)
        main_layout.addWidget(plot_button)

        # Lienzo para el gráfico
        self.box_canvas = FigureCanvas(plt.figure(figsize=(8, 6)))
        main_layout.addWidget(self.box_canvas)

        self.setLayout(main_layout)

    def plot_box(self):
        try:
            groups_text = self.groups_input.text()
            groups_names_text = self.groups_names_input.text()

            # Convertir texto a datos
            groups_data = self.parse_groups(groups_text)
            group_names = self.parse_names(groups_names_text)

            if len(groups_data) != len(group_names):
                raise ValueError("La cantidad de grupos no coincide con la cantidad de nombres.")

            self.plot(groups_data, group_names)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_groups(self, text):
        """Convierte el texto de grupos en una lista de listas de valores."""
        groups = text.split("|")
        parsed_groups = []
        for group in groups:
            values = [float(v.strip()) for v in group.split(",")]
            parsed_groups.append(values)
        return parsed_groups

    def parse_names(self, text):
        """Convierte el texto de los nombres en una lista de nombres."""
        return [name.strip() for name in text.split("|")]

    def plot(self, groups_data, group_names):
        """Dibuja el gráfico de cajas"""
        self.box_canvas.figure.clear()
        ax = self.box_canvas.figure.add_subplot(111)

        # Graficar el Box Plot
        ax.boxplot(groups_data, patch_artist=True, boxprops=dict(facecolor="skyblue", color="black"),
                   flierprops=dict(marker='o', color='red', markersize=6), 
                   medianprops=dict(color="blue"))

        # Configuración del gráfico
        ax.set_title("Gráfico de Cajas", size=20)
        ax.set_xlabel("Grupos")
        ax.set_ylabel("Valores")

        # Etiquetas con los nombres de los grupos
        ax.set_xticklabels(group_names)

        ax.grid(True)
        self.box_canvas.draw()

def get_graph():
    return BoxPlotCalculator()
