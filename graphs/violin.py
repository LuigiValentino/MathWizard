#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Violín"
GRAPH_SHORTCUT = "Ctrl+3"

class ViolinPlotCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Violín")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.data_input = QLineEdit()
        main_layout.addWidget(QLabel("Datos (grupos separados por ';', valores dentro del grupo separados por ','):"))
        main_layout.addWidget(self.data_input)

        self.labels_input = QLineEdit()
        main_layout.addWidget(QLabel("Nombres de los grupos (separados por coma):"))
        main_layout.addWidget(self.labels_input)

        self.color_button = QPushButton("Seleccionar Colores para los Grupos")
        self.color_button.clicked.connect(self.choose_colors)
        main_layout.addWidget(self.color_button)
        self.selected_colors = []

        plot_button = QPushButton("Graficar Violín")
        plot_button.clicked.connect(self.plot_violin)
        main_layout.addWidget(plot_button)

        self.violin_canvas = FigureCanvas(plt.figure(figsize=(8, 6)))
        main_layout.addWidget(self.violin_canvas)

        self.setLayout(main_layout)

    def choose_colors(self):
        """Seleccionar colores para cada grupo de datos"""
        data_text = self.data_input.text().strip()
        groups = data_text.split(";")
        self.selected_colors = [] 

        for i in range(len(groups)):
            color = QColorDialog.getColor()
            if color.isValid():
                self.selected_colors.append(color.name())  
            else:
                self.selected_colors.append("#000000")  

    def plot_violin(self):
        try:
            data_text = self.data_input.text().strip()
            if not data_text:
                raise ValueError("Ingrese datos para graficar.")
            groups = [list(map(float, group.split(","))) for group in data_text.split(";")]

            labels_text = self.labels_input.text().strip()
            labels = labels_text.split(",") if labels_text else [f"Grupo {i+1}" for i in range(len(groups))]

            if len(labels) != len(groups):
                raise ValueError("El número de nombres de grupos debe coincidir con la cantidad de grupos de datos.")

            if len(self.selected_colors) != len(groups):
                raise ValueError("Seleccione un color para cada grupo antes de graficar.")

            self.violin_canvas.figure.clear()
            ax = self.violin_canvas.figure.add_subplot(111)

            parts = ax.violinplot(groups, showmeans=True, showmedians=True)
            
            for i, pc in enumerate(parts["bodies"]):
                pc.set_facecolor(self.selected_colors[i])  
                pc.set_edgecolor("black")
                pc.set_alpha(0.7)

            ax.set_title("Gráfico de Violín")
            ax.set_xticks(range(1, len(groups) + 1))
            ax.set_xticklabels(labels)
            ax.set_xlabel("Grupos")
            ax.set_ylabel("Valores")
            ax.grid(True)

            self.violin_canvas.draw()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

def get_graph():
    return ViolinPlotCalculator()
