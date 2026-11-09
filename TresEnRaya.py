import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout


class TresEnRaya(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('3 en Raya')
        self.setMinimumSize(300, 300)

        # Estado del juego: jugador actual ('X' u 'O')
        self.turno = 'X'

        # Layout principal vertical
        caja = QVBoxLayout()

        # Layout en cuadrícula de 3x3 para los botones del tablero
        tablero = QGridLayout()

        # Creamos la matriz de 3x3 botones
        for fila in range(3):
            for columna in range(3):
                btn = QPushButton("")
                btn.setMinimumSize(80, 80)
                # Al pulsar cualquier botón, ejecutamos la función marcar
                btn.clicked.connect(self.marcar)
                tablero.addWidget(btn, fila, columna)

        caja.addLayout(tablero)

        # Contenedor central
        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)

    def marcar(self):
        # Obtenemos el botón que ha sido pulsado
        btn = self.sender()

        # Si el botón no se ha marcado aún:
        if btn.text() == "":
            btn.setText(self.turno)
            # Alternamos el turno entre X y O
            if self.turno == 'X':
                self.turno = 'O'
            else:
                self.turno = 'X'


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = TresEnRaya()
    ventana.show()
    aplicacion.exec()