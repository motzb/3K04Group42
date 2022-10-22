from PyQt5.QtWidgets import QApplication
from controllers.splash_screen import SplashScreen

# the main entry point of the function from where the application starts
if __name__ == "__main__":
    app = QApplication([])
    # the first screen of the application would be splash screen, all other screens would be called iteratively
    splash_screen = SplashScreen()
    splash_screen.show()
    app.exec_()
