import requests
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, \
    QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

SCRN_WIDTH = 800
SCRN_HEIGH = 670
intspn = 1


class Snv(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('supernavigator3000')
        self.setGeometry(0, 0, SCRN_WIDTH, SCRN_HEIGH)
        self.setStyleSheet('background: #f4f4f4; color: #000000; font-weight: 500; font-size: 14px; padding-left: 5px;')
        self.line_edit_style = 'background: #cccccc; color: #000000; font-size: 16px; border-radius: 20px;'
        self.btn_style = 'background: #ffad00; color: #000000; font-size: 16px; border-radius: 20px;'
        self.map_shower_style = 'background: #eeeedd;'
        # UI
        self.enter_obj = QLineEdit(self)
        self.enter_obj.setGeometry(10, 10, SCRN_WIDTH - 40, 40)
        self.enter_obj.setStyleSheet(self.line_edit_style)

        self.ok_btn = QPushButton("Найти!", self)
        self.ok_btn.setGeometry(SCRN_WIDTH - 110, 10, 100, 40)
        self.ok_btn.setStyleSheet(self.btn_style)
        self.ok_btn.clicked.connect(self.sm_get)

        self.map_shower = QLabel("", self)
        self.map_shower.setGeometry(0, 60, 600 * 1.34, 450 * 1.34)
        self.map_shower.setStyleSheet(self.map_shower_style)

        self.pu_btn = QPushButton("+", self)
        self.pu_btn.setGeometry(SCRN_WIDTH - 50, 60, 40, 40)
        self.pu_btn.setStyleSheet(self.btn_style)
        self.pu_btn.clicked.connect(self.pgup)

        self.pd_btn = QPushButton("-", self)
        self.pd_btn.setGeometry(SCRN_WIDTH - 50, 110, 40, 40)
        self.pd_btn.setStyleSheet(self.btn_style)
        self.pd_btn.clicked.connect(self.pgdown)

    def sm_get(self):
        spn = str(intspn)
        pos = self.enter_obj.text().split(',')
        mode = 'map'
        staticmap_request = f"http://static-maps.yandex.ru/1.x/?ll={pos[0]},{pos[1]}&spn={spn},{spn}&l={mode}"
        sm_response = requests.get(staticmap_request)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(sm_response.content)
            pixmap = QPixmap(self.map_file)
            scl_pixmap = pixmap.scaled(600 * 1.34, 450 * 1.34)
            self.map_shower.setPixmap(scl_pixmap)

    def pgup(self):
        global intspn
        intspn -= 0.5
        self.sm_get()

    def pgdown(self):
        global intspn
        intspn += 0.5
        self.sm_get()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    snv = Snv()
    snv.show()
    sys.exit(app.exec_())