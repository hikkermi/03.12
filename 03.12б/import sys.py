import sys
from PyQt5 import QtWidgets, uic
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')  
        self.result_label = self.findChild(QtWidgets.QLabel, 'resultLabel')  
        self.button.clicked.connect(self.open_second_window)
        self.second_window = None
    def open_second_window(self):
        if self.second_window is None:
            self.second_window = SecondWindow(self)
        self.second_window.show()
    def update_result(self, result):
        self.result_label.setText(f'Результат: {result:.2f}')
class SecondWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(SecondWindow, self).__init__()
        uic.loadUi('second_window.ui', self)
        self.main_window = main_window
        self.calculate_button = self.findChild(QtWidgets.QPushButton, 'calculateButton')  
        self.input_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.calculate_button.clicked.connect(self.calculate)
    def calculate(self):
        try:
            value = float(self.input_line_edit.text())
            result = value * 0.15
            self.main_window.update_result(result)
            self.close()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введите корректное число!')
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())