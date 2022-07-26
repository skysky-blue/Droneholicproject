import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt
import time

class MyApp(QWidget):


    def __init__(self):

        self.front = 0 #pitch 움직임 값
        self.side = 0  #roll 움직임 값
        self.up = 0    #throttle 움직임 값
        self.yaw = 0   #yaw 움직임 값
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

        self.slider_yaw = QSlider(Qt.Vertical, self) #yaw 슬라이더 설정
        self.slider_yaw.move(130, 30)
        self.slider_yaw.setRange(-1,1)
        self.slider_yaw.setSingleStep(1)

        self.slider_up = QSlider(Qt.Vertical, self) #up 슬라이더 설정
        self.slider_up.move(180, 30)
        self.slider_up.setRange(0, 100)
        self.slider_up.setSingleStep(1)

        btn = QPushButton('초기화', self)
        btn.move(35, 160)

        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()


        # while True:
            # print(self.keyReleaseEvent(self.key_W))

    def button_clicked(self):
        self.slider_front.setValue(0)
        self.slider_side.setValue(0)
        self.slider_up.setValue(0)
        self.slider_yaw.setValue(0)

    # def value_(self):


    def keyPressEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key()
        if key == 54:
            print('pressed')  # 6

    def keyReleaseEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key()
        if key == 87 and not eventQKeyEvent.isAutoRepeat():
            self.front = 0
            self.slider_front.setValue(self.front)
        elif key == 83 and not eventQKeyEvent.isAutoRepeat():
            self.front = 0
            self.slider_front.setValue(self.front)
        elif key == 65 and not eventQKeyEvent.isAutoRepeat():
            self.side = 0
            self.slider_side.setValue(self.side)
        elif key == 68 and not eventQKeyEvent.isAutoRepeat():
            self.side = 0
            self.slider_side.setValue(self.side)
        elif key == 81 and not eventQKeyEvent.isAutoRepeat():
            self.yaw = 0
            self.slider_yaw.setValue(self.yaw)
        elif key == 69 and not eventQKeyEvent.isAutoRepeat():
            self.yaw = 0
            self.slider_yaw.setValue(self.yaw)



    def keyPressEvent(self, e):

        if e.key() == Qt.Key_W: #pitch 조정
            self.front += 1
            self.slider_front.setValue(self.front)
        elif e.key() == Qt.Key_S:
            self.front -= 1
            self.slider_front.setValue(self.front)
        elif e.key() == Qt.Key_A: #roll 조정
            self.side += 1
            self.slider_side.setValue(self.side)
        elif e.key() == Qt.Key_D:
            self.side -= 1
            self.slider_side.setValue(self.side)
        elif e.key() == Qt.Key_R: #상하 조정
            self.up += 5
            self.slider_up.setValue(self.up)
        elif e.key() == Qt.Key_F:
            self.up -= 5
            self.slider_up.setValue(self.up)
        elif e.key() == Qt.Key_Q: #yaw 조정
            self.yaw += 1
            self.slider_yaw.setValue(self.yaw)
        elif e.key() == Qt.Key_E:
            self.yaw -= 1
            self.slider_yaw.setValue(self.yaw)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())