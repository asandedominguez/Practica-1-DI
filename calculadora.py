import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QGridLayout, QSizePolicy)
from PyQt6.QtGui import QColor, QPalette


class caixa_cor(QWidget):
    def __init__(self, cor):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)


class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(' calvo ---->')
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        caja = QVBoxLayout()

        pantalla = QHBoxLayout()
        pantalla.addWidget(caixa_cor("red"))

        colum1 = QHBoxLayout()
        colum1.addWidget(QPushButton("borrar"))
        colum1.addWidget(QPushButton("("))
        colum1.addWidget(QPushButton(")"))
        colum1.addWidget(QPushButton("mod"))
        colum1.addWidget(QPushButton("π"))

        colum2 = QHBoxLayout()
        colum2.addWidget(QPushButton("7"))
        colum2.addWidget(QPushButton("8"))
        colum2.addWidget(QPushButton("9"))
        colum2.addWidget(QPushButton("÷"))
        colum2.addWidget(QPushButton("√"))

        colum3 = QHBoxLayout()
        colum3.addWidget(QPushButton("4"))
        colum3.addWidget(QPushButton("5"))
        colum3.addWidget(QPushButton("6"))
        colum3.addWidget(QPushButton("x"))
        colum3.addWidget(QPushButton("x2"))

        igual = QGridLayout()

        igual.addWidget(QPushButton("1"), 0, 0)
        igual.addWidget(QPushButton("2"), 0, 1)
        igual.addWidget(QPushButton("3"), 0, 2)
        igual.addWidget(QPushButton("-"), 0, 3)

        igual.addWidget(QPushButton("0"), 1, 0)
        igual.addWidget(QPushButton(","), 1, 1)
        igual.addWidget(QPushButton("%"), 1, 2)
        igual.addWidget(QPushButton("+"), 1, 3)

        btn_igual = QPushButton("igual")
        btn_igual.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        igual.addWidget(btn_igual, 0, 4, 2, 1)

        caja.addLayout(pantalla, 2)
        caja.addLayout(colum1)
        caja.addLayout(colum2)
        caja.addLayout(colum3)
        caja.addLayout(igual)

        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = FiestaPrincipal()
    ventana.show()
    aplicacion.exec()