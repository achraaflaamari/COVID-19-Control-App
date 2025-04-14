import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMainWindow

import sys

class Form3(QDialog):
    def __init__(self, parent=None):
        super(Form3, self).__init__(parent)
        super().__init__()
        self.setFixedWidth(600)
        self.setFixedHeight(126)
        self.setWindowFlags(self.windowFlags()^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setModal(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(45, 20, 510, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(110)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.quitter = QtWidgets.QPushButton(self)
        self.quitter.setGeometry(QtCore.QRect(395, 80, 75, 23))
        self.pushButton.setGeometry(QtCore.QRect(475, 80, 75, 23))
        self.setWindowTitle(" ")
        self.setWindowIcon(QtGui.QIcon("Source/Icon.png"))
        self.label.setText("Avant de quitter , merci de vérifier l'enregistrement de vos données")
        self.pushButton.setText("Enregistrer")
        self.quitter.setText("Quitter")
        self.quitter.clicked.connect(self.accept)
        self.pushButton.clicked.connect(self.reject)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form3()
    form.show()
    sys.exit(app.exec_())