import sys
from PyQt5 import QtWidgets, uic

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('login.ui', self)
        
        self.login_button = self.findChild(QtWidgets.QPushButton, 'loginButton')
        self.login_button.clicked.connect(self.check_login)

        self.clear_button = self.findChild(QtWidgets.QPushButton, 'clearButton')
        self.clear_button.clicked.connect(self.clear_fields)

        self.user_data = {'admin': '123','HikkerMi':'AAAZOV'} 

    def check_login(self):
        username = self.findChild(QtWidgets.QLineEdit, 'usernameLineEdit').text()
        password = self.findChild(QtWidgets.QLineEdit, 'passwordLineEdit').text()

        if username in self.user_data and self.user_data[username] == password:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.error_window = ErrorWindow()
            self.error_window.show()

    def clear_fields(self):
        self.findChild(QtWidgets.QLineEdit, 'usernameLineEdit').clear()
        self.findChild(QtWidgets.QLineEdit, 'passwordLineEdit').clear()

class ErrorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ErrorWindow, self).__init__()
        uic.loadUi('error.ui', self)

        self.close_button = self.findChild(QtWidgets.QPushButton, 'closeButton')
        self.close_button.clicked.connect(self.close)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())