import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableView, QLineEdit, QPushButton, QLabel, QMessageBox
)


# ==============================================================================
# 1. MODELO DE TABLA EDITABLE (Patrón Modelo-Vista)
# ==============================================================================
class ModeloInventario(QAbstractTableModel):
    """Gestiona una matriz 2D (filas y columnas), cabeceras, colores y edición directa."""

    def __init__(self, datos):
        super().__init__()  # Inicializa QAbstractTableModel
        self.datos = datos  # Lista de listas: [[producto, categoría, precio, stock], ...]
        self.cabeceras = ["Producto", "Categoría", "Precio (€)", "Stock"]

    def rowCount(self, index):
        # Método obligatorio: indica el número total de filas
        return len(self.datos)

    def columnCount(self, index):
        # Método obligatorio: indica el número total de columnas
        return len(self.cabeceras)

    def headerData(self, section, orientation, role):
        # Define los títulos de la fila superior (cabeceras horizontales)
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.cabeceras[section]
        return None

    def data(self, index, role):
        # La vista llama a este método para dibujar cada celda (fila, columna)
        if not index.isValid():
            return None

        fila = index.row()
        col = index.column()
        valor = self.datos[fila][col]

        # DisplayRole: texto normal de la celda | EditRole: texto que aparece al hacer doble clic
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            if col == 2:  # Columna de precio: formatea siempre a 2 decimales
                return f"{valor:.2f}"
            return str(valor)

        # BackgroundRole: pinta el fondo de toda la fila de rojo suave si hay poco stock (< 5)
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.datos[fila][3] < 5:
                return QColor(255, 200, 200)

        return None

    def flags(self, index):
        # Habilita que las celdas se puedan seleccionar, activar y editar con doble clic
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role):
        # Se ejecuta automáticamente cuando el usuario termina de editar una celda en la tabla
        if role == Qt.ItemDataRole.EditRole:
            fila = index.row()
            col = index.column()
            texto = str(value).strip()

            if not texto:  # Rechaza dejar celdas vacías
                return False

            if col == 2:  # Validación si editó el Precio (float >= 0)
                try:
                    precio = float(texto.replace(",", "."))  # Admite coma o punto decimal
                    if precio < 0:
                        return False
                    self.datos[fila][col] = precio
                except ValueError:
                    return False
            elif col == 3:  # Validación si editó el Stock (int >= 0)
                try:
                    stock = int(texto)
                    if stock < 0:
                        return False
                    self.datos[fila][col] = stock
                except ValueError:
                    return False
            else:  # Columnas de texto (Producto o Categoría)
                self.datos[fila][col] = texto

            # Emite la señal dataChanged avisando qué celda cambió (activa el recálculo del total)
            self.dataChanged.emit(index, index)
            return True
        return False


