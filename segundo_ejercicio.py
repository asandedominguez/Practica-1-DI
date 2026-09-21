import \
    sys  # Importa el módulo del sistema para manejar los argumentos de la línea de comandos y la salida limpia de la app.
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel,
                             QLineEdit,
                             QHBoxLayout)  # Importa los componentes de la interfaz gráfica (widgets y layouts).
from PyQt6.QtGui import QColor, \
    QPalette  # Importa las clases necesarias para gestionar los colores y la paleta de la interfaz.

class CaixaCor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = QPalette()
        paleta.setColor (QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class FiestaPrincipal(QMainWindow):  # Define la clase de la ventana principal heredando de QMainWindow.
    def __init__(self):  # Método constructor que inicializa la clase.
        super().__init__()  # Llama al constructor de la clase padre (QMainWindow) para configurar correctamente el objeto.

        self.setWindowTitle('Prueba')  # Establece el título de la ventana como 'Prueba'.
        self.setMinimumSize(300, 200)  # Fija el tamaño mínimo que puede tener la ventana (300px de ancho por 200px de alto).
        self.setMaximumSize(500, 400)  # Fija el tamaño máximo que puede alcanzar la ventana (500px de ancho por 400px de alto).

        estructura = QHBoxLayout()

        columna1 = QVBoxLayout()
        contenedor = QWidget()  # Crea un widget genérico que servirá como base o contenedor principal.
        contenedor.setLayout()  # Asigna el diseño vertical 'caixaV' dentro del contenedor genérico.

        ventana = QWidget()
        estructura_vertical = QVBoxLayout(ventana)


        celda1 = QWidget();
        celda1.setStyleSheet("background-color: red;")
        celda2 = QWidget();
        celda2.setStyleSheet("background-color: green;")
        celda3 = QWidget();
        celda3.setStyleSheet("background-color: blue;")

        columna1.addWidget(celda1)
        columna1.addWidget(celda2)
        columna1.addWidget(celda3)

        estructura_vertical.addLayout(columna1)

        self.setCentralWidget(
            contenedor)  # Establece este contenedor como el widget central de la ventana principal (QMainWindow).

        self.show()  # Hace que la ventana sea visible en la pantalla.


if __name__ == '__main__':  # Comprueba si este script se está ejecutando directamente (y no importado como un módulo).
    aplicacion = QApplication(
        sys.argv)  # Crea la instancia principal de la aplicación PyQt, pasando los argumentos del sistema.
    fiesta = FiestaPrincipal()  # Crea una instancia de nuestra ventana personalizada, lo que ejecuta su constructor e inicia la interfaz.
    aplicacion.exec()  # Inicia el bucle de eventos de la aplicación (mantiene el programa abierto esperando interacciones del usuario).
