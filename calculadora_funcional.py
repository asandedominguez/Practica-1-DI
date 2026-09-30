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


class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(' calvo ---->')
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,400)

        caja = QVBoxLayout()


        pantalla = QHBoxLayout()
        pantalla_etiqueta = QLabel()
        pantalla.addWidget(pantalla_etiqueta)

        teclado = QGridLayout()
        btn1 = QPushButton(' ⌫ ')   # (' ⌫ ')

        def borrar_B():
            pantalla_etiqueta.setText("")
        btn1.clicked.connect(borrar_B)

        btn2 = QPushButton("7")
        def N7_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "7")
        btn2.clicked.connect(N7_B)

        btn3 = QPushButton(' 4')
        def N4_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "4")
        btn3.clicked.connect(N4_B)

        btn4 = QPushButton(' 1')
        def N1_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "1")
        btn4.clicked.connect(N1_B)


        btn5 = QPushButton(' 0')
        def N0_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "0")
        btn5.clicked.connect(N0_B)




        btn6 = QPushButton(' (')
        btn7 = QPushButton(' 8')
        btn8 = QPushButton(' 5')
        btn9 = QPushButton(' 2')
        btn10 = QPushButton(' ,')

        btn11 = QPushButton(' )')
        btn12 = QPushButton(' 9')
        btn13 = QPushButton(' 6')
        btn14 = QPushButton(' 3')
        btn15 = QPushButton(' %')

        btn16 = QPushButton(' mod')
        btn17 = QPushButton(' /')
        btn18 = QPushButton(' x')
        btn19 = QPushButton(' -')
        btn20 = QPushButton(' +')

        btn21 = QPushButton(' π')
        btn22 = QPushButton(' √')
        btn23 = QPushButton(' x²')
        btn24 = QPushButton(' =')



        btn24.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        teclado.addWidget(btn1,0,0)
        teclado.addWidget(btn2,1,0)
        teclado.addWidget(btn3,2,0)
        teclado.addWidget(btn4,3,0)
        teclado.addWidget(btn5,4,0)

        teclado.addWidget(btn6,0,1)
        teclado.addWidget(btn7,1,1)
        teclado.addWidget(btn8,2,1)
        teclado.addWidget(btn9,3,1)
        teclado.addWidget(btn10,4,1)

        teclado.addWidget(btn11,0,2)
        teclado.addWidget(btn12,1,2)
        teclado.addWidget(btn13,2,2)
        teclado.addWidget(btn14,3,2)
        teclado.addWidget(btn15,4,2)

        teclado.addWidget(btn16,0,3)
        teclado.addWidget(btn17,1,3)
        teclado.addWidget(btn18,2,3)
        teclado.addWidget(btn19,3,3)
        teclado.addWidget(btn20,4,3)

        teclado.addWidget(btn21,0,4)
        teclado.addWidget(btn22,1,4)
        teclado.addWidget(btn23,2,4)
        teclado.addWidget(btn24,3,4,2,1)





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