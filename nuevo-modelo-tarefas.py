import os
import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QListView

# Construimos la ruta absoluta a tick.png basada en la carpeta de este script
ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_tick = os.path.join(ruta_base, "tick.png")

imagen_tick = QImage(ruta_tick)
if imagen_tick.isNull():
    print(f"Advertencia: No se encontró o no se pudo cargar '{ruta_tick}'")
    tick = None
else:
    tick = imagen_tick.scaled(16, 16)


class ModeloTareas(QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []

    def rowCount(self, parent=None):
        return len(self.tareas)

    def data(self, indice, rol):
        if not indice.isValid():
            return None

        estado, texto = self.tareas[indice.row()]

        if rol == Qt.ItemDataRole.DisplayRole:
            return texto

        if rol == Qt.ItemDataRole.DecorationRole:
            if estado and tick is not None:
                return tick

        if rol == Qt.ItemDataRole.BackgroundRole:
            if estado:
                return QColor("lightgreen")

        return None


# Ejemplo básico de ventana para probar el modelo (puedes sustituirlo por tu QMainWindow actual)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tareas")

        lista = QListView()
        tareas_ejemplo = [
            (True, "Comprar pan"),
            (False, "Terminar práctica de DI"),
            (True, "Revisar ruta de tick.png"),
        ]
        self.modelo = ModeloTareas(tareas_ejemplo)
        lista.setModel(self.modelo)

        self.setCentralWidget(lista)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())