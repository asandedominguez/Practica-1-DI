from PyQt6.QtCore import Qt, QAbstractListModel

class ModeloTarefas(QAbstractListModel):
    def __init__(self, tarefas = None):
        super().__init__()
        self.tarefas = tarefas or []

    def data(self, indice, rol):
        pass

    def rowCount(self, indice):
        return len(self.tarefas)