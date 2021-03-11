import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Simple_drawing_window import Simple_drawing_window

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        

        p.setPen(QPen(Qt.green,  5, Qt.SolidLine))

        p.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        p.drawEllipse(40, 40, 200, 400)
        p.drawPixmap(QRect( 300, 100, 320, 320 ), self.rabbit )
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())