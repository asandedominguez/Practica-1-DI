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

        self.setWindowTitle(' calculadora ')
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,400)

        caja = QHBoxLayout()

        izquierda = QVBoxLayout()


        w_izq = QWidget()
        w_izq.setLayout(izquierda)

        centro = QHBoxLayout()
        centro.addWidget(caixa_cor("red"))

        w_centro = QWidget()
        w_centro.setLayout(centro)

        derecha = QVBoxLayout()
        derecha.addWidget(caixa_cor("red"))
        derecha.addWidget(caixa_cor("purple"))

        w_derc = QWidget()
        w_derc.setLayout(derecha)

        caja.addWidget(w_izq)
        caja.addWidget(w_centro)
        caja.addWidget(w_derc)


        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)









if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = FiestaPrincipal()
    ventana.show()
    aplicacion.exec()