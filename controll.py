import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        self.front = 125  # pitch 움직임 값
        self.side = 125  # roll 움직임 값
        self.up = 0  # throttle 움직임 값
        self.yaw = 125  # yaw 움직임 값
        self.pow = 0  # 파워 설정 값
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider_front = QSlider(Qt.Vertical, self)  # front 슬라이더 설정
        self.slider_front.move(30, 30)
        self.slider_front.setRange(0, 255)
        self.slider_front.setSingleStep(1)
        self.slider_front.setValue(self.front)

        self.slider_side = QSlider(Qt.Vertical, self)  # side 슬라이더 설정
        self.slider_side.move(130, 30)
        self.slider_side.setRange(0, 255)
        self.slider_side.setSingleStep(1)
        self.slider_side.setValue(self.side)

        self.slider_yaw = QSlider(Qt.Vertical, self)  # yaw 슬라이더 설정
        self.slider_yaw.move(230, 30)
        self.slider_yaw.setRange(0, 255)
        self.slider_yaw.setSingleStep(1)
        self.slider_yaw.setValue(self.yaw)

        self.slider_up = QSlider(Qt.Vertical, self)  # up 슬라이더 설정
        self.slider_up.move(330, 30)
        self.slider_up.setRange(0, 100)
        self.slider_up.setSingleStep(1)

        self.slider_pow = QSlider(Qt.Vertical, self)  # pow 슬라이더 설정
        self.slider_pow.move(430, 30)
        self.slider_pow.setRange(0, 130)
        self.slider_pow.setSingleStep(10)

        self.lab_pitch = QLabel('pitch', self)
        self.lab_pitch.move(55, 80)
        self.pitch_value = QLabel('125', self)
        self.pitch_value.move(55, 100)

        self.lab_roll = QLabel('roll', self)
        self.lab_roll.move(155, 80)
        self.roll_value = QLabel('125', self)
        self.roll_value.move(155, 100)

        self.lab_yaw = QLabel('yaw', self)
        self.lab_yaw.move(255, 80)
        self.yaw_value = QLabel('125', self)
        self.yaw_value.move(255, 100)

        self.lab_thr = QLabel('thr', self)
        self.lab_thr.move(355, 80)
        self.thr_value = QLabel('0    ', self)
        self.thr_value.move(355, 100)

        self.lab_pow = QLabel('pow', self)
        self.lab_pow.move(455, 80)
        self.pow_value = QLabel('0    ', self)
        self.pow_value.move(455, 100)

        self.slider_front.valueChanged.connect(self.text_change)
        self.slider_side.valueChanged.connect(self.text_change)
        self.slider_up.valueChanged.connect(self.text_change)
        self.slider_yaw.valueChanged.connect(self.text_change)
        self.slider_pow.valueChanged.connect(self.text_change)

        self.discription = QLabel('W,S는 pitch값 +- / A,D는 roll값 +- / Q,E는 yaw값 +- / R,F는 thr값 +-\n             pow슬라이더는 thr제외한 변수 변동 값 조정',self)
        self.discription.move(10,200)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 500, 300)
        self.show()

    def text_change(self):
        self.pow = self.slider_pow.value()
        self.pitch_value.setText(str(self.front))
        self.roll_value.setText(str(self.side))
        self.yaw_value.setText(str(self.yaw))
        self.thr_value.setText(str(self.up))
        self.pow_value.setText(str(self.pow))

    def keyReleaseEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key()
        if key == 87 and not eventQKeyEvent.isAutoRepeat():
            self.front = 125
            self.slider_front.setValue(self.front)
        elif key == 83 and not eventQKeyEvent.isAutoRepeat():
            self.front = 125
            self.slider_front.setValue(self.front)
        elif key == 65 and not eventQKeyEvent.isAutoRepeat():
            self.side = 125
            self.slider_side.setValue(self.side)
        elif key == 68 and not eventQKeyEvent.isAutoRepeat():
            self.side = 125
            self.slider_side.setValue(self.side)
        elif key == 81 and not eventQKeyEvent.isAutoRepeat():
            self.yaw = 125
            self.slider_yaw.setValue(self.yaw)
        elif key == 69 and not eventQKeyEvent.isAutoRepeat():
            self.yaw = 125
            self.slider_yaw.setValue(self.yaw)
        print("$36M77<60l5ㅁ150}%d}%d}%d%dU85ㅁ%d" % (self.side, self.front, self.yaw, self.up,
                                                    5 ^ 150 ^ self.side ^ self.front ^ self.yaw ^ self.up ^ 85))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_W and self.front == 125:  # pitch 조정

            self.front += self.pow
            self.slider_front.setValue(self.front)
        elif e.key() == Qt.Key_S and self.front == 125:
            if self.pow >= 125:
                self.front = 0
            else:
                self.front -= self.pow
            self.slider_front.setValue(self.front)
        elif e.key() == Qt.Key_A and self.side == 125:  # roll 조정
            self.side += self.pow
            self.slider_side.setValue(self.side)
        elif e.key() == Qt.Key_D and self.side ==125 :
            if self.pow >= 125:
                self.side = 0
            else:
                self.side -= self.pow
            self.slider_side.setValue(self.side)
        elif e.key() == Qt.Key_R:  # 상하 조정
            if self.up <= 95:
                self.up += 5
            self.slider_up.setValue(self.up)
        elif e.key() == Qt.Key_F:
            if self.up >= 5:
                self.up -= 5
            self.slider_up.setValue(self.up)
        elif e.key() == Qt.Key_Q and self.yaw == 125:  # yaw 조정
            self.yaw += self.pow
            self.slider_yaw.setValue(self.yaw)
        elif e.key() == Qt.Key_E and self.yaw == 125:
            if self.pow >= 125:
                self.yaw = 0
            else:
                self.yaw -= self.pow
            self.slider_yaw.setValue(self.yaw)

        print("$36M77<60l5ㅁ150}%d}%d}%d%dU85ㅁ%d" % (self.side, self.front, self.yaw, self.up,
                                                    5 ^ 150 ^ self.side ^ self.front ^ self.yaw ^ self.up ^ 85))


app = QApplication(sys.argv)
ex = MyApp()

sys.exit(app.exec_())
