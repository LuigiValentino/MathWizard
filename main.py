#!/usr/bin/env python3
import sys
import os
import importlib.util
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMessageBox, QMenuBar
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MathWizard")
        self.setGeometry(100, 100, 1200, 800)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.create_menu()
        self.load_calculators()
        self.load_graphs()
        self.load_tools()
        self.load_help()

    def create_menu(self):
        menubar = self.menuBar()
        self.calculators_menu = menubar.addMenu("Calculadoras (C)")
        self.graphs_menu = menubar.addMenu("Gráficos (G)")  
        self.tools_menu = menubar.addMenu("Herramientas (H)")  
        self.help_menu = menubar.addMenu("Ayuda (A)")

    def load_calculators(self):
        calculators_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calculators")
        if not os.path.exists(calculators_dir):
            QMessageBox.warning(self, "Error", f"El directorio 'calculators' no existe: {calculators_dir}")
            return

        for filename in os.listdir(calculators_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_path = os.path.join(calculators_dir, filename)
                module_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if spec is None:
                    continue
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Error al cargar el módulo {module_name}:\n{e}")
                    continue

                if not hasattr(module, "CALCULATOR_NAME") or not hasattr(module, "get_calculator"):
                    continue

                calculator_name = module.CALCULATOR_NAME
                shortcut = getattr(module, "CALCULATOR_SHORTCUT", None)
                get_calculator = module.get_calculator

                action = QAction(calculator_name, self)
                if shortcut:
                    action.setShortcut(shortcut)
                action.triggered.connect(lambda checked, get_calculator=get_calculator, name=calculator_name: self.open_calculator(get_calculator, name))
                self.calculators_menu.addAction(action)

    def load_graphs(self):
        graphs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graphs")
        if not os.path.exists(graphs_dir):
            QMessageBox.warning(self, "Error", f"El directorio 'graphs' no existe: {graphs_dir}")
            return

        for filename in os.listdir(graphs_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_path = os.path.join(graphs_dir, filename)
                module_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if spec is None:
                    continue
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Error al cargar el módulo {module_name}:\n{e}")
                    continue

                if not hasattr(module, "GRAPH_NAME") or not hasattr(module, "get_graph"):
                    continue

                graph_name = module.GRAPH_NAME
                shortcut = getattr(module, "GRAPH_SHORTCUT", None)
                get_graph = module.get_graph

                action = QAction(graph_name, self)
                if shortcut:
                    action.setShortcut(shortcut)
                action.triggered.connect(lambda checked, get_graph=get_graph, name=graph_name: self.open_graph(get_graph, name))
                self.graphs_menu.addAction(action)

    def load_tools(self):
        tools_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
        if not os.path.exists(tools_dir):
            QMessageBox.warning(self, "Error", f"El directorio 'tools' no existe: {tools_dir}")
            return

        for filename in os.listdir(tools_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_path = os.path.join(tools_dir, filename)
                module_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if spec is None:
                    continue
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Error al cargar el módulo {module_name}:\n{e}")
                    continue

                if not hasattr(module, "TOOL_NAME") or not hasattr(module, "get_tool"):
                    continue

                tool_name = module.TOOL_NAME
                shortcut = getattr(module, "TOOL_SHORTCUT", None)
                get_tool = module.get_tool

                action = QAction(tool_name, self)
                if shortcut:
                    action.setShortcut(shortcut)
                action.triggered.connect(lambda checked, get_tool=get_tool, name=tool_name: self.open_tool(get_tool, name))
                self.tools_menu.addAction(action)

    def load_help(self):
        help_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "help")
        if not os.path.exists(help_dir):
            QMessageBox.warning(self, "Error", f"El directorio 'help' no existe: {help_dir}")
            return

        for filename in os.listdir(help_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_path = os.path.join(help_dir, filename)
                module_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if spec is None:
                    continue
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Error al cargar el módulo {module_name}:\n{e}")
                    continue

                if not hasattr(module, "HELP_NAME") or not hasattr(module, "get_help"):
                    continue

                help_name = module.HELP_NAME
                shortcut = getattr(module, "HELP_SHORTCUT", None)
                get_help = module.get_help

                action = QAction(help_name, self)
                if shortcut:
                    action.setShortcut(shortcut)
                action.triggered.connect(lambda checked, get_help=get_help, name=help_name: self.open_help(get_help, name))
                self.help_menu.addAction(action)

    def open_calculator(self, get_calculator, name):
        widget = get_calculator()

        subwindow = QMdiSubWindow()
        subwindow.setWidget(widget)
        subwindow.setWindowTitle(name)
        self.mdi.addSubWindow(subwindow)

    
        subwindow.resize(widget.sizeHint())
        subwindow.show()
        subwindow.adjustSize()  

    def open_graph(self, get_graph, name):
        widget = get_graph()

        subwindow = QMdiSubWindow()
        subwindow.setWidget(widget)
        subwindow.setWindowTitle(name)
        self.mdi.addSubWindow(subwindow)


        subwindow.resize(widget.sizeHint())
        subwindow.show()
        subwindow.adjustSize()  

    def open_tool(self, get_tool, name):
        widget = get_tool()

        subwindow = QMdiSubWindow()
        subwindow.setWidget(widget)
        subwindow.setWindowTitle(name)
        self.mdi.addSubWindow(subwindow)


        subwindow.resize(widget.sizeHint())
        subwindow.show()
        subwindow.adjustSize() 

    def open_help(self, get_help, name):
        widget = get_help()

        subwindow = QMdiSubWindow()
        subwindow.setWidget(widget)
        subwindow.setWindowTitle(name)
        self.mdi.addSubWindow(subwindow)

        subwindow.resize(widget.sizeHint())
        subwindow.show()
        subwindow.adjustSize()  

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_C: 
            self.calculators_menu.popup(self.mapToGlobal(self.calculators_menu.geometry().topLeft()))
        elif event.key() == Qt.Key_G:  
            self.graphs_menu.popup(self.mapToGlobal(self.graphs_menu.geometry().topLeft()))
        elif event.key() == Qt.Key_H: 
            self.tools_menu.popup(self.mapToGlobal(self.tools_menu.geometry().topLeft()))
        elif event.key() == Qt.Key_A:  
            self.help_menu.popup(self.mapToGlobal(self.help_menu.geometry().topLeft()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyleSheet("""
    QMainWindow {
        background-color: #eaeaea; /* Un gris claro para evitar el blanco puro */
    }
    QMenuBar {
        background-color: white;
        color: #333;
        font-size: 14px;
        padding: 5px;
        border-bottom: 1px solid #bbb;
    }
    QMenuBar::item {
        padding: 8px;
    }
    QMenuBar::item:selected {
        background-color: #d6d6d6;
        border-radius: 4px;
    }
    QMenu {
        background-color: #f5f5f5;
        color: #333;
        font-size: 14px;
        border: 1px solid #bbb;
    }
    QMenu::item {
        padding: 8px 20px;
        margin: 2px;
        border-radius: 4px;
    }
    QMenu::item:selected {
        background-color: #d6d6d6;
    }



""")



    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
