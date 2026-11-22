import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
)


# ==============================================================================
# 1. CLASE DE LA VENTANA PRINCIPAL
# ==============================================================================
class EditorNotas(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle("Editor de Notas - Sin título")  # Título inicial superior
        self.setMinimumSize(640, 480)  # Tamaño mínimo permitido

        # Variables de estado internas para rastrear el archivo en uso
        self.ruta_actual = None  # Guarda la ruta en disco (None si aún no se ha guardado)
        self.modificado = False  # Bandera (flag) que indica si hay cambios pendientes

        # --- SECCIÓN 1: Área central de escritura ---
        self.editor = QTextEdit()  # Área de texto multilínea enriquecido
        # Cada vez que el usuario teclea o borra algo, se dispara al_modificar_texto
        self.editor.textChanged.connect(self.al_modificar_texto)
        self.setCentralWidget(self.editor)  # Ocupa todo el cuerpo central de QMainWindow

        # --- SECCIÓN 2: Barra de estado inferior (QStatusBar) ---
        self.barra_estado = self.statusBar()  # Obtiene la barra inferior nativa de QMainWindow
        self.barra_estado.showMessage("Listo | Caracteres: 0")

        # --- SECCIÓN 3: Definición de acciones reutilizables (QAction) ---
        # QAction encapsula un comando (texto, atajo y función) para usarlo en menús y barras a la vez
        self.accion_nuevo = QAction("Nuevo", self)
        self.accion_nuevo.setShortcut("Ctrl+N")  # Atajo de teclado
        self.accion_nuevo.triggered.connect(self.nuevo_archivo)

        self.accion_abrir = QAction("Abrir", self)
        self.accion_abrir.setShortcut("Ctrl+O")
        self.accion_abrir.triggered.connect(self.abrir_archivo)

        self.accion_guardar = QAction("Guardar", self)
        self.accion_guardar.setShortcut("Ctrl+S")
        self.accion_guardar.triggered.connect(self.guardar_archivo)

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.close)  # Llama al cierre de la ventana

        self.accion_limpiar = QAction("Limpiar todo", self)
        self.accion_limpiar.triggered.connect(self.limpiar_editor)

        self.accion_acerca = QAction("Acerca de", self)
        self.accion_acerca.triggered.connect(self.mostrar_acerca_de)

        # --- SECCIÓN 4: Barra de menús superior (QMenuBar) ---
        barra_menu = self.menuBar()  # Obtiene la barra de menús superior nativa

        # Menú desplegable "Archivo"
        menu_archivo = barra_menu.addMenu("Archivo")
        menu_archivo.addAction(self.accion_nuevo)
        menu_archivo.addAction(self.accion_abrir)
        menu_archivo.addAction(self.accion_guardar)
        menu_archivo.addSeparator()  # Dibuja una línea horizontal divisoria
        menu_archivo.addAction(self.accion_salir)

        # Menú desplegable "Editar"
        menu_editar = barra_menu.addMenu("Editar")
        menu_editar.addAction(self.accion_limpiar)

        # Menú desplegable "Ayuda"
        menu_ayuda = barra_menu.addMenu("Ayuda")
        menu_ayuda.addAction(self.accion_acerca)

        # --- SECCIÓN 5: Barra de herramientas flotante/acoplada (QToolBar) ---
        barra_herramientas = self.addToolBar("Principal")
        # Reutilizamos exactamente las mismas instancias QAction creadas arriba
        barra_herramientas.addAction(self.accion_nuevo)
        barra_herramientas.addAction(self.accion_abrir)
        barra_herramientas.addAction(self.accion_guardar)
        barra_herramientas.addSeparator()  # Separador vertical en la barra de iconos
        barra_herramientas.addAction(self.accion_limpiar)

    # ==========================================================================
    # 2. MÉTODOS DE CONTROL DE ESTADO Y ARCHIVOS (SLOTS)
    # ==========================================================================
    def al_modificar_texto(self):
        # Marca el documento como sucio (pendiente de guardar)
        self.modificado = True
        num_caracteres = len(self.editor.toPlainText())
        nombre = self.ruta_actual if self.ruta_actual else "Sin título"

        # Añade un asterisco (*) al título de la ventana para avisar de cambios sin guardar
        self.setWindowTitle(f"Editor de Notas - *{nombre}")
        self.barra_estado.showMessage(f"Modificado | Caracteres: {num_caracteres}")

    def confirmar_descarte(self):
        # Si no hay cambios pendientes, permite continuar directamente (True)
        if not self.modificado:
            return True

        # Abre un cuadro de diálogo modal pidiendo confirmación Sí/No
        respuesta = QMessageBox.question(
            self,
            "Cambios sin guardar",
            "Hay cambios sin guardar en el documento actual. ¿Deseas descartarlos?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        # Devuelve True solo si el usuario pulsó "Yes"
        return respuesta == QMessageBox.StandardButton.Yes

    def nuevo_archivo(self):
        # Antes de borrar el documento actual, comprueba si hay que pedir confirmación
        if not self.confirmar_descarte():
            return

        self.editor.clear()  # Vacía el editor (esto dispara textChanged primero)
        self.ruta_actual = None  # Resetea la ruta en disco
        self.modificado = False  # Fuerza modificado a False tras limpiar
        self.setWindowTitle("Editor de Notas - Sin título")
        self.barra_estado.showMessage("Nuevo documento | Caracteres: 0")

    def abrir_archivo(self):
        if not self.confirmar_descarte():
            return

        # Abre el explorador de archivos nativo del sistema operativo para elegir fichero
        # Devuelve una tupla: (ruta_seleccionada, filtro_usado); ignoramos el segundo con '_'
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo de texto",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        if ruta:
            try:
                # Lee el archivo en codificación UTF-8 para soportar tildes y eñes
                with open(ruta, "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()

                self.editor.setPlainText(contenido)  # Vuelca el texto en el editor
                self.ruta_actual = ruta  # Memoriza la ruta abierta
                self.modificado = False  # Resetea el estado tras la carga
                self.setWindowTitle(f"Editor de Notas - {ruta}")
                self.barra_estado.showMessage(f"Archivo abierto | Caracteres: {len(contenido)}")
            except OSError as error:
                # Captura errores de lectura (permisos, archivo corrupto, etc.)
                QMessageBox.critical(self, "Error al abrir", f"No se pudo leer el archivo:\n{error}")

    def guardar_archivo(self):
        # Si es un documento nuevo sin ruta asignada, pide dónde guardarlo (Guardar como)
        if not self.ruta_actual:
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo de texto",
                "nota.txt",
                "Archivos de texto (*.txt);;Todos los archivos (*)"
            )
            if not ruta:  # Si el usuario canceló el cuadro de diálogo, aborta
                return
            self.ruta_actual = ruta

        try:
            contenido = self.editor.toPlainText()
            # Escribe el contenido en disco sobrescribiendo el archivo
            with open(self.ruta_actual, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)

            self.modificado = False  # Ya está sincronizado con el disco
            self.setWindowTitle(f"Editor de Notas - {self.ruta_actual}")
            self.barra_estado.showMessage(f"Guardado correctamente | Caracteres: {len(contenido)}")
        except OSError as error:
            QMessageBox.critical(self, "Error al guardar", f"No se pudo guardar el archivo:\n{error}")

    def limpiar_editor(self):
        # Si ya está vacío, no hace falta preguntar nada
        if self.editor.toPlainText() == "":
            return

        respuesta = QMessageBox.question(
            self,
            "Limpiar texto",
            "¿Seguro que quieres borrar todo el texto del editor?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta == QMessageBox.StandardButton.Yes:
            self.editor.clear()

    def mostrar_acerca_de(self):
        # Muestra una ventana modal informativa simple
        QMessageBox.information(
            self,
            "Acerca de Editor de Notas",
            "Editor de texto desarrollado con Python y PyQt6.\nIncluye menús, barra de herramientas y gestión de archivos."
        )

    # ==========================================================================
    # 3. EVENTO NATIVO DE CIERRE DE VENTANA
    # ==========================================================================
    def closeEvent(self, event):
        # Sobrescribe el evento que Qt lanza al pulsar la 'X' de la ventana o Ctrl+Q
        if self.confirmar_descarte():
            event.accept()  # Permite que la ventana se cierre
        else:
            event.ignore()  # Cancela el cierre y mantiene el editor abierto


# ==============================================================================
# 4. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = EditorNotas()  # Crea nuestra ventana
    ventana.show()  # Muestra la ventana en pantalla
    sys.exit(aplicacion.exec())  # Inicia el bucle de eventos hasta cerrar