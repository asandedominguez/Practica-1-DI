import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLabel, QComboBox, QLineEdit, QCheckBox,
                             QPushButton, QMessageBox)


class Alquiler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reserva de Vehículos")
        self.setMinimumSize(350, 450)

        ventana = QVBoxLayout()

        # ----------------------------------------------------------------------
        # CAMPOS DE ENTRADA (Etiqueta + Campo)
        # ----------------------------------------------------------------------
        nombre = QLabel("Nombre")
        self.c_nombre = QLineEdit()
        self.c_nombre.setPlaceholderText("Dame tu nombre")

        dni = QLabel("DNI")
        self.c_dni = QLineEdit()  # Corrección 1: Nombre unificado como self.c_dni
        self.c_dni.setPlaceholderText("Dame tu DNI")

        dias = QLabel("Días")
        self.c_dias = QLineEdit()
        self.c_dias.setPlaceholderText("Dime cuántos días te quedas")

        # Añadimos alternadamente para mantener la coherencia visual
        ventana.addWidget(nombre)
        ventana.addWidget(self.c_nombre)
        ventana.addWidget(dni)
        ventana.addWidget(self.c_dni)
        ventana.addWidget(dias)
        ventana.addWidget(self.c_dias)

        # ----------------------------------------------------------------------
        # DESPLEGABLE DE PLANES
        # ----------------------------------------------------------------------
        plan = QLabel("Plan")
        self.desplegable = QComboBox()
        self.desplegable.addItems(["Económico", "Suv", "Premium"])

        ventana.addWidget(plan)
        ventana.addWidget(self.desplegable)

        # ----------------------------------------------------------------------
        # EXTRAS
        # ----------------------------------------------------------------------
        self.seguro = QCheckBox("Seguro a todo riesgo")
        self.conductor = QCheckBox("Conductor adicional")

        ventana.addWidget(self.seguro)
        ventana.addWidget(self.conductor)

        # ----------------------------------------------------------------------
        # BOTÓN CONFIRMAR
        # ----------------------------------------------------------------------
        self.confirmar = QPushButton("Confirmar reserva")
        ventana.addWidget(self.confirmar)

        contenedor = QWidget()
        contenedor.setLayout(ventana)
        self.setCentralWidget(contenedor)

        self.confirmar.clicked.connect(self.validarReserva)

    def validarReserva(self):
        nombre = self.c_nombre.text().strip()
        dni = self.c_dni.text().strip()
        dias_texto = self.c_dias.text().strip()
        plan = self.desplegable.currentText()

        # 1. Validar campos vacíos
        if not nombre or not dni or not dias_texto:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # 2. Validar que los días sean un número entero válido > 0
        try:
            dias_num = int(dias_texto)
            if dias_num <= 0:
                QMessageBox.warning(self, "Error", "Los días deben ser un número mayor a 0.")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "Los días deben ser un número entero válido.")
            return

        # 3. Determinar precio base por día según la categoría elegida
        if plan == "Económico":
            precio_dia = 30
        elif plan == "Suv":
            precio_dia = 50
        else:  # Premium
            precio_dia = 80

        # 4. Calcular el total
        total = dias_num * precio_dia

        # 5. Mostrar resumen de la reserva
        mensaje = (
            f"Reserva confirmada para {nombre} ({dni}).\n"
            f"Categoría: {plan} ({dias_num} días).\n"
            f"Total a pagar: {total}€"
        )
        QMessageBox.information(self, "Éxito", mensaje)


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = Alquiler()
    ventana.show()
    aplicacion.exec()