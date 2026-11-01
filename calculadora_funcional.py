import sys
import math
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
        def N_par_izq():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "(")
        btn6.clicked.connect(N_par_izq)

        btn7 = QPushButton(' 8')
        def N8_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "8")
        btn7.clicked.connect(N8_B)

        btn8 = QPushButton(' 5')
        def N5_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "5")
        btn8.clicked.connect(N5_B)

        btn9 = QPushButton(' 2')
        def N2_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "2")
        btn9.clicked.connect(N2_B)

        btn10 = QPushButton(' ,')
        def N_coma():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + ",")
        btn10.clicked.connect(N_coma)

        btn11 = QPushButton(' )')
        def N_par_der():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + ")")
        btn11.clicked.connect(N_par_der)

        btn12 = QPushButton(' 9')
        def N9_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "9")
        btn12.clicked.connect(N9_B)

        btn13 = QPushButton(' 6')
        def N6_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "6")
        btn13.clicked.connect(N6_B)

        btn14 = QPushButton(' 3')
        def N3_B():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "3")
        btn14.clicked.connect(N3_B)

        btn15 = QPushButton(' %')
        def N_porcentaje():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "%")
        btn15.clicked.connect(N_porcentaje)

        btn16 = QPushButton(' mod')
        def N_mod():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "%")
        btn16.clicked.connect(N_mod)

        btn17 = QPushButton(' /')
        def N_div():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "/")
        btn17.clicked.connect(N_div)

        btn18 = QPushButton(' x')
        def N_mult():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "x")
        btn18.clicked.connect(N_mult)

        btn19 = QPushButton(' -')
        def N_resta():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "-")
        btn19.clicked.connect(N_resta)

        btn20 = QPushButton(' +')
        def N_suma():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "+")
        btn20.clicked.connect(N_suma)

        btn21 = QPushButton(' π')
        def N_pi():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "π")
        btn21.clicked.connect(N_pi)

        btn22 = QPushButton(' √')
        def N_raiz():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "√(")
        btn22.clicked.connect(N_raiz)

        btn23 = QPushButton(' x²')
        def N_cuadrado():
            pantalla_etiqueta.setText(pantalla_etiqueta.text() + "**2")
        btn23.clicked.connect(N_cuadrado)

        btn24 = QPushButton(' =')

        def calcular():
            try:
                texto = pantalla_etiqueta.text().replace("x", "*").replace(",", ".").replace("π", str(math.pi)).replace("√", "math.sqrt")
                resultado = eval(texto)
                pantalla_etiqueta.setText(str(resultado))
            except Exception:
                pantalla_etiqueta.setText("Error")

        btn24.clicked.connect(calcular)

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