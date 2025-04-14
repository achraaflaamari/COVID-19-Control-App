from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel(self)
        self.setCentralWidget(label)
        label.setFixedHeight(900)
        movie = QMovie("Source/Studio_Project.gif")
        label.setMovie(movie)
        label.setScaledContents(True)
        movie.start()
        shortcut = QShortcut(QKeySequence("Esc"), self)
        shortcut.activated.connect(self.close)
        QTimer.singleShot(13250, lambda:self.close())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.showFullScreen()
    app.exec_()
