import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QLabel
)
class ModeloTarefas(QAbstractListModel):
    def __init__(self, tarefas = None):
        super().__init__()
        self.tarefas = tarefas or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tarefas[indice.row()]
            return texto

    def rowCount(self, indice):
        return len(self.tarefas)

class VentanaPrueba(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prueba de ModeloTarefas")
        self.resize(300, 250)

        # 1. Datos de ejemplo: Tuplas de (estado_booleano, "Texto de la tarea")
        datos_ejemplo = [
            (False, "Comprar leche"),
            (True, "Lavar el coche"),
            (False, "Estudiar PyQt6"),
            (True, "Hacer la comida"),
            (False, "Pasear al perro")
        ]

        # 2. Instanciamos tu modelo con los datos de ejemplo
        self.modelo = ModeloTarefas(datos_ejemplo)

        # 3. Creamos la vista (QListView) y le asignamos tu modelo
        self.vista_lista = QListView()
        self.vista_lista.setModel(self.modelo)

        # 4. Colocamos todo en la ventana
        layout = QVBoxLayout()
        layout.addWidget(QLabel("<b>Lista de Tareas:</b>"))
        layout.addWidget(self.vista_lista)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrueba()
    ventana.show()
    sys.exit(app.exec())