#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox, QFormLayout
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Matríz de Correlación"
GRAPH_SHORTCUT = "Ctrl+X"

class CorrelationMatrixChart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Matríz de Correlación")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Layout para ingresar los datos
        form_layout = QFormLayout()

        # Entrada para las columnas
        self.columns_input = QLineEdit()
        form_layout.addRow("Nombres de las columnas (separados por coma):", self.columns_input)

        # Entrada para los datos
        self.data_input = QLineEdit()
        form_layout.addRow("Datos de las columnas (cada fila separada por coma y los valores de las columnas por espacio):", self.data_input)

        main_layout.addLayout(form_layout)

        # Botón para graficar
        plot_button = QPushButton("Graficar Matríz de Correlación")
        plot_button.clicked.connect(self.plot_correlation_matrix)
        main_layout.addWidget(plot_button)

        # Crear lienzo para el gráfico
        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_correlation_matrix(self):
        try:
            # Obtener los datos ingresados
            columns = self.columns_input.text().split(',')
            data_text = self.data_input.text().split(',')

            if len(data_text) == 0 or len(columns) == 0:
                raise ValueError("Los datos y las columnas no pueden estar vacíos.")

            # Convertir los datos de texto a una matriz
            data = []
            for row in data_text:
                data.append([float(x) for x in row.strip().split()])

            # Crear un DataFrame con los datos
            df = pd.DataFrame(data, columns=columns)

            # Calcular la matriz de correlación
            corr_matrix = df.corr()

            # Graficar la matriz de correlación usando un heatmap
            self.plot(corr_matrix)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot(self, corr_matrix):
        """Dibuja el gráfico de la matriz de correlación"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

        # Graficar la matriz de correlación
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax, fmt='.2f', center=0)

        # Ajustar la apariencia
        ax.set_title("Matriz de Correlación")
        self.canvas.draw()

def get_graph():
    return CorrelationMatrixChart()
