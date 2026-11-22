import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListView, QLineEdit, QPushButton
)


# ==============================================================================
# 1. MODELO DE DATOS (Patrón Modelo-Vista)
# ==============================================================================
class ModeloTareas(QAbstractListModel):
    """Almacena los datos puros y le indica a la vista cómo debe dibujarlos."""

    def __init__(self, tareas=None):
        super().__init__()  # Inicializa QAbstractListModel
        # Lista interna donde cada elemento es [completada (bool), texto (str)]
        self.tareas = tareas if tareas is not None else []

    def rowCount(self, index):
        # Método obligatorio: le dice a la lista cuántas filas totales existen
        return len(self.tareas)

    def data(self, index, role):
        # Método obligatorio: la vista lo llama automáticamente para cada fila y propiedad
        if not index.isValid():
            return None

        # Extraemos el estado y el texto de la fila solicitada
        completada, texto = self.tareas[index.row()]

        # DisplayRole: define el texto visible en la fila
        if role == Qt.ItemDataRole.DisplayRole:
            estado = "✔" if completada else "✘"
            return f"[{estado}] {texto}"

        # ForegroundRole: define el color de la letra de esa fila
        if role == Qt.ItemDataRole.ForegroundRole:
            if completada:
                return QColor("green")  # Verde si está completada
            return QColor("black")  # Negro si está pendiente

        return None


# ==============================================================================
# 2. VENTANA PRINCIPAL (Vista y Controlador)
# ==============================================================================
class GestorTareas(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle("Gestor de Tareas (Modelo-Vista)")  # Título superior
        self.setMinimumSize(420, 360)  # Tamaño mínimo permitido

        # Layout principal vertical: arriba la lista, en medio el input, abajo los botones
        layout_principal = QVBoxLayout()

        # --- ZONA SUPERIOR: Enlace entre Modelo y Vista ---
        self.modelo = ModeloTareas([
            [False, "Repasar layouts en PyQt6"],
            [True, "Configurar entorno virtual"]
        ])
        self.vista = QListView()  # Widget visual optimizado para listas
        self.vista.setModel(self.modelo)  # Conecta la vista con nuestra fuente de datos
        layout_principal.addWidget(self.vista)

        # --- ZONA INTERMEDIA: Entrada de nuevas tareas ---
        fila_entrada = QHBoxLayout()
        self.txt_tarea = QLineEdit()
        self.txt_tarea.setPlaceholderText("Escribe una nueva tarea...")
        self.btn_anadir = QPushButton("Añadir")

        fila_entrada.addWidget(self.txt_tarea)
        fila_entrada.addWidget(self.btn_anadir)
        layout_principal.addLayout(fila_entrada)

        # --- ZONA INFERIOR: Acciones sobre la tarea seleccionada ---
        fila_acciones = QHBoxLayout()
        self.btn_completar = QPushButton("Completar / Desmarcar")
        self.btn_eliminar = QPushButton("Eliminar")

        fila_acciones.addWidget(self.btn_completar)
        fila_acciones.addWidget(self.btn_eliminar)
        layout_principal.addLayout(fila_acciones)

        # --- ENSAMBLAJE FINAL ---
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # --- CONEXIÓN DE SEÑALES Y SLOTS ---
        self.btn_anadir.clicked.connect(self.anadir_tarea)
        self.txt_tarea.returnPressed.connect(self.anadir_tarea)  # Permite añadir con Enter
        self.btn_completar.clicked.connect(self.alternar_estado)
        self.btn_eliminar.clicked.connect(self.eliminar_tarea)

    # ==========================================================================
    # 3. MÉTODOS DE MANIPULACIÓN DE DATOS (SLOTS)
    # ==========================================================================
    def anadir_tarea(self):
        texto = self.txt_tarea.text().strip()
        if not texto:  # Si el campo está vacío, no hace nada
            return

        # Añadimos la nueva tarea como pendiente (False) al modelo
        self.modelo.tareas.append([False, texto])
        # Avisamos a la vista de que los datos cambiaron para que se redibuje
        self.modelo.layoutChanged.emit()
        self.txt_tarea.clear()  # Limpiamos la caja de texto

    def alternar_estado(self):
        # Obtenemos los índices de las filas seleccionadas actualmente en la vista
        indices = self.vista.selectedIndexes()
        if indices:
            fila = indices[0].row()  # Tomamos el número de fila del elemento seleccionado
            # Invertimos el booleano (True -> False / False -> True)
            self.modelo.tareas[fila][0] = not self.modelo.tareas[fila][0]
            self.modelo.layoutChanged.emit()  # Refrescamos la vista

    def eliminar_tarea(self):
        indices = self.vista.selectedIndexes()
        if indices:
            fila = indices[0].row()
            del self.modelo.tareas[fila]  # Borramos la tarea de la lista del modelo
            self.modelo.layoutChanged.emit()  # Refrescamos la vista


# ==============================================================================
# 4. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = GestorTareas()  # Crea nuestra ventana
    ventana.show()  # Muestra la ventana en pantalla
    sys.exit(aplicacion.exec())  # Inicia el bucle de eventos hasta cerrar