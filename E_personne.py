from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form4(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(371)
        self.setFixedHeight(126)
        self.setWindowFlags(self.windowFlags()^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon("Source/Icon.png"))
        self.setWindowTitle(" ")
        layout = QVBoxLayout(self)
        self.label = QLabel(" ")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 50, 50))
        self.label_2.setText(" ")
        self.label_2.setPixmap(QtGui.QPixmap("Source/warning.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        button = QPushButton("OK", self)
        button.setGeometry(QtCore.QRect(150, 85, 75, 23))
        button.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication([])
    widget = Form4()
    widget.show()
    app.exec_()

