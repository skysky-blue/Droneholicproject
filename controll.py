import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton, QLabel
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
        self.slider_side.move(130, 30)
        self.slider_side.setRange(-1, 1)
        self.slider_side.setSingleStep(1)

        self.slider_yaw = QSlider(Qt.Vertical, self) #yaw 슬라이더 설정
        self.slider_yaw.move(230, 30)
        self.slider_yaw.setRange(-1,1)
        self.slider_yaw.setSingleStep(1)

        self.slider_up = QSlider(Qt.Vertical, self) #up 슬라이더 설정
        self.slider_up.move(330, 30)
        self.slider_up.setRange(0, 100)
        self.slider_up.setSingleStep(1)

        self.lab_pitch = QLabel('pitch', self)
        self.lab_pitch.move(55, 80)
        self.pitch_value = QLabel('0 ',self)
        self.pitch_value.move(55, 100)

        self.lab_roll = QLabel('roll', self)
        self.lab_roll.move(155, 80)
        self.roll_value = QLabel('0 ',self)
        self.roll_value.move(155, 100)

        self.lab_yaw = QLabel('yaw', self)
        self.lab_yaw.move(255, 80)
        self.yaw_value = QLabel('0 ',self)
        self.yaw_value.move(255, 100)

        self.lab_thr = QLabel('thr', self)
        self.lab_thr.move(355, 80)
        self.thr_value = QLabel('0    ',self)
        self.thr_value.move(355, 100)

        # font2 = label2.font()
        # font2.setFamily('Times New Roman')
        # font2.setBold(True)

        self.slider_front.valueChanged.connect(self.text_change)
        self.slider_side.valueChanged.connect(self.text_change)
        self.slider_up.valueChanged.connect(self.text_change)
        self.slider_yaw.valueChanged.connect(self.text_change)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()


        # while True:
            # print(self.keyReleaseEvent(self.key_W))
    def text_change(self):
        self.pitch_value.setText(str(self.front))
        self.roll_value.setText(str(self.side))
        self.yaw_value.setText(str(self.yaw))
        self.thr_value.setText(str(self.up))

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