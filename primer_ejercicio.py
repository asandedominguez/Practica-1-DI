import \
    sys  # Importa el módulo del sistema para manejar los argumentos de la línea de comandos y la salida limpia de la app.
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel,
                             QLineEdit)  # Importa los componentes de la interfaz gráfica (widgets y layouts).
from PyQt6.QtGui import QColor, \
    QPalette  # Importa las clases necesarias para gestionar los colores y la paleta de la interfaz.


class FiestaPrincipal(QMainWindow):  # Define la clase de la ventana principal heredando de QMainWindow.
    def __init__(self):  # Método constructor que inicializa la clase.
        super().__init__()  # Llama al constructor de la clase padre (QMainWindow) para configurar correctamente el objeto.

        self.setWindowTitle('Prueba')  # Establece el título de la ventana como 'Prueba'.
        self.setMinimumSize(300,
                            200)  # Fija el tamaño mínimo que puede tener la ventana (300px de ancho por 200px de alto).
        self.setMaximumSize(500,
                            400)  # Fija el tamaño máximo que puede alcanzar la ventana (500px de ancho por 400px de alto).

        palette = self.palette()  # Obtiene la paleta de colores actual de la ventana.
        palette.setColor(QPalette.ColorRole.Window,
                         QColor("blue"))  # Modifica el color de fondo (Window) de la paleta y lo pone azul.
        self.setPalette(palette)  # Aplica la paleta de colores modificada a la ventana.

        caixaV = QVBoxLayout()  # Crea un gestor de diseño (layout) vertical. Los elementos se colocarán uno debajo de otro.

        boton = QPushButton('botón')  # Crea un botón con el texto 'botón'.
        boton.clicked.connect(
            self.on_boton_clicked)  # Conecta el evento de hacer clic en el botón con la función 'on_boton_clicked'.

        self.etiqueta = QLabel(
            "Hola a todas")  # Crea una etiqueta de texto que inicialmente dice "Hola a todas". Se usa 'self' para guardarla como atributo.
        self.cadroTexto = QLineEdit()  # Crea un cuadro de entrada de texto de una sola línea. Se usa 'self' para guardarlo como atributo.
        self.cadroTexto.setPlaceholderText(
            "Introduce tu nombre")  # Añade un texto de sugerencia gris de fondo al cuadro de texto.

        self.etiqueta.setText("Otro texto")  # Cambia inmediatamente el texto de la etiqueta a "Otro texto".
        self.cadroTexto.setText(
            "Tamén o podo modificar con outro texto")  # Escribe por defecto el texto gallego en el cuadro de entrada.

        print(self.etiqueta.text())  # Imprime en la consola de Python el texto actual de la etiqueta ("Otro texto").
        print(
            self.cadroTexto.text())  # Imprime en la consola el texto actual del cuadro de entrada ("Tamén o podo modificar con outro texto").

        caixaV.addWidget(self.etiqueta)  # Añade la etiqueta al diseño vertical (se posicionará arriba).
        caixaV.addWidget(self.cadroTexto)  # Añade el cuadro de texto al diseño vertical (se posicionará en el medio).
        caixaV.addWidget(boton)  # Añade el botón al diseño vertical (se posicionará abajo).

        contenedor = QWidget()  # Crea un widget genérico que servirá como base o contenedor principal.
        contenedor.setLayout(caixaV)  # Asigna el diseño vertical 'caixaV' dentro del contenedor genérico.
        self.setCentralWidget(
            contenedor)  # Establece este contenedor como el widget central de la ventana principal (QMainWindow).

        self.show()  # Hace que la ventana sea visible en la pantalla.

    def on_boton_clicked(self):  # Define el método que se ejecuta cuando el botón emite la señal 'clicked'.
        self.etiqueta  # Línea que hace referencia al atributo de la etiqueta pero no realiza ninguna acción ni operación.
        self.cadroTexto  # Línea que hace referencia al atributo del cuadro de texto pero no realiza ninguna acción ni operación.
        texto_actual = self.cadroTexto.text()  # Obtiene el texto que el usuario haya escrito dentro del cuadro en ese momento.
        self.etiqueta.setText("hola" + texto_actual)  # Asigna ese texto recuperado a la etiqueta, actualizando lo que se muestra en pantalla.


if __name__ == '__main__':  # Comprueba si este script se está ejecutando directamente (y no importado como un módulo).
    aplicacion = QApplication(
        sys.argv)  # Crea la instancia principal de la aplicación PyQt, pasando los argumentos del sistema.
    fiesta = FiestaPrincipal()  # Crea una instancia de nuestra ventana personalizada, lo que ejecuta su constructor e inicia la interfaz.
    aplicacion.exec()  # Inicia el bucle de eventos de la aplicación (mantiene el programa abierto esperando interacciones del usuario).
