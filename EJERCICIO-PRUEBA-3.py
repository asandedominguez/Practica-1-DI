import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QRadioButton, QCheckBox,
    QPushButton, QMessageBox
)


class FormularioEvento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inscripción a Evento Tecnológico")
        self.setMinimumSize(380, 460)

        layout_principal = QVBoxLayout()

        # 1. Campos de texto con sus etiquetas (QVBoxLayout)
        lbl_nombre = QLabel("Nombre:")
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Introduce tu nombre completo")

        lbl_email = QLabel("Email:")
        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("ejemplo@correo.com")

        lbl_password = QLabel("Contraseña:")
        self.txt_password = QLineEdit()
        self.txt_password.setPlaceholderText("Mínimo 6 caracteres")

        lbl_entradas = QLabel("Nº de entradas:")
        self.txt_entradas = QLineEdit()
        self.txt_entradas.setPlaceholderText("Ej: 2")

        layout_principal.addWidget(lbl_nombre)
        layout_principal.addWidget(self.txt_nombre)
        layout_principal.addWidget(lbl_email)
        layout_principal.addWidget(self.txt_email)
        layout_principal.addWidget(lbl_password)
        layout_principal.addWidget(self.txt_password)
        layout_principal.addWidget(lbl_entradas)
        layout_principal.addWidget(self.txt_entradas)

        # 2. Desplegable de tipo de pase (QComboBox)
        lbl_pase = QLabel("Tipo de pase:")
        self.cmb_pase = QComboBox()
        self.cmb_pase.addItems(["Estudiante", "Profesional", "VIP"])

        layout_principal.addWidget(lbl_pase)
        layout_principal.addWidget(self.cmb_pase)

        # 3. Grupo horizontal de QRadioButton para modalidad
        lbl_modalidad = QLabel("Modalidad:")
        layout_modalidad = QHBoxLayout()
        self.rbt_presencial = QRadioButton("Presencial")
        self.rbt_online = QRadioButton("Online")
        self.rbt_presencial.setChecked(True)
        layout_modalidad.addWidget(self.rbt_presencial)
        layout_modalidad.addWidget(self.rbt_online)

        layout_principal.addWidget(lbl_modalidad)
        layout_principal.addLayout(layout_modalidad)

        # 4. Checkbox de condiciones y botón de envío
        self.chk_condiciones = QCheckBox("Acepto los términos y condiciones")
        layout_principal.addWidget(self.chk_condiciones)

        self.btn_confirmar = QPushButton("Confirmar inscripción")
        self.btn_confirmar.clicked.connect(self.validar_inscripcion)
        layout_principal.addWidget(self.btn_confirmar)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

    def validar_inscripcion(self):
        nombre = self.txt_nombre.text().strip()
        email = self.txt_email.text().strip()
        password = self.txt_password.text().strip()
        entradas_texto = self.txt_entradas.text().strip()
        pase = self.cmb_pase.currentText()

        # 1. Comprobar campos vacíos
        if not nombre or not email or not password or not entradas_texto:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # 2. Validar formato básico de email
        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Error", "El email debe contener '@' y '.'.")
            return

        # 3. Validar longitud de contraseña
        if len(password) < 6:
            QMessageBox.warning(self, "Error", "La contraseña debe tener al menos 6 caracteres.")
            return

        # 4. Validar que las entradas sean un entero mayor que 0
        try:
            num_entradas = int(entradas_texto)
            if num_entradas <= 0:
                QMessageBox.warning(self, "Error", "El número de entradas debe ser mayor que 0.")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "El número de entradas debe ser un número entero válido.")
            return

        # 5. Comprobar aceptación de condiciones
        if not self.chk_condiciones.isChecked():
            QMessageBox.warning(self, "Error", "Debes aceptar los términos y condiciones.")
            return

        # 6. Calcular precio según tipo de pase
        if pase == "Estudiante":
            precio_unitario = 20
        elif pase == "Profesional":
            precio_unitario = 50
        else:  # VIP
            precio_unitario = 100

        total = num_entradas * precio_unitario
        modalidad = "Presencial" if self.rbt_presencial.isChecked() else "Online"

        # 7. Mostrar resumen de confirmación
        mensaje = (
            f"Inscripción confirmada para {nombre} ({email}).\n"
            f"Pase: {pase} | Modalidad: {modalidad}\n"
            f"Entradas: {num_entradas} x {precio_unitario}€\n"
            f"Total a pagar: {total}€"
        )
        QMessageBox.information(self, "Inscripción Completada", mensaje)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = FormularioEvento()
    ventana.show()
    sys.exit(aplicacion.exec())