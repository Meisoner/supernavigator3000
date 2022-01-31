import requests
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, \
    QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

SCRN_WIDTH = 800
SCRN_HEIGH = 670


class Snv(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('supernavigator3000')
        self.setGeometry(0, 0, SCRN_WIDTH, SCRN_HEIGH)
        self.setStyleSheet('background: #f4f4f4; color: #000000; font-weight: 500; font-size: 14px; padding-left: 5px;')
        self.line_edit_style = 'background: #cccccc; color: #000000; font-size: 16px; border-radius: 20px;'
        self.btn_style = 'background: #ffad00; color: #000000; font-size: 16px; border-radius: 20px;'
        self.map_shower_style = 'background: #eeffdd;'
        # UI
        self.enter_obj = QLineEdit(self)
        self.enter_obj.setGeometry(10, 10, SCRN_WIDTH - 20, 40)
        self.enter_obj.setStyleSheet(self.line_edit_style)

        self.ok_btn = QPushButton("Найти!", self)
        self.ok_btn.setGeometry(SCRN_WIDTH - 110, 10, 100, 40)
        self.ok_btn.setStyleSheet(self.btn_style)
        # self.ok_btn.clicked.connect(self.gc_get)

        self.map_shower = QLabel("", self)
        self.map_shower.setGeometry(0, 60, 600 * 1.35, 450 * 1.35)
        self.map_shower.setStyleSheet(self.map_shower_style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    snv = Snv()
    snv.show()
    sys.exit(app.exec_())