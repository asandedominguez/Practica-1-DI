import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton,
    QWidget, QLabel, QLineEdit, QHBoxLayout
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

        self.setWindowTitle('Panel de Estado')
        self.setMinimumSize(400, 220)
        self.setMaximumSize(600, 400)

        caja = QVBoxLayout()

        # 1. Panel superior con únicamente la etiqueta centrada
        self.color = PanelColor("gray")
        self.pantalla_etiqueta = QLabel("Sistema en espera")
        self.pantalla_etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_panel = QVBoxLayout(self.color)
        layout_panel.addWidget(self.pantalla_etiqueta)

        # 2. Fila inferior horizontal con el QLineEdit y los 3 botones
        fila_inferior = QHBoxLayout()

        self.texto = QLineEdit()
        self.texto.setPlaceholderText("Introduce un mensaje...")

        boton1 = QPushButton("Activo")
        boton2 = QPushButton("Alerta")
        boton3 = QPushButton("Crítico")

        # Conexión directa de cada botón a su propio método sin lambda
        boton1.clicked.connect(self.on_activo_clicked)
        boton2.clicked.connect(self.on_alerta_clicked)
        boton3.clicked.connect(self.on_critico_clicked)

        fila_inferior.addWidget(self.texto)
        fila_inferior.addWidget(boton1)
        fila_inferior.addWidget(boton2)
        fila_inferior.addWidget(boton3)

        # 3. Ensamblaje en el layout principal
        caja.addWidget(self.color)
        caja.addLayout(fila_inferior)

        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)

    def on_activo_clicked(self):
        mensaje = self.texto.text().strip()
        if not mensaje:
            self.pantalla_etiqueta.setText("Por favor, introduce un mensaje")
            return

        self.pantalla_etiqueta.setText("Activo: " + mensaje)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("green"))
        self.color.setPalette(paleta)

    def on_alerta_clicked(self):
        mensaje = self.texto.text().strip()
        if not mensaje:
            self.pantalla_etiqueta.setText("Por favor, introduce un mensaje")
            return

        self.pantalla_etiqueta.setText("¡Alerta!: " + mensaje)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("yellow"))
        self.color.setPalette(paleta)

    def on_critico_clicked(self):
        mensaje = self.texto.text().strip()
        if not mensaje:
            self.pantalla_etiqueta.setText("Por favor, introduce un mensaje")
            return

        self.pantalla_etiqueta.setText("¡Crítico!: " + mensaje)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("red"))
        self.color.setPalette(paleta)


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = FiestaPrincipal()
    ventana.show()
    sys.exit(app.exec())