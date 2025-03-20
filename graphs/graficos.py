#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# El nombre y atajo de teclado de la calculadora
GRAPH_NAME = "Gráficos Interactivos"
GRAPH_SHORTCUT = "Ctrl+U"

class GraphCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Gráficos Interactivos")
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Crear las pestañas
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_bar_chart_tab(), "Gráfico de Barras")
        self.tabs.addTab(self.create_line_chart_tab(), "Gráfico de Líneas")
        self.tabs.addTab(self.create_pie_chart_tab(), "Gráfico de Pastel")

        main_layout.addWidget(self.tabs)

        self.setLayout(main_layout)

    def create_bar_chart_tab(self):
        """Crea la pestaña de Gráfico de Barras."""
        tab = QWidget()
        layout = QVBoxLayout()

        # Formulario de entrada
        self.bar_categories_input = QLineEdit()
        self.bar_values_input = QLineEdit()
        layout.addWidget(QLabel("Categorías (separadas por comas):"))
        layout.addWidget(self.bar_categories_input)
        layout.addWidget(QLabel("Valores (separados por comas):"))
        layout.addWidget(self.bar_values_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Barras")
        plot_button.clicked.connect(self.plot_bar_chart)
        layout.addWidget(plot_button)

        # Crear un lienzo para el gráfico
        self.bar_canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.bar_canvas)

        tab.setLayout(layout)
        return tab

    def create_line_chart_tab(self):
        """Crea la pestaña de Gráfico de Líneas."""
        tab = QWidget()
        layout = QVBoxLayout()

        # Formulario de entrada
        self.line_x_input = QLineEdit()
        self.line_y_input = QLineEdit()
        layout.addWidget(QLabel("Valores del Eje X (separados por comas):"))
        layout.addWidget(self.line_x_input)
        layout.addWidget(QLabel("Valores del Eje Y (separados por comas):"))
        layout.addWidget(self.line_y_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Líneas")
        plot_button.clicked.connect(self.plot_line_chart)
        layout.addWidget(plot_button)

        # Crear un lienzo para el gráfico
        self.line_canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.line_canvas)

        tab.setLayout(layout)
        return tab

    def create_pie_chart_tab(self):
        """Crea la pestaña de Gráfico de Pastel."""
        tab = QWidget()
        layout = QVBoxLayout()

        # Formulario de entrada
        self.pie_labels_input = QLineEdit()
        self.pie_sizes_input = QLineEdit()
        layout.addWidget(QLabel("Etiquetas (separadas por comas):"))
        layout.addWidget(self.pie_labels_input)
        layout.addWidget(QLabel("Tamaños (separados por comas):"))
        layout.addWidget(self.pie_sizes_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Pastel")
        plot_button.clicked.connect(self.plot_pie_chart)
        layout.addWidget(plot_button)

        # Crear un lienzo para el gráfico
        self.pie_canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.pie_canvas)

        tab.setLayout(layout)
        return tab

    def plot_bar_chart(self):
        """Genera el gráfico de barras."""
        try:
            categories = self.bar_categories_input.text().split(',')
            values = list(map(float, self.bar_values_input.text().split(',')))
            self.plot_bar(categories, values)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot_bar(self, categories, values):
        """Dibuja el gráfico de barras en el lienzo."""
        self.bar_canvas.figure.clear()
        ax = self.bar_canvas.figure.add_subplot(111)
        ax.bar(categories, values)
        ax.set_title("Gráfico de Barras")
        ax.set_xlabel("Categorías")
        ax.set_ylabel("Valores")
        ax.grid(True)
        self.bar_canvas.draw()

    def plot_line_chart(self):
        """Genera el gráfico de líneas."""
        try:
            x_values = list(map(float, self.line_x_input.text().split(',')))
            y_values = list(map(float, self.line_y_input.text().split(',')))
            self.plot_line(x_values, y_values)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot_line(self, x_values, y_values):
        """Dibuja el gráfico de líneas en el lienzo."""
        self.line_canvas.figure.clear()
        ax = self.line_canvas.figure.add_subplot(111)
        ax.plot(x_values, y_values)
        ax.set_title("Gráfico de Líneas")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.grid(True)
        self.line_canvas.draw()

    def plot_pie_chart(self):
        """Genera el gráfico de pastel."""
        try:
            labels = self.pie_labels_input.text().split(',')
            sizes = list(map(float, self.pie_sizes_input.text().split(',')))
            self.plot_pie(labels, sizes)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def plot_pie(self, labels, sizes):
        """Dibuja el gráfico de pastel en el lienzo."""
        self.pie_canvas.figure.clear()
        ax = self.pie_canvas.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Gráfico de Pastel")
        self.pie_canvas.draw()

def get_graph():
    return GraphCalculator()
