import sys
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListView, QLineEdit, QPushButton, QLabel, QComboBox, QStackedLayout,
    QRadioButton, QFormLayout
)


# ==============================================================================
# PARTE A: MODELO DE DATOS (QAbstractListModel)
# ==============================================================================
class ModeloContactos(QAbstractListModel):
    def __init__(self, contactos=None):
        super().__init__()
        # Estructura: (es_favorito: bool, nombre: str)
        self.contactos = contactos or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.contactos)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        es_fav, nombre = self.contactos[index.row()]
        prefijo = "⭐ " if es_fav else ""
        return f"{prefijo}{nombre}"

    def engadir(self, nombre):
        if nombre:
            posicion = len(self.contactos)
            self.beginInsertRows(QModelIndex(), posicion, posicion)
            self.contactos.append((False, nombre))
            self.endInsertRows()

    def eliminar(self, fila):
        if 0 <= fila < len(self.contactos):
            self.beginRemoveRows(QModelIndex(), fila, fila)
            del self.contactos[fila]
            self.endRemoveRows()


# ==============================================================================
# VENTANA PRINCIPAL
# ==============================================================================
class VentanaGestionContactos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Contactos y Formulario Adaptativo")
        self.resize(450, 500)

        # Layout Principal
        layout_principal = QVBoxLayout()

        # ----------------------------------------------------------------------
        # PARTE A: LISTA Y CONTROLES MODELO-VISTA
        # ----------------------------------------------------------------------
        layout_principal.addWidget(QLabel("<b>Lista de Contactos:</b>"))

        # Modelo y Vista
        self.modelo = ModeloContactos([
            (True, "Ana López"),
            (False, "Carlos Gómez"),
            (False, "María Rodríguez")
        ])
        self.vista_lista = QListView()
        self.vista_lista.setModel(self.modelo)
        layout_principal.addWidget(self.vista_lista)

        # Entrada de nuevo contacto y botón añadir
        layout_entrada = QHBoxLayout()
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre del nuevo contacto...")
        self.btn_engadir = QPushButton("Añadir Contacto")

        layout_entrada.addWidget(self.input_nombre)
        layout_entrada.addWidget(self.btn_engadir)
        layout_principal.addLayout(layout_entrada)

        # Botón para borrar
        self.btn_eliminar = QPushButton("Eliminar Seleccionado")
        layout_principal.addWidget(self.btn_eliminar)

        # Separador visual
        layout_principal.addWidget(QLabel("<hr>"))

        # ----------------------------------------------------------------------
        # PARTE B: FORMULARIO DINÁMICO (QStackedLayout)
        # ----------------------------------------------------------------------
        layout_principal.addWidget(QLabel("<b>Detalles del Tipo de Contacto:</b>"))

        # ComboBox para seleccionar el tipo de contacto
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Personal", "Trabajo"])
        layout_principal.addWidget(self.combo_tipo)

        # QStackedLayout para alternar entre paneles
        self.stacked_layout = QStackedLayout()

        # Panel 1: Personal
        panel_personal = QWidget()
        form_personal = QFormLayout(panel_personal)
        form_personal.addRow("Cumpleaños:", QLineEdit())

        layout_radio = QHBoxLayout()
        radio_familia = QRadioButton("Familia")
        radio_amigo = QRadioButton("Amigo")
        radio_amigo.setChecked(True)
        layout_radio.addWidget(radio_familia)
        layout_radio.addWidget(radio_amigo)
        form_personal.addRow("Relación:", layout_radio)

        # Panel 2: Trabajo
        panel_trabajo = QWidget()
        form_trabajo = QFormLayout(panel_trabajo)
        form_trabajo.addRow("Empresa:", QLineEdit())

        combo_dpto = QComboBox()
        combo_dpto.addItems(["IT", "Ventas", "RRHH"])
        form_trabajo.addRow("Departamento:", combo_dpto)

        # Añadimos los paneles al QStackedLayout
        self.stacked_layout.addWidget(panel_personal)
        self.stacked_layout.addWidget(panel_trabajo)

        # Contenedor para alojar el QStackedLayout dentro del layout principal
        contenedor_stacked = QWidget()
        contenedor_stacked.setLayout(self.stacked_layout)
        layout_principal.addWidget(contenedor_stacked)

        # ----------------------------------------------------------------------
        # CONEXIONES DE SEÑALES Y SLOTS
        # ----------------------------------------------------------------------
        self.btn_engadir.clicked.connect(self.on_engadir_clicked)
        self.input_nombre.returnPressed.connect(self.on_engadir_clicked)
        self.btn_eliminar.clicked.connect(self.on_eliminar_clicked)
        self.combo_tipo.currentIndexChanged.connect(self.stacked_layout.setCurrentIndex)

        # Asignar contenedor central
        contenedor_central = QWidget()
        contenedor_central.setLayout(layout_principal)
        self.setCentralWidget(contenedor_central)

    # --------------------------------------------------------------------------
    # MÉTODOS HANDLER (SLOTS)
    # --------------------------------------------------------------------------
    def on_engadir_clicked(self):
        texto = self.input_nombre.text().strip()
        if texto:
            self.modelo.engadir(texto)
            self.input_nombre.clear()

    def on_eliminar_clicked(self):
        indices = self.vista_lista.selectedIndexes()
        if indices:
            fila = indices[0].row()
            self.modelo.eliminar(fila)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaGestionContactos()
    ventana.show()
    sys.exit(app.exec())