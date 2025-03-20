#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QColorDialog, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAPH_NAME = "Gráfico de Dispersión Complejo"
GRAPH_SHORTCUT = "Ctrl+S"

class ComplexScatterPlotCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico de Dispersión Complejo")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Entrada para los nombres de los grupos
        self.groups_name_input = QLineEdit()
        main_layout.addWidget(QLabel("Nombres de los grupos (separados por coma):"))
        main_layout.addWidget(self.groups_name_input)

        # Instrucciones para la entrada de puntos
        instrucciones = (
            "Formato de entrada:\n"
            "• Cada grupo se separa con '|'\n"
            "• Dentro de cada grupo, los puntos se separan con ';'\n"
            "• Cada punto se escribe entre paréntesis, con sus coordenadas separadas por coma.\n"
            "Ejemplo: (1,2);(3,4) | (5,6);(7,8);(9,10)"
        )
        main_layout.addWidget(QLabel(instrucciones))

        # Entrada para los grupos de puntos
        self.groups_input = QLineEdit()
        main_layout.addWidget(self.groups_input)

        # Botón para graficar
        plot_button = QPushButton("Graficar Dispersión")
        plot_button.clicked.connect(self.plot_scatter)
        main_layout.addWidget(plot_button)

        # Lienzo para el gráfico
        self.scatter_canvas = FigureCanvas(plt.figure())
        main_layout.addWidget(self.scatter_canvas)

        self.setLayout(main_layout)

    def plot_scatter(self):
        try:
            groups_text = self.groups_input.text()
            groups = self.parse_groups(groups_text)

            groups_names_text = self.groups_name_input.text()
            groups_names = self.parse_groups_names(groups_names_text, len(groups))

            colors = self.ask_for_colors(len(groups))

            self.plot(groups, colors, groups_names)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un problema al graficar: {e}")

    def parse_groups(self, text):
        """
        Convierte el texto de grupos en una lista de grupos.
        Cada grupo es una lista de puntos (tuplas de dos números).
        Formato esperado: (x,y);(x,y) | (x,y);(x,y);(x,y)
        """
        # Separar grupos usando '|'
        group_strs = text.split("|")
        parsed_groups = []
        for group_str in group_strs:
            group_str = group_str.strip()
            if not group_str:
                continue
            # Separar puntos usando ';'
            point_strs = group_str.split(";")
            group_points = []
            for pt in point_strs:
                pt = pt.strip()
                if pt.startswith("("):
                    pt = pt[1:]
                if pt.endswith(")"):
                    pt = pt[:-1]
                coords = pt.split(",")
                if len(coords) != 2:
                    raise ValueError(f"El punto '{pt}' no tiene 2 coordenadas.")
                try:
                    x, y = map(float, coords)
                except Exception as e:
                    raise ValueError(f"Error al convertir '{pt}' a números: {e}")
                group_points.append((x, y))
            parsed_groups.append(group_points)
        return parsed_groups

    def parse_groups_names(self, text, num_groups):
        """
        Convierte el texto de nombres en una lista de nombres.
        Debe haber exactamente 'num_groups' nombres, separados por coma.
        """
        names = [n.strip() for n in text.split(",") if n.strip()]
        if len(names) != num_groups:
            raise ValueError("La cantidad de nombres de grupos no coincide con la cantidad de grupos de puntos.")
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

    def plot(self, groups, colors, groups_names):
        """Dibuja el gráfico de dispersión con cada grupo en su color y nombre."""
        self.scatter_canvas.figure.clear()
        ax = self.scatter_canvas.figure.add_subplot(111)

        for i, group in enumerate(groups):
            x_values, y_values = zip(*group)
            ax.scatter(x_values, y_values, color=colors[i], label=groups_names[i])

        ax.set_title("Gráfico de Dispersión Complejo")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.legend()
        ax.grid(True)
        self.scatter_canvas.draw()

def get_graph():
    return ComplexScatterPlotCalculator()
