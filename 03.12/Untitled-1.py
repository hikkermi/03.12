import sys
from PyQt5 import QtWidgets, uic

class SurveyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SurveyApp, self).__init__()
        uic.loadUi('survey.ui', self)

        self.correct_answers = [0, 0, 2]
        self.user_answers = []

        self.startButton.clicked.connect(self.start_survey)
        self.nextButton1.clicked.connect(lambda: self.next_question(0))
        self.nextButton2.clicked.connect(lambda: self.next_question(1))
        self.nextButton3.clicked.connect(lambda: self.next_question(2))

        self.stackedWidget.setCurrentIndex(0)  

    def start_survey(self):
        self.stackedWidget.setCurrentIndex(1)
        self.user_answers = []

    def next_question(self, question_index):
        if question_index == 0:
            if self.radioButton1.isChecked():
                self.user_answers.append(0)
            elif self.radioButton2.isChecked():
                self.user_answers.append(1)
            elif self.radioButton3.isChecked():
                self.user_answers.append(2)
            else:
                self.user_answers.append(-1)
            
        elif question_index == 1:
            if self.radioButton4.isChecked():
                self.user_answers.append(0)
            elif self.radioButton5.isChecked():
                self.user_answers.append(1)
            elif self.radioButton6.isChecked():
                self.user_answers.append(2)
            else:
                self.user_answers.append(-1)
        
        elif question_index == 2:
            if self.radioButton7.isChecked():
                self.user_answers.append(0)
            elif self.radioButton8.isChecked():
                self.user_answers.append(1)
            elif self.radioButton9.isChecked():
                self.user_answers.append(2)
            else:
                self.user_answers.append(-1)

        if question_index < 2:
            self.stackedWidget.setCurrentIndex(question_index + 2)
            self.reset_radio_buttons(question_index + 2)
        else:
            self.show_results()

    def reset_radio_buttons(self, question_index):
        if question_index == 2:
            self.radioButton1.setChecked(False)
            self.radioButton2.setChecked(False)
            self.radioButton3.setChecked(False)
        elif question_index == 3:
            self.radioButton4.setChecked(False)
            self.radioButton5.setChecked(False)
            self.radioButton6.setChecked(False)
        elif question_index == 4:
            self.radioButton7.setChecked(False)
            self.radioButton8.setChecked(False)
            self.radioButton9.setChecked(False)

    def show_results(self):
        score = sum(1 for i, answer in enumerate(self.user_answers) if answer == self.correct_answers[i])
        self.resultLabel.setText(f'Ваш результат: {score} из {len(self.correct_answers)}')
        self.stackedWidget.setCurrentIndex(4)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SurveyApp()
    window.show()
    sys.exit(app.exec_())