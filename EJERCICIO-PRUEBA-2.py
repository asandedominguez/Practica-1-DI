# NOTA = • Si el objeto es un diseño (QHBoxLayout, QVBoxLayout, QGridLayout, etc.) → usa .addLayout().
# • Si el objeto es un componente visual (QPushButton, QLabel, QWidget, etc.) → usa .addWidget().



import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton,
    QWidget, QLineEdit, QGridLayout, QSizePolicy
)

# ==============================================================================
# 1. CLASE DE LA VENTANA PRINCIPAL
# ==============================================================================
class ConversorMultifuncion(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle("Conversor Multifunción")  # Título de la barra superior
        self.setMinimumSize(360, 320)  # Tamaño mínimo permitido

        # Layout principal vertical: pondrá la pantalla arriba y el teclado abajo
        caja_principal = QVBoxLayout()

        # --- ZONA SUPERIOR: Pantalla numérica ---
        self.entrada = QLineEdit()  # Campo de texto donde se ven números y resultados
        self.entrada.setPlaceholderText("Ingresar número")  # Texto guía en gris
        # Aplicamos estilo CSS (QSS) para agrandar la letra y dar margen interno
        self.entrada.setStyleSheet("font-size: 18px; padding: 6px;")
        caja_principal.addWidget(self.entrada)

        # --- ZONA INFERIOR: Cuadrícula de botones (QGridLayout) ---
        # Permite organizar elementos en filas y columnas como una tabla
        teclado = QGridLayout()

        # Botones de borrado
        btn_borrar_uno = QPushButton("⌫")
        btn_borrar_uno.clicked.connect(self.on_borrar_uno_clicked)

        btn_ce = QPushButton("CE")
        btn_ce.clicked.connect(self.on_ce_clicked)

        # Creación y conexión de los botones numéricos del 0 al 9
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

        # Botón para decimales
        btn_punto = QPushButton(".")
        btn_punto.clicked.connect(self.on_punto_clicked)

        # Botones de operaciones de conversión (columna derecha)
        btn_cf = QPushButton("°C -> °F")
        btn_cf.clicked.connect(self.on_celsius_fahrenheit_clicked)

        btn_ck = QPushButton("°C -> K")
        btn_ck.clicked.connect(self.on_celsius_kelvin_clicked)

        btn_ed = QPushButton("€ -> $")
        btn_ed.clicked.connect(self.on_euros_dolares_clicked)

        # Botón Limpiar expandido (ocupará 2 filas de alto)
        btn_limpiar = QPushButton("Limpiar")
        # Expanding obliga al botón a estirarse todo lo posible en ancho y alto
        btn_limpiar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # Reutiliza el mismo método de borrado total que el botón CE
        btn_limpiar.clicked.connect(self.on_ce_clicked)

        # --- POSICIONAMIENTO EN LA REJILLA ---
        # Sintaxis: addWidget(widget, fila, columna, filas_que_ocupa, columnas_que_ocupa)

        # Fila 0
        teclado.addWidget(btn_borrar_uno, 0, 0)
        teclado.addWidget(btn_ce, 0, 1, 1, 2)  # Fila 0, col 1: ocupa 1 fila y 2 columnas
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
        teclado.addWidget(btn_limpiar, 3, 3, 2, 1)  # Fila 3, col 3: ocupa 2 filas y 1 columna

        teclado.addWidget(btn_0, 4, 0, 1, 2)  # Fila 4, col 0: ocupa 1 fila y 2 columnas
        teclado.addWidget(btn_punto, 4, 2)

        # --- ENSAMBLAJE FINAL ---
        caja_principal.addLayout(teclado)  # Añadimos la cuadrícula debajo de la pantalla

        # Contenedor central obligatorio para QMainWindow
        contenedor = QWidget()
        contenedor.setLayout(caja_principal)
        self.setCentralWidget(contenedor)

    # ==========================================================================
    # 2. MÉTODOS DE BORRADO
    # ==========================================================================
    def on_borrar_uno_clicked(self):
        texto = self.entrada.text()
        # Slicing [:-1]: toma toda la cadena excepto el último carácter
        self.entrada.setText(texto[:-1])

    def on_ce_clicked(self):
        # Vacía por completo el contenido del QLineEdit
        self.entrada.clear()

    # ==========================================================================
    # 3. MÉTODOS NUMÉRICOS (Concatenan el dígito al texto existente)
    # ==========================================================================
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
        # Evita escribir más de un punto decimal en el mismo número
        if "." not in self.entrada.text():
            self.entrada.setText(self.entrada.text() + ".")

    # ==========================================================================
    # 4. MÉTODOS DE CONVERSIÓN (Con control de errores)
    # ==========================================================================
    def on_celsius_fahrenheit_clicked(self):
        try:
            # Convertimos el texto a número decimal (float)
            valor = float(self.entrada.text())
            resultado = (valor * 9 / 5) + 32
            # Redondeamos a 2 decimales y devolvemos como texto a la pantalla
            self.entrada.setText(str(round(resultado, 2)))
        except ValueError:
            # Si la pantalla está vacía o tiene texto inválido (ej. "Error" o solo ".")
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


# ==============================================================================
# 5. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = ConversorMultifuncion()  # Crea nuestra ventana
    ventana.show()  # Muestra la ventana en pantalla
    sys.exit(aplicacion.exec())  # Inicia el bucle de eventos hasta cerrar