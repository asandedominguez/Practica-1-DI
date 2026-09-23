import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout)
from PyQt6.QtGui import QColor,QPalette


class caixa_cor(QWidget):
    def __init__(self,cor):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)


class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(' calvo ---->')
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,400)

        caja = QVBoxLayout()


        pantalla = QHBoxLayout()
        pantalla.addWidget(caixa_cor("red"))

        colum1 = QHBoxLayout()

        colum1.addWidget(QPushButton("hola"))
        colum1.addWidget(QPushButton("hola"))
        colum1.addWidget(QPushButton("hola"))
        colum1.addWidget(QPushButton("hola"))


        colum2 = QHBoxLayout()
        colum2.addWidget(QPushButton("hola"))
        colum2.addWidget(QPushButton("hola"))
        colum2.addWidget(QPushButton("hola"))
        colum2.addWidget(QPushButton("hola"))

        colum3 = QHBoxLayout()
        colum3.addWidget(QPushButton("hola"))
        colum3.addWidget(QPushButton("hola"))
        colum3.addWidget(QPushButton("hola"))
        colum3.addWidget(QPushButton("hola"))

        colum4 = QHBoxLayout()
        colum4.addWidget(QPushButton("hola"))
        colum4.addWidget(QPushButton("hola"))
        colum4.addWidget(QPushButton("hola"))
        colum4.addWidget(QPushButton("hola"))


        colum5 = QHBoxLayout()
        colum5.addWidget(QPushButton("hola"))
        colum5.addWidget(QPushButton("hola"))
        colum5.addWidget(QPushButton("hola"))
        colum5.addWidget(QPushButton("hola"))

        caja.addLayout(pantalla)
        caja.addLayout(colum1)
        caja.addLayout(colum2)
        caja.addLayout(colum3)
        caja.addLayout(colum4)
        caja.addLayout(colum5)

        caja.addLayout(pantalla, 2)  # La pantalla ocupa 2 partes de alto



        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)




if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = FiestaPrincipal()
    ventana.show()
    aplicacion.exec()