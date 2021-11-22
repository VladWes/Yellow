import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        uic.loadUi('UI.ui', self)
        self.flag = 0
        self.balls.clicked.connect(self.draw)

    def draw(self):
        self.flag = 1
        self.update()

    def paintEvent(self, event):
        if self.flag == 1:
            self.qp.begin(self)
            self.circle()
            self.qp.end()

    def circle(self):
        a = randrange(30, 200)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(300 - a, 300 - a, a, a)
        self.flag = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
