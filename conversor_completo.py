import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QGridLayout, QHBoxLayout)

class ConversorExpress(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Conversor Express')
        self.setMinimumSize(350, 300)

        caja_principal = QVBoxLayout()

        # Usaremos solo 'self.entrada' como pantalla única para evitar confusiones
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText('Ingresar numero')
        self.entrada.setStyleSheet("font-size: 18px; padding: 5px;")

        teclado = QGridLayout()

        # Botón Borrar uno (⌫)
        btn1 = QPushButton(' ⌫ ')
        def borrar_B():
            texto = self.entrada.text()
            self.entrada.setText(texto[:-1]) # Borra el último carácter
        btn1.clicked.connect(borrar_B)

        # Botón Borrar Todo (CE)
        btn2 = QPushButton(' CE ')
        def borrar_CE():
            self.entrada.setText("")
        btn2.clicked.connect(borrar_CE)

        # Botones numéricos (modificados para que escriban en self.entrada)
        btn3 = QPushButton(' 1 ')
        def Boton3():
            self.entrada.setText(self.entrada.text() + "1")
        btn3.clicked.connect(Boton3)

        btn4 = QPushButton(' 2 ')
        def Boton4():
            self.entrada.setText(self.entrada.text() + "2")
        btn4.clicked.connect(Boton4)

        btn5 = QPushButton(' 3 ')
        def Boton5():
            self.entrada.setText(self.entrada.text() + "3")
        btn5.clicked.connect(Boton5)

        btn6 = QPushButton(' 4 ')
        def Boton6():
            self.entrada.setText(self.entrada.text() + "4")
        btn6.clicked.connect(Boton6)

        btn7 = QPushButton(' 5 ')
        def Boton7():
            self.entrada.setText(self.entrada.text() + "5")
        btn7.clicked.connect(Boton7)

        btn8 = QPushButton(' 6 ')
        def Boton8():
            self.entrada.setText(self.entrada.text() + "6")
        btn8.clicked.connect(Boton8)

        btn9 = QPushButton(' 7 ')
        def Boton9():
            self.entrada.setText(self.entrada.text() + "7")
        btn9.clicked.connect(Boton9)

        btn10 = QPushButton(' 8 ')
        def Boton10():
            self.entrada.setText(self.entrada.text() + "8")
        btn10.clicked.connect(Boton10)

        btn11 = QPushButton(' 9 ')
        def Boton11():
            self.entrada.setText(self.entrada.text() + "9")
        btn11.clicked.connect(Boton11)

        # Botón de Punto/Coma decimal
        btn12 = QPushButton(' . ')
        def BotonComa():
            # Evitamos poner más de un punto decimal
            if "." not in self.entrada.text():
                self.entrada.setText(self.entrada.text() + ".")
        btn12.clicked.connect(BotonComa)

        # --- Lógica de conversión corregida (String -> Float -> String) ---
        boton13 = QPushButton(' € ➔ $ ')
        def Boton12():
            try:
                valor_string = self.entrada.text()
                valor_numerico = float(valor_string) # CONVERSIÓN A NÚMERO
                resultado = valor_numerico * 1.10
                self.entrada.setText(str(round(resultado, 2))) # REGRESO A STRING (Redondeado a 2 decimales)
            except ValueError:
                self.entrada.setText("Error")
        boton13.clicked.connect(Boton12)

        boton14 = QPushButton(' ºC ➔ ºF ')
        def Boton13():
            try:
                valor_string = self.entrada.text()
                valor_numerico = float(valor_string) # CONVERSIÓN A NÚMERO
                resultado = (valor_numerico * 9/5) + 32
                self.entrada.setText(str(round(resultado, 2))) # REGRESO A STRING
            except ValueError:
                self.entrada.setText("Error")
        boton14.clicked.connect(Boton13)

        # Posicionamiento en la rejilla
        teclado.addWidget(btn1,0,0)
        teclado.addWidget(btn2,0,1)
        teclado.addWidget(btn3,0,2)
        teclado.addWidget(btn4,1,0)
        teclado.addWidget(btn5,1,1)
        teclado.addWidget(btn6,1,2)
        teclado.addWidget(btn7,2,0)
        teclado.addWidget(btn8,2,1)
        teclado.addWidget(btn9,2,2)
        teclado.addWidget(btn10,3,0)
        teclado.addWidget(btn11,3,1)
        teclado.addWidget(btn12,3,2)
        teclado.addWidget(boton13,4,0,1,2) # Expandido para ocupar 2 columnas
        teclado.addWidget(boton14,4,2)

        caja_principal.addWidget(self.entrada)
        caja_principal.addLayout(teclado)

        contenedor = QWidget()
        contenedor.setLayout(caja_principal)
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = ConversorExpress()
    ventana.show()
    aplicacion.exec()
