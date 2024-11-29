import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.first_paint = True

    def paintEvent(self, event):
        if not self.first_paint:
            qp = QPainter()
            qp.begin(self)
            for i in range(10):
                self.draw_circle(qp)
            qp.end()
        self.first_paint = False

    def paint(self):
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = randint(0, 700), randint(0, 600)
        diameter = randint(20, 200)
        qp.drawEllipse(x, y, diameter, diameter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
