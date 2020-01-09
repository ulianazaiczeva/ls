from math import cos, radians, sin
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QFrame


class LSystemPaintWidget(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.qp = QPainter()
        self.lsystem = None

    def paint(self, init_x, init_y, length, lsystem):
        self.init_x = init_x
        self.init_y = init_y
        self.length = length
        self.lsystem = lsystem
        self.update()

    def coords(self, x, y):
        return int(x), int(self.size().height() - y)

    def draw_lsystem(self):
        if not self.lsystem:
            return

        x = self.init_x
        y = self.init_y
        k = 0
        m = []

        for h in self.lsystem.lstring:
            if h == "F" or h == 'f':
                new_x = x + self.length * cos(radians(k))
                new_y = y + self.length * sin(radians(k))
                if h == 'F':
                    self.qp.drawLine(*self.coords(x, y), *self.coords(new_x, new_y))
                x, y = new_x, new_y
            elif h == "-":
                k += self.lsystem.k()
            elif h == "+":
                k -= self.lsystem.k()
            elif h == "[":
                m.append((x, y, k))
            elif h == "]":
                x, y, angle = m.pop(-1)
            elif h == "|":
                k += 180

    def draw_bg(self):
        width, height = self.size().width() - 1, self.size().height() - 1
        self.qp.setBrush(QBrush(QColor('#FFFFFF')))
        self.qp.drawRect(0, 0, width, height)

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw_bg()
        self.draw_lsystem()
        self.qp.end()
