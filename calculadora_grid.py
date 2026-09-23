import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton,QGridLayout ,QWidget, QLabel, QLineEdit )
from PyQt6.QtGui import QColor,QPalette



class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(' calvo ---->')
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        maia = QGridLayout()
        btn1 = QPushButton(' holi ')
        btn2 = QPushButton(' holi')
        btn3 = QPushButton(' holi')
        btn4 = QPushButton(' holi')


        maia.addWidget(btn1)
        maia.addWidget(btn2,0,1,1,2)
        maia.addWidget(btn3,1,0,2,1)
        maia.addWidget(btn4,1,1,1,2)


        contenedor = QWidget()
        contenedor.setLayout(maia)
        self.setCentralWidget(contenedor)
        self.show()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiesta = FiestaPrincipal()
    aplicacion.exec()