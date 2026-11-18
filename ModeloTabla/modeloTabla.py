from PyQt6.QtCore import *
from PyQt6.QtGui import *


class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla
        # Cambia este número según en qué posición esté la columna "DNI" en self.tabla[0]
        # Por ejemplo: 0 si es la primera columna, 1 si es la segunda
        self.columna_dni = 0

    def rowCount(self, indice=QModelIndex()):
        return len(self.tabla) - 1

    def columnCount(self, indice=QModelIndex()):
        return len(self.tabla[0])

    def data(self, indice, rol):
        if not indice.isValid():
            return None

        dato = self.tabla[indice.row() + 1][indice.column()]

        if rol == Qt.ItemDataRole.DisplayRole:
            if indice.column() == 3:
                return "✓" if dato else "✗"
            return dato

        if rol == Qt.ItemDataRole.EditRole:
            if indice.column() != self.columna_dni and indice.column() != 3:
                return dato

        if rol == Qt.ItemDataRole.CheckStateRole:
            if indice.column() == 3:
                return Qt.CheckState.Checked if dato else Qt.CheckState.Unchecked

        return None

    def setData(self, indice, valor, rol):
        if not indice.isValid():
            return False

        if rol == Qt.ItemDataRole.EditRole:
            # Bloqueamos tanto la columna del DNI como la columna 3 (checkbox)
            if indice.column() != self.columna_dni and indice.column() != 3:
                self.tabla[indice.row() + 1][indice.column()] = valor
                self.dataChanged.emit(indice, indice, [rol])
                return True

        if rol == Qt.ItemDataRole.CheckStateRole:
            if indice.column() == 3:
                self.tabla[indice.row() + 1][indice.column()] = (
                    valor == Qt.CheckState.Checked.value
                )
                self.dataChanged.emit(indice, indice, [rol, Qt.ItemDataRole.DisplayRole])
                return True

        return False

    def headerData(self, seccion, orientacion, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.tabla[0][seccion]
        return None

    def flags(self, indice):
        if not indice.isValid():
            return Qt.ItemFlag.NoItemFlags

        condicion = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        # Solo permitimos editar si NO es la columna del DNI ni la columna 3
        if indice.column() != self.columna_dni and indice.column() != 3:
            condicion = condicion | Qt.ItemFlag.ItemIsEditable

        if indice.column() == 3:
            condicion = condicion | Qt.ItemFlag.ItemIsUserCheckable

        return condicion