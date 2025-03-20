#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Velocímetro"
GRAPH_SHORTCUT = "Ctrl+2"

class GaugeChart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Velocímetro")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.value_input = QLineEdit()
        self.marks_input = QLineEdit()

        main_layout.addWidget(QLabel("Ingrese el valor del velocímetro (0-100):"))
        main_layout.addWidget(self.value_input)
        main_layout.addWidget(QLabel("Ingrese marcas personalizadas (separadas por coma, ej. 55, 89):"))
        main_layout.addWidget(self.marks_input)

        plot_button = QPushButton("Graficar Velocímetro")
        plot_button.clicked.connect(self.plot_gauge_chart)
        main_layout.addWidget(plot_button)

        self.canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_gauge_chart(self):
        try:
            value = float(self.value_input.text().strip())
            marks = self.marks_input.text().strip().split(',')

            if not 0 <= value <= 100:
                raise ValueError("El valor debe estar entre 0 y 100.")

            if not marks:
                marks = []
            else:
                marks = [float(m.strip()) for m in marks if 0 <= float(m.strip()) <= 100]

            self.plot(value, marks)

        except ValueError as e:
            QMessageBox.warning(self, "Error", f"Entrada inválida: {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot(self, value, marks):
        """Dibuja el gráfico de Velocímetro con marcas personalizadas y un estilo moderno"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111, polar=True)

        
        theta = np.linspace(np.pi, 0, 100)  
        ax.fill_between(theta, 0, 1, color="#3498db", alpha=0.8)  

        ax.set_ylim(0, 1)
        ax.set_xticks([]) 
        ax.set_yticks([])  
        ax.set_frame_on(False)

        for mark in marks:
            mark_angle = np.pi * (1 - mark / 100)  
            ax.plot([mark_angle, mark_angle], [0, 1], color="gray", linewidth=1) 
            ax.text(mark_angle, 1.05, f"{mark}%", horizontalalignment='center', fontsize=12, color="gray")

        needle_angle = np.pi * (1 - value / 100)
        ax.plot([needle_angle, needle_angle], [0, 1], color="black", linewidth=3, zorder=10)

        ax.add_artist(plt.Circle((0, 0), 0.1, color='white', ec="black", lw=4, zorder=15))

        ax.text(needle_angle, 1.15, f"{value}%", horizontalalignment='center', fontsize=20, fontweight='bold', color='black', zorder=20)



        self.canvas.draw()

def get_graph():
    return GaugeChart()
