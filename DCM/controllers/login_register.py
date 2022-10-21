from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit

from controllers.dashboard import Dashboard
from database.db import Database
from database.user import User
from views.login_register import Ui_LoginRegister


# LoginRegister controller to handle data communication with LoginRegister view
class LoginRegister(QMainWindow, Ui_LoginRegister):
    def __init__(self):
        super(LoginRegister, self).__init__()
        self.setupUi(self)
        # declaration of class variables
        # state can be LOGIN or REGISTER based on the user selection
        self.state = "LOGIN"
        self.user = User()
        self.db = Database()
        self.db.connect()
        self.dashboard = Dashboard(self)

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, LoginRegister):
        Ui_LoginRegister.setupUi(self, LoginRegister)
        self.btn_register_login.clicked.connect(self.onclick_btn_register_login)
        self.btn_login_register.clicked.connect(self.onclick_btn_login_register)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

    # function to validate input credentials
    def validate_inputs(self):
        self.user.username = self.lineEdit_username.text().strip()
        self.user.password = self.lineEdit_password.text().strip()
        if self.user.username != "" and self.user.password != "":
            return True
        else:
            # display error for missing inputs
            QMessageBox.critical(self, "Invalid Inputs", "One or more details are missing",
                                 QMessageBox.StandardButton.Ok)
            return False

    # function will be called when user press login button depending upon the state
    def onclick_btn_login_register(self):
        # first validate inputs
        if self.validate_inputs():
            if self.state == "LOGIN":
                if self.db.login(self.user.username, self.user.password) is None:
                    QMessageBox.critical(self, "Login Error", "Invalid username or password!".
                                         format(self.user.username), QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Logged In", "Logged In Successfully!", QMessageBox.StandardButton.Ok)
                    self.clear()
                    self.hide()
                    self.dashboard.init(self.user.username)
                    self.dashboard.show()
            else:
                # check if user already exists
                if self.db.is_user_exists(self.user.username):
                    QMessageBox.critical(self, "User Already Exists", "User with username '{}' already exists!".
                                         format(self.user.username), QMessageBox.StandardButton.Ok)
                else:
                    if self.db.user_limit_exceeds():
                        QMessageBox.critical(self, "Registration Error", "Registered users Limit exceeded than 10!",
                                             QMessageBox.StandardButton.Ok)
                    else:
                        # add user in database
                        if self.db.add_user(self.user):
                            QMessageBox.information(self, "Registered", "User '{}' registered successfully!".
                                                    format(self.user.username), QMessageBox.StandardButton.Ok)
                            self.clear()
                            self.state = "LOGIN"
                            self.switch_state()

    # function will be callled when user wants to change the state from login to register and vice versa
    def onclick_btn_register_login(self):
        self.state = "REGISTER" if self.state == "LOGIN" else "LOGIN"
        self.switch_state()

    # function will be called to switch the state from login to register and vice versa
    def switch_state(self):
        if self.state == "LOGIN":
            self.label_login_register.setText("LOGIN")
            self.label_login_register_detail.setText("Please enter your credentials to login")
            self.btn_login_register.setText("Login")
            self.btn_register_login.setText("Don't Have an account? Sign Up")
        else:
            self.label_login_register.setText("Sign Up")
            self.label_login_register_detail.setText("Please enter the details to sign up")
            self.btn_login_register.setText("Sign Up")
            self.btn_register_login.setText("Already Have an account? Login")

    # function will clear the input credentials values
    def clear(self):
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()



