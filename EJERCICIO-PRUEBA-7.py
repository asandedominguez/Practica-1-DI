import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
)


class EditorNotas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Notas - Sin título")
        self.setMinimumSize(640, 480)

        self.ruta_actual = None
        self.modificado = False

        # 1. Widget central de edición
        self.editor = QTextEdit()
        self.editor.textChanged.connect(self.al_modificar_texto)
        self.setCentralWidget(self.editor)

        # 2. Barra de estado inferior
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Listo | Caracteres: 0")

        # 3. Definición de acciones (QAction)
        self.accion_nuevo = QAction("Nuevo", self)
        self.accion_nuevo.setShortcut("Ctrl+N")
        self.accion_nuevo.triggered.connect(self.nuevo_archivo)

        self.accion_abrir = QAction("Abrir", self)
        self.accion_abrir.setShortcut("Ctrl+O")
        self.accion_abrir.triggered.connect(self.abrir_archivo)

        self.accion_guardar = QAction("Guardar", self)
        self.accion_guardar.setShortcut("Ctrl+S")
        self.accion_guardar.triggered.connect(self.guardar_archivo)

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.close)

        self.accion_limpiar = QAction("Limpiar todo", self)
        self.accion_limpiar.triggered.connect(self.limpiar_editor)

        self.accion_acerca = QAction("Acerca de", self)
        self.accion_acerca.triggered.connect(self.mostrar_acerca_de)

        # 4. Barra de menús superior (QMenuBar)
        barra_menu = self.menuBar()

        menu_archivo = barra_menu.addMenu("Archivo")
        menu_archivo.addAction(self.accion_nuevo)
        menu_archivo.addAction(self.accion_abrir)
        menu_archivo.addAction(self.accion_guardar)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)

        menu_editar = barra_menu.addMenu("Editar")
        menu_editar.addAction(self.accion_limpiar)

        menu_ayuda = barra_menu.addMenu("Ayuda")
        menu_ayuda.addAction(self.accion_acerca)

        # 5. Barra de herramientas (QToolBar)
        barra_herramientas = self.addToolBar("Principal")
        barra_herramientas.addAction(self.accion_nuevo)
        barra_herramientas.addAction(self.accion_abrir)
        barra_herramientas.addAction(self.accion_guardar)
        barra_herramientas.addSeparator()
        barra_herramientas.addAction(self.accion_limpiar)

    def al_modificar_texto(self):
        self.modificado = True
        num_caracteres = len(self.editor.toPlainText())
        nombre = self.ruta_actual if self.ruta_actual else "Sin título"
        self.setWindowTitle(f"Editor de Notas - *{nombre}")
        self.barra_estado.showMessage(f"Modificado | Caracteres: {num_caracteres}")

    def confirmar_descarte(self):
        if not self.modificado:
            return True

        respuesta = QMessageBox.question(
            self,
            "Cambios sin guardar",
            "Hay cambios sin guardar en el documento actual. ¿Deseas descartarlos?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        return respuesta == QMessageBox.StandardButton.Yes

    def nuevo_archivo(self):
        if not self.confirmar_descarte():
            return

        self.editor.clear()
        self.ruta_actual = None
        self.modificado = False
        self.setWindowTitle("Editor de Notas - Sin título")
        self.barra_estado.showMessage("Nuevo documento | Caracteres: 0")

    def abrir_archivo(self):
        if not self.confirmar_descarte():
            return

        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo de texto",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                self.editor.setPlainText(contenido)
                self.ruta_actual = ruta
                self.modificado = False
                self.setWindowTitle(f"Editor de Notas - {ruta}")
                self.barra_estado.showMessage(f"Archivo abierto | Caracteres: {len(contenido)}")
            except OSError as error:
                QMessageBox.critical(self, "Error al abrir", f"No se pudo leer el archivo:\n{error}")

    def guardar_archivo(self):
        if not self.ruta_actual:
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo de texto",
                "nota.txt",
                "Archivos de texto (*.txt);;Todos los archivos (*)"
            )
            if not ruta:
                return
            self.ruta_actual = ruta

        try:
            contenido = self.editor.toPlainText()
            with open(self.ruta_actual, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
            self.modificado = False
            self.setWindowTitle(f"Editor de Notas - {self.ruta_actual}")
            self.barra_estado.showMessage(f"Guardado correctamente | Caracteres: {len(contenido)}")
        except OSError as error:
            QMessageBox.critical(self, "Error al guardar", f"No se pudo guardar el archivo:\n{error}")

    def limpiar_editor(self):
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
        QMessageBox.information(
            self,
            "Acerca de Editor de Notas",
            "Editor de texto desarrollado con Python y PyQt6.\nIncluye menús, barra de herramientas y gestión de archivos."
        )

    def closeEvent(self, event):
        if self.confirmar_descarte():
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = EditorNotas()
    ventana.show()
    sys.exit(aplicacion.exec())