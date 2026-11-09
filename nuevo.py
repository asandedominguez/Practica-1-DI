import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QLabel, QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QGridLayout, QHBoxLayout
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
        self.setWindowTitle("Lista de Tareas PyQt6")
        self.resize(400, 350)

        # 1. Datos de ejemplo
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

        # 4. Campo de texto y botón para AÑADIR
        self.input_texto = QLineEdit()
        self.input_texto.setPlaceholderText("Escribe una nueva tarea...")
        self.btn_engadir = QPushButton("Añadir")

        layout_entrada = QHBoxLayout()
        layout_entrada.addWidget(self.input_texto)
        layout_entrada.addWidget(self.btn_engadir)

        # 5. Botones para HECHO y BORRAR
        self.btn_feito = QPushButton("Marcar Hecho / Deshacer")
        self.btn_borrar = QPushButton("Borrar Tarea")

        layout_acciones = QHBoxLayout()
        layout_acciones.addWidget(self.btn_feito)
        layout_acciones.addWidget(self.btn_borrar)

        # 6. Colocamos todo en el layout principal de la ventana
        layout = QVBoxLayout()
        layout.addWidget(QLabel("<b>Lista de Tareas:</b>"))
        layout.addLayout(layout_entrada)
        layout.addWidget(self.vista_lista)
        layout.addLayout(layout_acciones)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # 7. Conexiones de botones a sus funciones
        self.btn_engadir.clicked.connect(self.on_engadir)
        self.input_texto.returnPressed.connect(self.on_engadir)
        self.btn_borrar.clicked.connect(self.on_borrar)
        self.btn_feito.clicked.connect(self.on_feito)

    def on_engadir(self):
        texto = self.input_texto.text().strip()
        if texto:
            posicion = len(self.modelo.tarefas)
            # Notificamos a la vista que insertamos una fila
            self.modelo.beginInsertRows(QModelIndex(), posicion, posicion)
            self.modelo.tarefas.append((False, texto))
            self.modelo.endInsertRows()
            self.input_texto.clear()

    def on_borrar(self):
        indices = self.vista_lista.selectedIndexes()
        if indices:
            fila = indices[0].row()
            # Notificamos a la vista que eliminamos una fila
            self.modelo.beginRemoveRows(QModelIndex(), fila, fila)
            del self.modelo.tarefas[fila]
            self.modelo.endRemoveRows()

    def on_feito(self):
        indices = self.vista_lista.selectedIndexes()
        if indices:
            fila = indices[0].row()
            completado, texto = self.modelo.tarefas[fila]

            # Si ya está marcada como hecha, le quitamos el tachado/marcado; si no, se lo ponemos
            if texto.startswith("[✔] "):
                nuevo_texto = texto.replace("[✔] ", "", 1)
                self.modelo.tarefas[fila] = (False, nuevo_texto)
            else:
                nuevo_texto = "[✔] " + texto
                self.modelo.tarefas[fila] = (True, nuevo_texto)

            # Notificamos a la vista que esa fila ha cambiado su contenido
            idx = self.modelo.index(fila)
            self.modelo.dataChanged.emit(idx, idx, [Qt.ItemDataRole.DisplayRole])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrueba()
    ventana.show()
    sys.exit(app.exec())