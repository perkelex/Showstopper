from sys import exit
from time import strftime, gmtime
from subprocess import Popen
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIntValidator


class Showstopper(QtWidgets.QWidget):
    class Decoratos(object):
        @staticmethod
        def stopTimers(func):
            def inner(self, *args, **kwargs):
                if self.countdownTimer.isActive():
                    self.countdownTimer.stop()
                if self.triggerTimer.isActive():
                    self.triggerTimer.stop()

                func(self, *args, **kwargs)
            return inner

    def __init__(self):
        super().__init__()

        self.counter = 0
        self.topLabel = QtWidgets.QLabel("Shutdown in",
                                     alignment=QtCore.Qt.AlignCenter)
        self.bottomLabel = QtWidgets.QLabel("",
                                     alignment=QtCore.Qt.AlignCenter)

        self.nowButton = QtWidgets.QPushButton("Now")
        self.oneHourButton = QtWidgets.QPushButton("1h")
        self.twoHourButton = QtWidgets.QPushButton("2h")
        self.threeHourButton = QtWidgets.QPushButton("3h")
        self.abortButton = QtWidgets.QPushButton("Abort")

        self.countdownTimer = QtCore.QTimer()
        self.countdownTimer.setInterval(1000)
        self.countdownTimer.timeout.connect(self.countdown)

        self.triggerTimer = QtCore.QTimer()
        self.triggerTimer.timeout.connect(self.shutdown)
        self.triggerTimer.setSingleShot(True)

        self.layout = QtWidgets.QGridLayout(self)
        self.customTimeLayout = QtWidgets.QHBoxLayout()
        self.CTLHourInput = QtWidgets.QLineEdit("00")
        self.CTLHourInput.setFixedWidth(20)
        self.CTLHourInput.setFixedHeight(15)

        self.CTLHMSeparatorLabel = QtWidgets.QLabel(":",
                                     alignment=QtCore.Qt.AlignCenter)

        self.CTLMinuteInput = QtWidgets.QLineEdit("00")
        self.CTLMinuteInput.setFixedWidth(20)
        self.CTLMinuteInput.setFixedHeight(15)

        self.CTLMSSeparatorLabel = QtWidgets.QLabel(":",
                                     alignment=QtCore.Qt.AlignCenter)

        self.CTLSecondInput = QtWidgets.QLineEdit("00")
        self.CTLSecondInput.setFixedWidth(20)
        self.CTLSecondInput.setFixedHeight(15)

        self.CTLStartButton = QtWidgets.QPushButton("Start")

        self.customTimeLayout.addWidget(self.CTLHourInput)
        self.customTimeLayout.addWidget(self.CTLHMSeparatorLabel)
        self.customTimeLayout.addWidget(self.CTLMinuteInput)
        self.customTimeLayout.addWidget(self.CTLMSSeparatorLabel)
        self.customTimeLayout.addWidget(self.CTLSecondInput)
        self.customTimeLayout.addWidget(self.CTLStartButton)

        self.layout.addWidget(self.topLabel, 0, 1)
        self.layout.addWidget(self.nowButton, 1, 1)
        self.layout.addWidget(self.oneHourButton, 2, 1)
        self.layout.addWidget(self.twoHourButton, 3, 1)
        self.layout.addWidget(self.threeHourButton, 4, 1)
        self.layout.addLayout(self.customTimeLayout, 5, 1)
        self.layout.addWidget(self.abortButton, 6, 1)
        self.layout.addWidget(self.bottomLabel, 7, 1)

        self.setLayout(self.layout)

        self.nowButton.clicked.connect(self.nowButtonOnClick)
        self.oneHourButton.clicked.connect(self.oneHourButtonOnClick)
        self.twoHourButton.clicked.connect(self.twoHourButtonOnClick)
        self.threeHourButton.clicked.connect(self.threeHourButtonOnClick)
        self.CTLStartButton.clicked.connect(self.CTLStartButtonOnClick)
        self.abortButton.clicked.connect(self.abortButtonOnClick)


    @Decoratos.stopTimers
    def nowButtonOnClick(self):
        self.counter = 0

        self.triggerTimer.setInterval(self.counter * 1000)
        self.triggerTimer.start()

        self.countdownTimer.start()

    @Decoratos.stopTimers
    def oneHourButtonOnClick(self):
        self.counter = 3600

        self.triggerTimer.setInterval(self.counter * 1000)
        self.triggerTimer.start()

        self.countdownTimer.start()

    @Decoratos.stopTimers
    def twoHourButtonOnClick(self):
        self.counter = 7200

        self.triggerTimer.setInterval(self.counter * 1000)
        self.triggerTimer.start()

        self.countdownTimer.start()

    @Decoratos.stopTimers
    def threeHourButtonOnClick(self):
        self.counter = 10800

        self.triggerTimer.setInterval(self.counter * 1000)
        self.triggerTimer.start()

        self.countdownTimer.start()

    @Decoratos.stopTimers
    def CTLStartButtonOnClick(self):
        self.counter = self.getHours() + self.getMinutes() + self.getSeconds()

        self.triggerTimer.setInterval(self.counter * 1000)
        self.triggerTimer.start()

        self.countdownTimer.start()

    @Decoratos.stopTimers
    def abortButtonOnClick(self):
        self.bottomLabel.setText("Shutdown aborted!")

    def countdown(self):
        self.counter -= 1
        self.bottomLabel.setText(f"Countdown: {strftime('%#H:%M:%S', gmtime(self.counter))}")

    def shutdown(self):
        Popen(['shutdown.exe', '-s', '-f', '-t', '0'])

    def getHours(self):
        hours = 0
        try:
            hours = int(self.CTLHourInput.text()) * 3600
        except:
            return 0
        return hours

    def getMinutes(self):
        minutes = 0
        try:
            minutes = int(self.CTLMinuteInput.text()) * 60
        except:
            return 0
        return minutes

    def getSeconds(self):
        seconds = 0
        try:
            seconds = int(self.CTLSecondInput.text())
        except:
            return 0
        return seconds


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Showstopper()
    widget.setWindowTitle("Showstopper")
    # window icon doesn't work for some odd reason
    # widget.setWindowIcon(QtGui.QIcon("rss/shutodwn.png"))
    widget.resize(250, 100)
    widget.show()

    exit(app.exec())