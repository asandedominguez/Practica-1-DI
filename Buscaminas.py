import sys
import random
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QGridLayout, QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QSizePolicy


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
        pantalla_etiqueta = QLabel("Buscaminas")
        pantalla.addWidget(pantalla_etiqueta)

        teclado = QGridLayout()

        # Posiciones de las minas (3 minas aleatorias)
        minas = random.sample(range(9), 3)

        btn1 = QPushButton(' ')
        def click_b1():
            if 0 in minas:
                btn1.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn1.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn1.clicked.connect(click_b1)

        btn2 = QPushButton(' ')
        def click_b2():
            if 1 in minas:
                btn2.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn2.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn2.clicked.connect(click_b2)

        btn3 = QPushButton(' ')
        def click_b3():
            if 2 in minas:
                btn3.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn3.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn3.clicked.connect(click_b3)

        btn4 = QPushButton(' ')
        def click_b4():
            if 3 in minas:
                btn4.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn4.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn4.clicked.connect(click_b4)

        btn5 = QPushButton(' ')
        def click_b5():
            if 4 in minas:
                btn5.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn5.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn5.clicked.connect(click_b5)

        btn6 = QPushButton(' ')
        def click_b6():
            if 5 in minas:
                btn6.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn6.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn6.clicked.connect(click_b6)

        btn7 = QPushButton(' ')
        def click_b7():
            if 6 in minas:
                btn7.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn7.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn7.clicked.connect(click_b7)

        btn8 = QPushButton(' ')
        def click_b8():
            if 7 in minas:
                btn8.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn8.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn8.clicked.connect(click_b8)

        btn9 = QPushButton(' ')
        def click_b9():
            if 8 in minas:
                btn9.setText("💣")
                pantalla_etiqueta.setText("¡Boom! Perdiste")
            else:
                btn9.setText("1")
                pantalla_etiqueta.setText("¡Salvado!")
        btn9.clicked.connect(click_b9)

        teclado.addWidget(btn1, 0, 0)
        teclado.addWidget(btn2, 0, 1)
        teclado.addWidget(btn3, 0, 2)
        teclado.addWidget(btn4, 1, 0)
        teclado.addWidget(btn5, 1, 1)
        teclado.addWidget(btn6, 1, 2)
        teclado.addWidget(btn7, 2, 0)
        teclado.addWidget(btn8, 2, 1)
        teclado.addWidget(btn9, 2, 2)

        caja.addLayout(pantalla)
        caja.addLayout(teclado)

        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = FiestaPrincipal()
    ventana.show()
    aplicacion.exec()