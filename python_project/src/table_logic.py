import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    header_labels = ['Frequency', 'R-S11', 'I-S11', 'R-S21', 'I-21', 'R-S12', 'I-S12','R-S22', 'I-S22']
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data



    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)