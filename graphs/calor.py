#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QComboBox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Calor"
GRAPH_SHORTCUT = "Ctrl+R"

class HeatmapCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Calor")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada de datos en forma de matriz
        self.data_input = QLineEdit()
        main_layout.addWidget(QLabel("Datos (filas separadas por ';', valores dentro de la fila por ','):"))
        main_layout.addWidget(self.data_input)

        # Entrada para etiquetas de filas
        self.y_labels_input = QLineEdit()
        main_layout.addWidget(QLabel("Etiquetas de las filas (separadas por coma):"))
        main_layout.addWidget(self.y_labels_input)

        # Entrada para etiquetas de columnas
        self.x_labels_input = QLineEdit()
        main_layout.addWidget(QLabel("Etiquetas de las columnas (separadas por coma):"))
        main_layout.addWidget(self.x_labels_input)

        # Selector de colormap
        self.cmap_selector = QComboBox()
        self.cmap_selector.addItems(["viridis", "plasma", "inferno", "magma", "cividis", "coolwarm", "Blues", "Greens", "Reds"])
        main_layout.addWidget(QLabel("Selecciona un mapa de colores:"))
        main_layout.addWidget(self.cmap_selector)

        # Botón para graficar
        plot_button = QPushButton("Graficar Heatmap")
        plot_button.clicked.connect(self.plot_heatmap)
        main_layout.addWidget(plot_button)

        # Lienzo para el gráfico
        self.heatmap_canvas = FigureCanvas(plt.figure(figsize=(7, 5)))
        main_layout.addWidget(self.heatmap_canvas)

        self.setLayout(main_layout)

    def plot_heatmap(self):
        try:
            # Obtener y procesar los datos
            data_text = self.data_input.text().strip()
            if not data_text:
                raise ValueError("Ingrese datos para graficar.")

            data = np.array([list(map(float, row.split(","))) for row in data_text.split(";")])

            # Obtener etiquetas
            y_labels_text = self.y_labels_input.text().strip()
            x_labels_text = self.x_labels_input.text().strip()

            y_labels = y_labels_text.split(",") if y_labels_text else [f"F{i+1}" for i in range(data.shape[0])]
            x_labels = x_labels_text.split(",") if x_labels_text else [f"C{i+1}" for i in range(data.shape[1])]

            if len(y_labels) != data.shape[0]:
                raise ValueError("El número de etiquetas de filas no coincide con los datos.")
            if len(x_labels) != data.shape[1]:
                raise ValueError("El número de etiquetas de columnas no coincide con los datos.")

            # Obtener colormap seleccionado
            cmap = self.cmap_selector.currentText()

            # Limpiar gráfico anterior y crear uno nuevo
            self.heatmap_canvas.figure.clear()
            ax = self.heatmap_canvas.figure.add_subplot(111)

            # Crear el heatmap
            cax = ax.imshow(data, cmap=cmap, aspect="auto")

            # Agregar etiquetas
            ax.set_xticks(np.arange(len(x_labels)))
            ax.set_yticks(np.arange(len(y_labels)))
            ax.set_xticklabels(x_labels)
            ax.set_yticklabels(y_labels)

            # Agregar colorbar
            self.heatmap_canvas.figure.colorbar(cax)

            # Ajustes finales
            ax.set_title("Gráfico de Calor")
            ax.set_xlabel("Columnas")
            ax.set_ylabel("Filas")
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

            self.heatmap_canvas.draw()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

def get_graph():
    return HeatmapCalculator()
