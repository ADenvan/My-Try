import sys
import random
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from charset_normalizer.cli import query_yes_no
from PySide6.QtCore import QTimer, Qt, Signal, QObject
from requests import session

from ui_05_pulsi import Ui_MainWindow

class Puls_5(QMainWindow):
    update_gui = Signal()

    def __init__(self):
        super(Puls_5, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.session_active = False
        self.session_time = 100
        self.current_numbers = (0, 0)
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_questions = 0

        self.time_label = self.ui.time_label # UI label Timer
        self.progress_bar = self.ui.progress_bar # UI prog-bar

        self.question_label = self.ui.question_label #
        self.answer_input = self.ui.answer_input #
        self.answer_input.returnPressed.connect(self.check_answer)


        self.stats_label = self.ui.stats_label

        self.start_but = self.ui.start_btn # Ui start Btn
        self.start_but.clicked.connect(self.toggle_session) # Start

        self.update_gui.connect(self.update_interface)

        self.setup_timers() # Timer

    def toggle_session(self):
        self.start_session()

    def start_session(self):
        self.timer.start(100)
        self.generate_question()

    def generate_question(self):
        # self.ui.progressBar.setValue(self.progress_bar.maximum())

        self.current_numbers = (random.randint(0, 5), random.randint(0, 5))
        self.question_label.setText(
            f"{self.current_numbers[0]} + {self.current_numbers[1]} = ?"
        )
        self.answer_input.clear()
        self.answer_input.setFocus()

    def check_answer(self):
        try:
            answer = int(self.answer_input.text())
            correct = sum(self.current_numbers) == answer

            if correct:
                self.correct_answers += 1
                self.stats_label.setText(f"correct: {self.correct_answers}")
                self.session_time += 20
                # self.flash_background(QColor(144, 238, 144))  # Зеленый
            else:
                self.incorrect_answers += 1
                self.stats_label.setText(f"error: ")

                # self.flash_background(QColor(255, 182, 193))  # Красный

            self.total_questions += 1
            self.generate_question()
            self.update_interface()
            # self.update_interface()

        except ValueError:
            pass

    def setup_timers(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
    def end_session(self):
        self.timer.stop()

    def update_timer(self):
        # self.time_label.setText(f"> {self.session_time} сек")
        self.session_time -= 1
        self.progress_bar.setValue(self.progress_bar.minimum() + self.session_time)

        if self.session_time <= 0:
            print("end")
            self.end_session()
        else:
            self.update_gui.emit()
    def update_interface(self):
        # self.time_label.setText(self.session_time)
        self.stats_label.setText(f"Correct:{self.correct_answers} / Not:{self.incorrect_answers} / Tot:{self.total_questions}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Puls_5()
    window.show()

    sys.exit(app.exec_())