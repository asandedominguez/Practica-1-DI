import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListView, QLineEdit, QPushButton
)


class ModeloTareas(QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas if tareas is not None else []

    def rowCount(self, index):
        return len(self.tareas)

    def data(self, index, role):
        if not index.isValid():
            return None

        completada, texto = self.tareas[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            estado = "✔" if completada else "✘"
            return f"[{estado}] {texto}"

        if role == Qt.ItemDataRole.ForegroundRole:
            if completada:
                return QColor("green")
            return QColor("black")

        return None


class GestorTareas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas (Modelo-Vista)")
        self.setMinimumSize(420, 360)

        layout_principal = QVBoxLayout()

        # 1. Vista y Modelo
        self.modelo = ModeloTareas([
            [False, "Repasar layouts en PyQt6"],
            [True, "Configurar entorno virtual"]
        ])
        self.vista = QListView()
        self.vista.setModel(self.modelo)
        layout_principal.addWidget(self.vista)

        # 2. Campo de entrada y botón Añadir
        fila_entrada = QHBoxLayout()
        self.txt_tarea = QLineEdit()
        self.txt_tarea.setPlaceholderText("Escribe una nueva tarea...")
        self.btn_anadir = QPushButton("Añadir")
        fila_entrada.addWidget(self.txt_tarea)
        fila_entrada.addWidget(self.btn_anadir)
        layout_principal.addLayout(fila_entrada)

        # 3. Botones de acción sobre la tarea seleccionada
        fila_acciones = QHBoxLayout()
        self.btn_completar = QPushButton("Completar / Desmarcar")
        self.btn_eliminar = QPushButton("Eliminar")
        fila_acciones.addWidget(self.btn_completar)
        fila_acciones.addWidget(self.btn_eliminar)
        layout_principal.addLayout(fila_acciones)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # Conexiones explícitas sin lambda
        self.btn_anadir.clicked.connect(self.anadir_tarea)
        self.txt_tarea.returnPressed.connect(self.anadir_tarea)
        self.btn_completar.clicked.connect(self.alternar_estado)
        self.btn_eliminar.clicked.connect(self.eliminar_tarea)

    def anadir_tarea(self):
        texto = self.txt_tarea.text().strip()
        if not texto:
            return
        self.modelo.tareas.append([False, texto])
        self.modelo.layoutChanged.emit()
        self.txt_tarea.clear()

    def alternar_estado(self):
        indices = self.vista.selectedIndexes()
        if indices:
            fila = indices[0].row()
            self.modelo.tareas[fila][0] = not self.modelo.tareas[fila][0]
            self.modelo.layoutChanged.emit()

    def eliminar_tarea(self):
        indices = self.vista.selectedIndexes()
        if indices:
            fila = indices[0].row()
            del self.modelo.tareas[fila]
            self.modelo.layoutChanged.emit()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = GestorTareas()
    ventana.show()
    sys.exit(aplicacion.exec())