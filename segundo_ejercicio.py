import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel,
                             QLineEdit, QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette

class CaixaCor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Prueba')
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        # 1. Widget central y su layout vertical principal
        contenedor = QWidget()
        layout_principal = QVBoxLayout(contenedor) # Asigna el layout directamente al contenedor

        # 2. Celdas usando tu clase CaixaCor (evita el problema del tamaño 0)

        columna1 = QHBoxLayout()
        celda1 = CaixaCor("red")
        celda2 = CaixaCor("green")
        celda3 = CaixaCor("blue")

        # 3. Añadir celdas a la columna
        columna1.addWidget(celda1)
        columna1.addWidget(celda2)
        columna1.addWidget(celda3)

        columna2 = QVBoxLayout()
        celda4 = CaixaCor("yellow")

        columna2.addWidget(celda4)

        layout_principal.addLayout(columna2)
        layout_principal.addLayout(columna1)

        # 4. Establecer el contenedor central
        self.setCentralWidget(contenedor)
        self.show()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiesta = FiestaPrincipal()
    aplicacion.exec()
