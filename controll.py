import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):


    def __init__(self):
        self.front = 0 #앞뒤 움직임 값
        self.side = 0  #좌우 움직임 값
        self.up = 0    #상하 움직임 값
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider_front = QSlider(Qt.Vertical, self) #front 슬라이더 설정
        self.slider_front.move(30, 30)
        self.slider_front.setRange(-1,1)
        self.slider_front.setSingleStep(1)

        self.slider_side = QSlider(Qt.Vertical, self) #side 슬라이더 설정
        self.slider_side.move(80, 30)
        self.slider_side.setRange(-1, 1)
        self.slider_side.setSingleStep(1)

        self.slider_up = QSlider(Qt.Vertical, self) #up 슬라이더 설정
        self.slider_up.move(130, 30)
        self.slider_up.setRange(0, 100)
        self.slider_up.setSingleStep(1)

        btn = QPushButton('초기화', self)
        btn.move(35, 160)

        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

        self.keyReleaseEvent(Qt.key_W)
        while True:
            print(self.keyReleaseEvent(self.key_W))

    def button_clicked(self):
        self.slider_front.setValue(0)
        self.slider_side.setValue(0)
        self.slider_up.setValue(0)

    # def value_(self):

    # keyRealease
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_W: #앞뒤 조정
            self.front += 1
            self.slider_front.setValue(self.front)
        elif e.key() == Qt.Key_S:
            self.front -= 1
            self.slider_front.setValue(self.front)
        elif e.key() == Qt.Key_A: #좌우 조정
            self.side += 1
            self.slider_side.setValue(self.side)
        elif e.key() == Qt.Key_D:
            self.side -= 1
            self.slider_side.setValue(self.side)
        elif e.key() == Qt.Key_Q: #상하 조정
            self.up += 5
            self.slider_up.setValue(self.up)
        elif e.key() == Qt.Key_E:
            self.up -= 5
            self.slider_up.setValue(self.up)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())