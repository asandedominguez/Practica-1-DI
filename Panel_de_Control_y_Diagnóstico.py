import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton,
    QWidget, QLabel, QLineEdit, QHBoxLayout, QComboBox, QStackedLayout, QGridLayout, QCheckBox, QGroupBox, QRadioButton, QDial, QSizePolicy
)

from PyQt6.QtGui import QColor, QPalette

class PanelColor(QWidget):
    def __init__(self, cor):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)

class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Diagnóstico industrial')
        self.setMinimumSize(560, 460)
        self.setMaximumSize(600, 800)

        caja = QVBoxLayout()

        vertical = QVBoxLayout()

        self.color = PanelColor("gray")
        self.mensaje = QLabel("Sistema detenido")
        self.mensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)

        panel = QVBoxLayout(self.color)
        panel.addWidget(self.mensaje)

        apilar = QStackedLayout()

        self.menu = QComboBox()
        self.menu.addItems(["Control manual", "parametros", "registros"])
        self.menu.setCurrentIndex(0)

        caja.addWidget(self.menu)

        control = QWidget()
        vista = QGridLayout()

        self.checkbox = QCheckBox("Activar sistema")
        vista.addWidget(self.checkbox,0,0,1,2)

        self.checkbox.stateChanged.connect(self.activarZoa)
        self.activarZoa(0)

        self.grupo_modo = QGroupBox("Estado operativo")
        vista.addWidget(self.grupo_modo,1,0)

        layout_modo = QHBoxLayout()

        self.normal = QRadioButton("normal")
        self.emergencia = QRadioButton("Calor")
        self.normal.setChecked(True)
        layout_modo.addWidget(self.normal)
        layout_modo.addWidget(self.emergencia)
        self.grupo_modo.setLayout(layout_modo)

        self.dial = QDial()
        self.dial.setRange(0, 100)
        vista.addWidget(self.dial, 1, 1)

        reset = QPushButton("Resetear")

        reset.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        vista.addWidget(reset, 0, 2, 2, 1)

        control.setLayout(vista)

        apilar.addWidget()
