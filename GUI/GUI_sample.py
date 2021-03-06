# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        # self.setWindowIcon(QIcon('web.png')) # 图标样式
        #
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()
    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()

    sys.exit(app.exec_())

