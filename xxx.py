import sys
import random as ran

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_ellipse()
        qp.end()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(ran.sample(range(100)), ran.sample(range((100))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())