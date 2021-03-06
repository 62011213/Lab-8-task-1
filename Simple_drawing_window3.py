import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Simple_drawing_window import Simple_drawing_window


class Simple_drawing_window3(Simple_drawing_window):

    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255, 50, 30))
        

        p.drawPolygon([
            QPoint( 50, 400 ), QPoint( 130, 400 ),
            QPoint( 50, 100 ), QPoint( 130, 100 )
        ])

        p.drawPixmap(QRect( 200, 100, 320, 320 ), self.rabbit )
        p.end()


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window3()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())