# ==============================================================================
# 2. VENTANA PRINCIPAL (Vista y Controlador)
# ==============================================================================
class GestorInventario(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa QMainWindow

        # Configuración básica de la ventana
        self.setWindowTitle("Inventario de Tienda (QTableView)")  # Título superior
        self.setMinimumSize(620, 420)  # Tamaño mínimo permitido

        # Layout principal vertical: tabla arriba, formulario en medio, pie abajo
        layout_principal = QVBoxLayout()

        # --- ZONA SUPERIOR: Tabla conectada al modelo ---
        productos_iniciales = [
            ["Teclado Mecánico", "Periféricos", 79.90, 12],
            ["Ratón Inalámbrico", "Periféricos", 35.50, 3],
            ["Monitor 27 pulgadas", "Pantallas", 249.00, 7],
            ["Cable HDMI 2m", "Accesorios", 9.95, 2]
        ]
        self.modelo = ModeloInventario(productos_iniciales)
        self.tabla = QTableView()  # Widget visual en forma de hoja de cálculo
        self.tabla.setModel(self.modelo)  # Vincula la tabla con nuestro modelo de datos
        layout_principal.addWidget(self.tabla)

        # --- ZONA INTERMEDIA: Formulario horizontal para añadir filas ---
        fila_nuevo = QHBoxLayout()
        self.txt_prod = QLineEdit()
        self.txt_prod.setPlaceholderText("Producto")
        self.txt_cat = QLineEdit()
        self.txt_cat.setPlaceholderText("Categoría")
        self.txt_precio = QLineEdit()
        self.txt_precio.setPlaceholderText("Precio")
        self.txt_stock = QLineEdit()
        self.txt_stock.setPlaceholderText("Stock")
        self.btn_agregar = QPushButton("Añadir Producto")

        fila_nuevo.addWidget(self.txt_prod)
        fila_nuevo.addWidget(self.txt_cat)
        fila_nuevo.addWidget(self.txt_precio)
        fila_nuevo.addWidget(self.txt_stock)
        fila_nuevo.addWidget(self.btn_agregar)
        layout_principal.addLayout(fila_nuevo)

        # --- ZONA INFERIOR: Botón de borrado y etiqueta de resumen ---
        fila_pie = QHBoxLayout()
        self.btn_borrar = QPushButton("Eliminar Seleccionado")
        self.lbl_total = QLabel("Valor total del inventario: 0.00 €")

        fila_pie.addWidget(self.btn_borrar)
        fila_pie.addWidget(self.lbl_total)
        layout_principal.addLayout(fila_pie)

        # --- ENSAMBLAJE FINAL ---
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # --- CONEXIÓN DE SEÑALES Y SLOTS ---
        self.btn_agregar.clicked.connect(self.agregar_producto)
        self.btn_borrar.clicked.connect(self.eliminar_producto)

        # Cada vez que se edita una celda (dataChanged) o se añade/borra una fila (layoutChanged),
        # se dispara automáticamente el recálculo del valor total del inventario
        self.modelo.dataChanged.connect(self.recalcular_total)
        self.modelo.layoutChanged.connect(self.recalcular_total)

        # Calculamos el valor total inicial al arrancar la ventana
        self.recalcular_total()

    # ==========================================================================
    # 3. MÉTODOS DE GESTIÓN DEL INVENTARIO (SLOTS)
    # ==========================================================================
    def agregar_producto(self):
        prod = self.txt_prod.text().strip()
        cat = self.txt_cat.text().strip()
        precio_txt = self.txt_precio.text().strip()
        stock_txt = self.txt_stock.text().strip()

        # Comprobamos que ningún campo esté vacío
        if not prod or not cat or not precio_txt or not stock_txt:
            QMessageBox.warning(self, "Error", "Rellena todos los campos del producto.")
            return

        # Validamos que precio (decimal) y stock (entero) sean números válidos y >= 0
        try:
            precio = float(precio_txt.replace(",", "."))
            stock = int(stock_txt)
            if precio < 0 or stock < 0:
                QMessageBox.warning(self, "Error", "El precio y el stock no pueden ser negativos.")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio o stock con formato numérico inválido.")
            return

        # Insertamos la nueva fila en el modelo y notificamos para redibujar y recalcular
        self.modelo.datos.append([prod, cat, precio, stock])
        self.modelo.layoutChanged.emit()

        # Limpiamos los 4 campos de entrada
        self.txt_prod.clear()
        self.txt_cat.clear()
        self.txt_precio.clear()
        self.txt_stock.clear()

    def eliminar_producto(self):
        # Primero comprueba si el usuario seleccionó toda la fila haciendo clic en el número lateral
        indices = self.tabla.selectionModel().selectedRows()
        if not indices:
            # Si solo hizo clic en una celda suelta, obtenemos la fila a la que pertenece esa celda
            celdas = self.tabla.selectedIndexes()
            if not celdas:
                return
            fila = celdas[0].row()
        else:
            fila = indices[0].row()

        # Eliminamos la fila de los datos y notificamos a la vista
        del self.modelo.datos[fila]
        self.modelo.layoutChanged.emit()

    def recalcular_total(self):
        # Suma (precio * stock) de cada producto en el modelo
        total = 0.0
        for fila in self.modelo.datos:
            total += fila[2] * fila[3]
        self.lbl_total.setText(f"Valor total del inventario: {total:.2f} €")


# ==============================================================================
# 4. PUNTO DE ENTRADA DE LA APLICACIÓN
# ==============================================================================
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)  # Crea la instancia de la aplicación
    ventana = GestorInventario()  # Crea nuestra ventana
    ventana.show()  # Muestra la ventana en pantalla
    sys.exit(aplicacion.exec())  # Inicia el bucle de eventos hasta cerrar