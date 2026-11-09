import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QCheckBox, QStackedLayout, QHBoxLayout, QPushButton


class CalculadoraTemperatura(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de temperaturas")
        self.setMinimumSize(300, 200)

        ventana = QVBoxLayout()

        self.temperatutaC = QLineEdit()
        self.temperatutaC.setPlaceholderText("Dame la temperatura en grados Cº")

        self.resultado = QLabel("Resultado en Farenheit")

        self.temperatutaF = QLabel("Resultado en Kelvin")

        ventana.addWidget(self.temperatutaC)
        ventana.addWidget(self.temperatutaF)
        ventana.addWidget(self.resultado)

        botones = QHBoxLayout()

        calcular = QPushButton("Calcular")
        limpiar = QPushButton("Limpiar")

        botones.addWidget(calcular)
        botones.addWidget(limpiar)
        ventana.addLayout(botones)

        contenedor = QWidget()
        contenedor.setLayout(ventana)
        self.setCentralWidget(contenedor)

        calcular.clicked.connect(self.calcularF)
        calcular.clicked.connect(self.calcularK)
        limpiar.clicked.connect(self.limpiar)

    def calcularF(self):
        t = self.temperatutaC.text()
        try:
            f = float(t)
            self.resultado.setText(f"Resultado en Farenheit: {f * 1.8 +32}")
        except ValueError:
            self.resultado.setText("Error al realizar la conversión")

    def calcularK(self):
        t = self.temperatutaC.text()
        try:
            f = float(t)
            self.temperatutaF.setText(f"Resultado en Kelvin: {f + 273.15}")
        except ValueError:
            self.temperatutaF.setText("Error al realizar la conversión")

    def limpiar(self):
        self.temperatutaC.clear()
        self.temperatutaF.clear()
        self.resultado.setText("Resultado")
        self.temperatutaF.setText("Resultado en Farenheit")


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = CalculadoraTemperatura()
    ventana.show()
    aplicacion.exec()

