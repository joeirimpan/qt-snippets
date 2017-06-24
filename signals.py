# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QLineEdit, QProgressBar,
    QLabel, QHBoxLayout
)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class ProgressBar_Dialog(QDialog):

    def __init__(self):
        super(ProgressBar_Dialog, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.progressLabel = QLabel('Progress Bar:', self)

        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)

        self.hboxLayout = QHBoxLayout(self)

        self.hboxLayout.addWidget(self.progressLabel)
        self.hboxLayout.addWidget(self.progressBar)

        self.setLayout(self.hboxLayout)
        self.setWindowTitle('Progressbar Dialog')

        self.show()

    @pyqtSlot(int)
    def set_slider_value(self, val):
        self.progressBar.setValue(val)

    def make_connection(self, slider_object):
        slider_object.changedValue.connect(self.set_slider_value)


class Number_Dialog(QDialog):

    changedValue = pyqtSignal(int)

    def __init__(self):
        super(Number_Dialog, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.editTextLabel = QLabel('Edit Number:', self)

        self.editText = QLineEdit(self)
        self.editText.setValidator(QIntValidator(0, 100, self))

        self.editText.textChanged.connect(
            self.on_changed_value
        )

        self.hboxLayout = QHBoxLayout(self)

        self.hboxLayout.addWidget(self.editTextLabel)
        self.hboxLayout.addWidget(self.editText)

        self.setLayout(self.hboxLayout)

        self.setWindowTitle("Number Dialog")
        self.show()

    def on_changed_value(self, value):
        self.changedValue.emit(int(value or 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    nd = Number_Dialog()
    pb = ProgressBar_Dialog()
    pb.make_connection(nd)
    sys.exit(app.exec_())
