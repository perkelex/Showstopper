import sys
import time
import subprocess
from PySide6 import QtCore, QtWidgets


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

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.topLabel)
        self.layout.addWidget(self.nowButton)
        self.layout.addWidget(self.oneHourButton)
        self.layout.addWidget(self.twoHourButton)
        self.layout.addWidget(self.threeHourButton)
        self.layout.addWidget(self.abortButton)
        self.layout.addWidget(self.bottomLabel)

        self.nowButton.clicked.connect(self.nowButtonOnClick)
        self.oneHourButton.clicked.connect(self.oneHourButtonOnClick)
        self.twoHourButton.clicked.connect(self.twoHourButtonOnClick)
        self.threeHourButton.clicked.connect(self.threeHourButtonOnClick)
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
    def abortButtonOnClick(self):
        self.bottomLabel.setText("Shutdown aborted!")

    def countdown(self):
        self.counter -= 1
        self.bottomLabel.setText(f"Countdown: {time.strftime('%#H:%M:%S', time.gmtime(self.counter))}")

    def shutdown(self):
        subprocess.Popen(['shutdown.exe', '-s', '-f', '-t', '0'])


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Showstopper()
    widget.setWindowTitle("Showstopper")
    # window icon doesn't work for some odd reason
    # widget.setWindowIcon(QtGui.QIcon("rss/shutodwn.png"))
    widget.resize(250, 100)
    widget.show()

    sys.exit(app.exec())