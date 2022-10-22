from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from controllers.login_register import LoginRegister
from views.splash_screen import Ui_SplashScreen

# Global values
progressBarValue = 0


# Dashboard controller class that will handle all the events of the widgets in the dashboard view
class SplashScreen(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, SplashScreen):
        Ui_SplashScreen.setupUi(self, SplashScreen)

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Apply shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)

        # Lets use QTIMER to delay the progressBar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.login_register)

        self.timer.start(3000)

    # this function will change the value of the progress bar iteratively
    def login_register(self):
        self.login_register = LoginRegister()
        self.close()
        self.login_register.show()
        self.timer.stop()
