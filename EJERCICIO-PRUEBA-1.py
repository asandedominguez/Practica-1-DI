import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton,
    QWidget, QLabel, QLineEdit, QHBoxLayout
)
from PyQt6.QtGui import QColor, QPalette


# ==============================================================================
# 1. CLASE AUXILIAR PARA EL PANEL DE COLOR
# ==============================================================================
class PanelColor(QWidget):
    """Widget personalizado que actúa como un recuadro con color de fondo sólido."""

    def __init__(self, cor):
        super().__init__()  # Inicializa la clase padre (QWidget)

        # Obliga al widget a pintar su propio fondo (por defecto son transparentes)
        self.setAutoFillBackground(True)

        # Creamos una paleta de colores y asignamos el color recibido al rol 'Window' (fondo)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)


# ==============================================================================
# 2. CLASE DE LA VENTANA PRINCIPAL
# ==============================================================================
class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle('Panel de Estado')  # Título en la barra superior
        self.setMinimumSize(400, 220)  # Tamaño mínimo al redimensionar (ancho, alto)
        self.setMaximumSize(600, 400)  # Tamaño máximo permitido

        # Layout principal que dividirá la ventana en dos zonas (arriba y abajo)
        caja = QVBoxLayout()

        # --- ZONA SUPERIOR: Panel de estado ---
        self.color = PanelColor("gray")  # Instanciamos nuestro panel en color gris inicial
        self.pantalla_etiqueta = QLabel("Sistema en espera")  # Texto inicial
        # Centramos el texto tanto horizontal como verticalmente dentro de la etiqueta
        self.pantalla_etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Creamos un layout dentro del panel gris y metemos la etiqueta en él
        layout_panel = QVBoxLayout(self.color)
        layout_panel.addWidget(self.pantalla_etiqueta)

        # --- ZONA INFERIOR: Controles de entrada ---
        fila_inferior = QHBoxLayout()  # Organizará el cuadro de texto y botones en fila

        self.texto = QLineEdit()  # Campo donde el usuario escribe
        self.texto.setPlaceholderText("Introduce un mensaje...")  # Texto guía en gris claro

        # Creación de los tres botones
        boton1 = QPushButton("Activo")
        boton2 = QPushButton("Alerta")
        boton3 = QPushButton("Crítico")

        # --- CONEXIÓN DE SEÑALES Y SLOTS (Eventos) ---
        # Cuando se hace clic ('clicked'), se ejecuta ('connect') el método indicado
        boton1.clicked.connect(self.on_activo_clicked)
        boton2.clicked.connect(self.on_alerta_clicked)
        boton3.clicked.connect(self.on_critico_clicked)

        # Añadimos los controles a la fila horizontal (de izquierda a derecha)
        fila_inferior.addWidget(self.texto)
        fila_inferior.addWidget(boton1)
        fila_inferior.addWidget(boton2)
        fila_inferior.addWidget(boton3)

        # --- ENSAMBLAJE FINAL DE LA INTERFAZ ---
        caja.addWidget(self.color)  # Arriba: el panel de color
        caja.addLayout(fila_inferior)  # Abajo: la fila con el input y los botones

        # QMainWindow necesita un widget central único para contener todo el diseño
        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)

    # ==========================================================================
    # 3. MÉTODOS DE RESPUESTA A LOS BOTONES (SLOTS)
    # ==========================================================================
    def on_activo_clicked(self):
        # Obtenemos el texto del QLineEdit y quitamos espacios sobrantes (.strip())
        mensaje = self.texto.text().strip()

        # Validación: si el campo está vacío, avisamos y detenemos la función (return)
        if not mensaje:
            self.pantalla_etiqueta.setText("Por favor, introduce un mensaje")
            return

        # Actualizamos el texto y cambiamos el color del panel superior a verde
        self.pantalla_etiqueta.setText("Activo: " + mensaje)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("green"))
        self.color.setPalette(paleta)

    def on_alerta_clicked(self):
        mensaje = self.texto.text().strip()
        if not mensaje:
            self.pantalla_etiqueta.setText("Por favor, introduce un mensaje")
            return

        # Actualizamos el texto y cambiamos el color a amarillo
        self.pantalla_etiqueta.setText("¡Alerta!: " + mensaje)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("yellow"))
        self.color.setPalette(paleta)

    def on_critico_clicked(self):
        mensaje = self.texto.text().strip()
        if not mensaje:
            self.pantalla_etiqueta.setText("Por favor, introduce un mensaje")
            return

        # Actualizamos el texto y cambiamos el color a rojo
        self.pantalla_etiqueta.setText("¡Crítico!: " + mensaje)
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("red"))
        self.color.setPalette(paleta)


# ==============================================================================
# 4. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = FiestaPrincipal()  # Crea nuestra ventana
    ventana.show()  # La hace visible en pantalla

    # Inicia el bucle infinito que escucha clics y teclas hasta cerrar la ventana.
    # NOTA: En tu código original decía 'app.exec()', debe ser 'aplicacion.exec()'
    sys.exit(aplicacion.exec())