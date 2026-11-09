import sys
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QComboBox,
    QWidget, QStackedLayout, QGridLayout, QLabel, QRadioButton,
    QHBoxLayout, QGroupBox, QListView, QAbstractItemView,
    QPushButton, QLineEdit, QMessageBox
)
class ModeloTarefas(QAbstractListModel):
    def __init__(self, tarefas=None):
        super().__init__()
        self.tarefas = tarefas or []

    def data(self, indice, rol=Qt.ItemDataRole.DisplayRole):
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tarefas[indice.row()]
            return texto

    def rowCount(self, indice=QModelIndex()):
        return len(self.tarefas)

    def engadir(self, texto):
        if texto:
            self.beginInsertRows(QModelIndex(), len(self.tarefas), len(self.tarefas))
            self.tarefas.append((False, texto))
            self.endInsertRows()

    def eliminar(self, fila):
        if 0 <= fila < len(self.tarefas):
            self.beginRemoveRows(QModelIndex(), fila, fila)
            del self.tarefas[fila]
            self.endRemoveRows()