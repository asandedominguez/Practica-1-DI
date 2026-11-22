import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QRadioButton, QCheckBox,
    QPushButton, QMessageBox
)


# ==============================================================================
# 1. CLASE DE LA VENTANA PRINCIPAL
# ==============================================================================
class FormularioEvento(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle("Inscripción a Evento Tecnológico")  # Título de la barra superior
        self.setMinimumSize(380, 460)  # Tamaño mínimo permitido

        # Layout principal vertical: apila todos los campos del formulario de arriba abajo
        layout_principal = QVBoxLayout()

        # --- SECCIÓN 1: Campos de entrada de texto ---
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

        # Añadimos cada etiqueta y su caja de texto correspondiente al layout vertical
        layout_principal.addWidget(lbl_nombre)
        layout_principal.addWidget(self.txt_nombre)
        layout_principal.addWidget(lbl_email)
        layout_principal.addWidget(self.txt_email)
        layout_principal.addWidget(lbl_password)
        layout_principal.addWidget(self.txt_password)
        layout_principal.addWidget(lbl_entradas)
        layout_principal.addWidget(self.txt_entradas)

        # --- SECCIÓN 2: Menú desplegable (QComboBox) ---
        lbl_pase = QLabel("Tipo de pase:")
        self.cmb_pase = QComboBox()  # Lista desplegable de selección única
        self.cmb_pase.addItems(["Estudiante", "Profesional", "VIP"])  # Rellena las opciones

        layout_principal.addWidget(lbl_pase)
        layout_principal.addWidget(self.cmb_pase)

        # --- SECCIÓN 3: Botones de opción excluyentes (QRadioButton) ---
        lbl_modalidad = QLabel("Modalidad:")
        layout_modalidad = QHBoxLayout()  # Sub-layout horizontal para ponerlos lado a lado

        self.rbt_presencial = QRadioButton("Presencial")
        self.rbt_online = QRadioButton("Online")
        self.rbt_presencial.setChecked(True)  # Marca "Presencial" como opción por defecto

        # Al estar dentro del mismo contenedor/layout, PyQt garantiza que solo uno pueda marcarse
        layout_modalidad.addWidget(self.rbt_presencial)
        layout_modalidad.addWidget(self.rbt_online)

        layout_principal.addWidget(lbl_modalidad)
        layout_principal.addLayout(layout_modalidad)  # Anidamos la fila horizontal en el vertical

        # --- SECCIÓN 4: Casilla de verificación y botón de envío ---
        self.chk_condiciones = QCheckBox("Acepto los términos y condiciones")
        layout_principal.addWidget(self.chk_condiciones)

        self.btn_confirmar = QPushButton("Confirmar inscripción")
        # Conectamos el clic del botón al método que valida y procesa todo el formulario
        self.btn_confirmar.clicked.connect(self.validar_inscripcion)
        layout_principal.addWidget(self.btn_confirmar)

        # --- ENSAMBLAJE FINAL ---
        # Contenedor central obligatorio para QMainWindow
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

    # ==========================================================================
    # 2. MÉTODO DE VALIDACIÓN Y CÁLCULO (SLOT)
    # ==========================================================================
    def validar_inscripcion(self):
        # Recogemos todos los valores actuales del formulario (.strip() limpia espacios extra)
        nombre = self.txt_nombre.text().strip()
        email = self.txt_email.text().strip()
        password = self.txt_password.text().strip()
        entradas_texto = self.txt_entradas.text().strip()
        pase = self.cmb_pase.currentText()  # Obtiene el texto de la opción elegida en el desplegable

        # Paso 1: Verificar que ningún campo de texto esté vacío
        if not nombre or not email or not password or not entradas_texto:
            # Muestra una ventana emergente de advertencia y detiene la función (return)
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Paso 2: Validar estructura mínima de correo electrónico
        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Error", "El email debe contener '@' y '.'.")
            return

        # Paso 3: Comprobar longitud mínima de seguridad en la contraseña
        if len(password) < 6:
            QMessageBox.warning(self, "Error", "La contraseña debe tener al menos 6 caracteres.")
            return

        # Paso 4: Validar que las entradas sean un número entero positivo
        try:
            num_entradas = int(entradas_texto)  # Intenta convertir texto a entero
            if num_entradas <= 0:
                QMessageBox.warning(self, "Error", "El número de entradas debe ser mayor que 0.")
                return
        except ValueError:
            # Salta si el usuario escribió letras o decimales (ej. "dos" o "2.5")
            QMessageBox.warning(self, "Error", "El número de entradas debe ser un número entero válido.")
            return

        # Paso 5: Verificar que el QCheckBox esté marcado
        if not self.chk_condiciones.isChecked():
            QMessageBox.warning(self, "Error", "Debes aceptar los términos y condiciones.")
            return

        # Paso 6: Asignar tarifa unitaria según el pase y calcular el importe total
        if pase == "Estudiante":
            precio_unitario = 20
        elif pase == "Profesional":
            precio_unitario = 50
        else:  # VIP
            precio_unitario = 100

        total = num_entradas * precio_unitario
        # Operador ternario: asigna "Presencial" si ese radio button está marcado; si no, "Online"
        modalidad = "Presencial" if self.rbt_presencial.isChecked() else "Online"

        # Paso 7: Construir el resumen multilínea y mostrarlo en una ventana informativa
        mensaje = (
            f"Inscripción confirmada para {nombre} ({email}).\n"
            f"Pase: {pase} | Modalidad: {modalidad}\n"
            f"Entradas: {num_entradas} x {precio_unitario}€\n"
            f"Total a pagar: {total}€"
        )
        QMessageBox.information(self, "Inscripción Completada", mensaje)


# ==============================================================================
# 3. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = FormularioEvento()  # Crea nuestra ventana
    ventana.show()  # Muestra la ventana en pantalla
    sys.exit(aplicacion.exec())  # Inicia el bucle de eventos hasta cerrar