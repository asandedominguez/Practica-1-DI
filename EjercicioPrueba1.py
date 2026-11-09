import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QGridLayout,QHBoxLayout)
from PyQt6.QtGui import QColor,QPalette
from PyQt6.QtWidgets import QSizePolicy

class caixa_cor(QWidget):
    def __init__(self,cor):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)

class Layouts(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' Primero ejercicio ---->')
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        ventana = QVBoxLayout()

        pantalla = QHBoxLayout()
        self.color = caixa_cor("gray")
        pantalla_etiqueta = QLabel("Semaforo apagado")
        pantalla.addWidget(pantalla_etiqueta)

        layout_caja = QVBoxLayout(self.color)
        layout_caja.addWidget(pantalla_etiqueta)

        botones = QGridLayout()

        boton1 = QPushButton('Rojo')
        def boton_1():
            pantalla_etiqueta.setText('¡Alto!')
            paleta = QPalette()
            paleta.setColor(QPalette.ColorRole.Window, QColor("red"))
            self.color.setPalette(paleta)
        boton1.clicked.connect(boton_1)

        boton2 = QPushButton('Amarillo')
        def boton_2():
            paleta = QPalette()
            paleta.setColor(QPalette.ColorRole.Window, QColor("yellow"))
            self.color.setPalette(paleta)
        boton2.clicked.connect(boton_2)

        boton3 = QPushButton('Verde')
        def boton_3():
            pantalla_etiqueta.setText('Puede pasar sin problema')
            paleta = QPalette()
            paleta.setColor(QPalette.ColorRole.Window, QColor("green"))
            self.color.setPalette(paleta)
        boton3.clicked.connect(boton_3)


        botones.addWidget(boton1,0,0)
        botones.addWidget(boton2,0,1)
        botones.addWidget(boton3,0,2)

        ventana.addWidget(self.color)
        ventana.addLayout(botones)

        contenedor = QWidget()
        contenedor.setLayout(ventana)
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = Layouts()
    ventana.show()
    aplicacion.exec()

