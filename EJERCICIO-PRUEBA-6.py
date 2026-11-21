import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableView, QLineEdit, QPushButton, QLabel, QMessageBox
)


class ModeloInventario(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self.datos = datos
        self.cabeceras = ["Producto", "Categoría", "Precio (€)", "Stock"]

    def rowCount(self, index):
        return len(self.datos)

    def columnCount(self, index):
        return len(self.cabeceras)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.cabeceras[section]
        return None

    def data(self, index, role):
        if not index.isValid():
            return None

        fila = index.row()
        col = index.column()
        valor = self.datos[fila][col]

        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            if col == 2:
                return f"{valor:.2f}"
            return str(valor)

        # Resaltar en rojo claro si el stock (columna 3) es menor que 5
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.datos[fila][3] < 5:
                return QColor(255, 200, 200)

        return None

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            fila = index.row()
            col = index.column()
            texto = str(value).strip()

            if not texto:
                return False

            if col == 2:  # Precio (float >= 0)
                try:
                    precio = float(texto.replace(",", "."))
                    if precio < 0:
                        return False
                    self.datos[fila][col] = precio
                except ValueError:
                    return False
            elif col == 3:  # Stock (int >= 0)
                try:
                    stock = int(texto)
                    if stock < 0:
                        return False
                    self.datos[fila][col] = stock
                except ValueError:
                    return False
            else:
                self.datos[fila][col] = texto

            self.dataChanged.emit(index, index)
            return True
        return False


class GestorInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventario de Tienda (QTableView)")
        self.setMinimumSize(620, 420)

        layout_principal = QVBoxLayout()

        # 1. Datos iniciales y tabla
        productos_iniciales = [
            ["Teclado Mecánico", "Periféricos", 79.90, 12],
            ["Ratón Inalámbrico", "Periféricos", 35.50, 3],
            ["Monitor 27 pulgadas", "Pantallas", 249.00, 7],
            ["Cable HDMI 2m", "Accesorios", 9.95, 2]
        ]
        self.modelo = ModeloInventario(productos_iniciales)
        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)
        layout_principal.addWidget(self.tabla)

        # 2. Fila de alta de nuevo producto
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

        # 3. Pie con botón eliminar y valor total del inventario
        fila_pie = QHBoxLayout()
        self.btn_borrar = QPushButton("Eliminar Seleccionado")
        self.lbl_total = QLabel("Valor total del inventario: 0.00 €")
        fila_pie.addWidget(self.btn_borrar)
        fila_pie.addWidget(self.lbl_total)
        layout_principal.addLayout(fila_pie)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # Conexiones explícitas
        self.btn_agregar.clicked.connect(self.agregar_producto)
        self.btn_borrar.clicked.connect(self.eliminar_producto)
        self.modelo.dataChanged.connect(self.recalcular_total)
        self.modelo.layoutChanged.connect(self.recalcular_total)

        self.recalcular_total()

    def agregar_producto(self):
        prod = self.txt_prod.text().strip()
        cat = self.txt_cat.text().strip()
        precio_txt = self.txt_precio.text().strip()
        stock_txt = self.txt_stock.text().strip()

        if not prod or not cat or not precio_txt or not stock_txt:
            QMessageBox.warning(self, "Error", "Rellena todos los campos del producto.")
            return

        try:
            precio = float(precio_txt.replace(",", "."))
            stock = int(stock_txt)
            if precio < 0 or stock < 0:
                QMessageBox.warning(self, "Error", "El precio y el stock no pueden ser negativos.")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio o stock con formato numérico inválido.")
            return

        self.modelo.datos.append([prod, cat, precio, stock])
        self.modelo.layoutChanged.emit()

        self.txt_prod.clear()
        self.txt_cat.clear()
        self.txt_precio.clear()
        self.txt_stock.clear()

    def eliminar_producto(self):
        indices = self.tabla.selectionModel().selectedRows()
        if not indices:
            # Si seleccionó una celda suelta en lugar de la fila entera
            celdas = self.tabla.selectedIndexes()
            if not celdas:
                return
            fila = celdas[0].row()
        else:
            fila = indices[0].row()

        del self.modelo.datos[fila]
        self.modelo.layoutChanged.emit()

    def recalcular_total(self):
        total = 0.0
        for fila in self.modelo.datos:
            total += fila[2] * fila[3]
        self.lbl_total.setText(f"Valor total del inventario: {total:.2f} €")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = GestorInventario()
    ventana.show()
    sys.exit(aplicacion.exec())