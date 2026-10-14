import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel,
                             QLineEdit, QComboBox, QStackedLayout, QGridLayout, QRadioButton)
from PyQt6.QtGui import QColor, QPalette


class FiestaPrincipal(QMainWindow):
    def __init__(self, cor):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)

        caja = QVBoxLayout()

        self.combTipo = QComboBox()
        self.combTipo.addItem("Alumno")
        self.combTipo.addItems(("Profesores", "Pas"))
        self.combTipo.setCurrentIndex(-1)
        self.combTipo.currentIndexChanged.connect(self.on_combTipo_currentIndexChanged)

        caja.addWidget(self.combTipo)

        tarxetas = QStackedLayout()

        mainalumno = QGridLayout()
        lblCiclos = QLabel("Ciclos")
        combCiclo = QComboBox()
        ciclos = ("DAM", "ASIR", "SMR", "IEA", "ADF")
        combCiclo.addItems(ciclos)
        combCiclo.setCurrentIndex(-1)

        rbtPrimeiro = QRadioButton("Primeiro")
        rbtSegundo = QRadioButton("Segundo")

        cmbAnoMatricula = QComboBox()
        cursoMatricula = ("25/26", "26/27", "27/28")
        cmbAnoMatricula.addItems(cursoMatricula)
        cmbAnoMatricula.setCurrentIndex(-1)

        lblNomeNai = QLabel("Nome Nai")
        txtNomeNai = QLineEdit()
        lblNomePai = QLabel("Nome Pai")
        txtNomePai = QLineEdit()

        mainalumno.addWidget(lblCiclos, 0, 0)
        mainalumno.addWidget(combCiclo, 0, 1)

        mainalumno.addWidget(rbtPrimeiro, 1, 0)
        mainalumno.addWidget(rbtSegundo, 1, 1)

        mainalumno.addWidget(QLabel("Ano Matrícula"), 2, 0)
        mainalumno.addWidget(cmbAnoMatricula, 2, 1)

        mainalumno.addWidget(lblNomeNai, 3, 0)
        mainalumno.addWidget(txtNomeNai, 3, 1)

        mainalumno.addWidget(lblNomePai, 4, 0)
        mainalumno.addWidget(txtNomePai, 4, 1)

        widgetAlumno = QWidget()
        widgetAlumno.setLayout(mainalumno)
        tarxetas.addWidget(widgetAlumno)

        caja.addLayout(tarxetas)

        container = QWidget()
        container.setLayout(caja)
        self.setCentralWidget(container)

    def on_combTipo_currentIndexChanged(self):
        self.tarxetas.setCurrentIndex(self.combTipo.currentIndex())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestaPrincipal("red")
    ventana.show()
    sys.exit(app.exec())