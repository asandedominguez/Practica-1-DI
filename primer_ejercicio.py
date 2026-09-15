import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A miña primeira aplicacion Qt")
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1800, 1600)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    app.exec()

