import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMainWindow

import sys

class Form1(QDialog):
    def __init__(self, parent=None):
        super(Form1, self).__init__(parent)
        super().__init__()
        self.setFixedWidth(371)
        self.setFixedHeight(126)
        self.setWindowFlags(self.windowFlags()^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setModal(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 50, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Source/warning.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.setWindowTitle("Erreur !")
        self.label.setText("Récupérez les données s\'il vous plaît !")
        self.pushButton.setText("OK")
        self.setWindowIcon(QtGui.QIcon("Source/Icon.png"))
        self.setWindowTitle(" ")
        self.pushButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form1()
    form.show()
    sys.exit(app.exec_())