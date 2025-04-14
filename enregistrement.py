from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ajout_eff import Form5

class Form6(QDialog):
    def __init__(self):
        global fermer
        super().__init__()
        self.setFixedWidth(371)
        self.setFixedHeight(130)
        self.setWindowFlags(self.windowFlags()^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon("Source/Icon.png"))
        self.setWindowTitle(" ")
        layout = QVBoxLayout(self)
        self.label = QLabel(" Enregistrement... ")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(90)
        self.label.setFont(font)
        layout.addStretch()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(150, 85, 100, 18)
        self.progress_bar.setMaximum(100)
        layout.addWidget(self.label,alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.progress_bar)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress_bar)
        self.timer.start(10)
        layout.addStretch()
        layout.addStretch()
        self.label2 = QLabel(" ")
        self.label2.hide()
    def closeEvent(self, event):
        if not self.timer.isActive():
            self.enr=Form5()
            self.enr.label.setText(self.label2.text())
            self.enr.show()
            event.accept()
        else:
            event.ignore()
    def update_progress_bar(self):
        value = self.progress_bar.value() + 1
        self.progress_bar.setValue(value)

        if value >= 100:
            self.timer.stop()
            self.close()


if __name__ == '__main__':
    app = QApplication([])
    widget = Form6()
    widget.show()
    app.exec_()

