import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton,
    QWidget, QLineEdit, QGridLayout, QSizePolicy
)


class ConversorMultifuncion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor Multifunción")
        self.setMinimumSize(360, 320)

        caja_principal = QVBoxLayout()

        # 1. Pantalla superior
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Ingresar número")
        self.entrada.setStyleSheet("font-size: 18px; padding: 6px;")
        caja_principal.addWidget(self.entrada)

        # 2. Cuadrícula de botones (QGridLayout)
        teclado = QGridLayout()

        # Fila 0: Borrado
        btn_borrar_uno = QPushButton("⌫")
        btn_borrar_uno.clicked.connect(self.on_borrar_uno_clicked)

        btn_ce = QPushButton("CE")
        btn_ce.clicked.connect(self.on_ce_clicked)

        # Botones numéricos del 0 al 9
        btn_0 = QPushButton("0")
        btn_0.clicked.connect(self.on_btn0_clicked)

        btn_1 = QPushButton("1")
        btn_1.clicked.connect(self.on_btn1_clicked)

        btn_2 = QPushButton("2")
        btn_2.clicked.connect(self.on_btn2_clicked)

        btn_3 = QPushButton("3")
        btn_3.clicked.connect(self.on_btn3_clicked)

        btn_4 = QPushButton("4")
        btn_4.clicked.connect(self.on_btn4_clicked)

        btn_5 = QPushButton("5")
        btn_5.clicked.connect(self.on_btn5_clicked)

        btn_6 = QPushButton("6")
        btn_6.clicked.connect(self.on_btn6_clicked)

        btn_7 = QPushButton("7")
        btn_7.clicked.connect(self.on_btn7_clicked)

        btn_8 = QPushButton("8")
        btn_8.clicked.connect(self.on_btn8_clicked)

        btn_9 = QPushButton("9")
        btn_9.clicked.connect(self.on_btn9_clicked)

        # Botón punto decimal
        btn_punto = QPushButton(".")
        btn_punto.clicked.connect(self.on_punto_clicked)

        # Botones de conversión (columna derecha)
        btn_cf = QPushButton("°C -> °F")
        btn_cf.clicked.connect(self.on_celsius_fahrenheit_clicked)

        btn_ck = QPushButton("°C -> K")
        btn_ck.clicked.connect(self.on_celsius_kelvin_clicked)

        btn_ed = QPushButton("€ -> $")
        btn_ed.clicked.connect(self.on_euros_dolares_clicked)

        # Botón Limpiar expandido (ocupa 2 filas)
        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn_limpiar.clicked.connect(self.on_ce_clicked)

        # 3. Posicionamiento en la rejilla (fila, columna, [rowSpan, colSpan])
        # Fila 0
        teclado.addWidget(btn_borrar_uno, 0, 0)
        teclado.addWidget(btn_ce, 0, 1, 1, 2)  # Ocupa 2 columnas
        teclado.addWidget(btn_cf, 0, 3)

        # Fila 1
        teclado.addWidget(btn_7, 1, 0)
        teclado.addWidget(btn_8, 1, 1)
        teclado.addWidget(btn_9, 1, 2)
        teclado.addWidget(btn_ck, 1, 3)

        # Fila 2
        teclado.addWidget(btn_4, 2, 0)
        teclado.addWidget(btn_5, 2, 1)
        teclado.addWidget(btn_6, 2, 2)
        teclado.addWidget(btn_ed, 2, 3)

        # Fila 3 y Fila 4
        teclado.addWidget(btn_1, 3, 0)
        teclado.addWidget(btn_2, 3, 1)
        teclado.addWidget(btn_3, 3, 2)
        teclado.addWidget(btn_limpiar, 3, 3, 2, 1)  # Ocupa filas 3 y 4 en la columna 3

        teclado.addWidget(btn_0, 4, 0, 1, 2)  # El 0 ocupa 2 columnas
        teclado.addWidget(btn_punto, 4, 2)

        caja_principal.addLayout(teclado)

        contenedor = QWidget()
        contenedor.setLayout(caja_principal)
        self.setCentralWidget(contenedor)

    # --- Métodos de borrado ---
    def on_borrar_uno_clicked(self):
        texto = self.entrada.text()
        self.entrada.setText(texto[:-1])

    def on_ce_clicked(self):
        self.entrada.clear()

    # --- Métodos numéricos ---
    def on_btn0_clicked(self):
        self.entrada.setText(self.entrada.text() + "0")

    def on_btn1_clicked(self):
        self.entrada.setText(self.entrada.text() + "1")

    def on_btn2_clicked(self):
        self.entrada.setText(self.entrada.text() + "2")

    def on_btn3_clicked(self):
        self.entrada.setText(self.entrada.text() + "3")

    def on_btn4_clicked(self):
        self.entrada.setText(self.entrada.text() + "4")

    def on_btn5_clicked(self):
        self.entrada.setText(self.entrada.text() + "5")

    def on_btn6_clicked(self):
        self.entrada.setText(self.entrada.text() + "6")

    def on_btn7_clicked(self):
        self.entrada.setText(self.entrada.text() + "7")

    def on_btn8_clicked(self):
        self.entrada.setText(self.entrada.text() + "8")

    def on_btn9_clicked(self):
        self.entrada.setText(self.entrada.text() + "9")

    def on_punto_clicked(self):
        if "." not in self.entrada.text():
            self.entrada.setText(self.entrada.text() + ".")

    # --- Métodos de conversión con captura de ValueError ---
    def on_celsius_fahrenheit_clicked(self):
        try:
            valor = float(self.entrada.text())
            resultado = (valor * 9 / 5) + 32
            self.entrada.setText(str(round(resultado, 2)))
        except ValueError:
            self.entrada.setText("Error")

    def on_celsius_kelvin_clicked(self):
        try:
            valor = float(self.entrada.text())
            resultado = valor + 273.15
            self.entrada.setText(str(round(resultado, 2)))
        except ValueError:
            self.entrada.setText("Error")

    def on_euros_dolares_clicked(self):
        try:
            valor = float(self.entrada.text())
            resultado = valor * 1.10
            self.entrada.setText(str(round(resultado, 2)))
        except ValueError:
            self.entrada.setText("Error")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = ConversorMultifuncion()
    ventana.show()
    sys.exit(aplicacion.exec())