import sys
import os
import csv
import random
import time
from fileinput import filename

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from charset_normalizer.cli import query_yes_no
from PySide6.QtCore import QTimer, Qt, Signal, QObject, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QIntValidator, QColor

from requests import session

from ui_05_pulsi import Ui_MainWindow
class ResultsTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)
    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None

# class ResultsDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.
class Puls_5(QMainWindow):
    update_gui = Signal()

    def __init__(self):
        super(Puls_5, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.session_time = 100
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_questions = 0
        self.session_active = False
        self.current_numbers = (0, 0)
        self.setup_timers() # Timer

        self.time_label = self.ui.time_label # UI label Timer
        self.progress_bar = self.ui.progress_bar # UI prog-bar

        self.question_label = self.ui.question_label # Вопрос
        self.answer_input = self.ui.answer_input # Поле ввода
        self.answer_input.returnPressed.connect(self.check_answer) # Отввет пользователя


        self.stats_label = self.ui.stats_label


        self.tableView = self.ui.tableView
        # headers = ["Правильные", "Неправильные", "Всего"]
        # data = [[self.correct_answers, self.incorrect_answers, self.total_questions]]

        data, headers = self.load_csv_data()
        self.model = ResultsTableModel(data, headers)
        self.tableView.setModel(self.model)

        self.start_btn = self.ui.start_btn # Ui start Btn
        self.start_btn.clicked.connect(self.toggle_session) # Start

        self.update_gui.connect(self.update_interface)

    def load_csv_data(self):
        filename = "session_05_main.csv"
        headers = ["Correct", "in-correct", "t-time", "%"]
        data = []

        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                try:
                    next(reader)  # Пропускаем заголовок
                except StopIteration:
                    pass

                for row in reader:
                    if len(row) == 4:
                        try:
                            data.append([int(row[0]), int(row[1]), float(row[2]), float(row[3])])
                        except ValueError:
                            print("ValueError row ")
                            continue
        return data, headers


    def setup_timers(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
    def toggle_session(self):
        if not self.session_active:
            self.start_session()
        else:
            self.end_session()

    def start_session(self):
        self.session_active = True
        self.session_time = 30
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_questions = 0
        self.start_btn.setText("Стоп")
        self.answer_input.setDisabled(False)
        self.generate_question()
        self.timer.start(100)
        self.updata_table()
        self.update_interface()

    def updata_table(self):
        data, headers = self.load_csv_data()
        self.model = ResultsTableModel(data, headers)
        self.tableView.setModel(self.model)

    def end_session(self):
        self.session_active = False
        self.timer.stop()
        self.answer_input.setDisabled(True)
        self.start_btn.setText("Старт")
        self.save_to_csv()
        self.show_results()

    def update_timer(self):
        self.session_time -= 1
        self.progress_bar.setValue(self.progress_bar.minimum() + self.session_time)


        if self.session_time <= 0:
            print("end")
            self.end_session()
        else:
            self.update_gui.emit()

    def generate_question(self):
        # self.ui.progressBar.setValue(self.progress_bar.maximum())

        self.current_numbers = (random.randint(0, 5), random.randint(0, 5))
        self.question_label.setText(
            f"{self.current_numbers[0]} + {self.current_numbers[1]} ="
        )
        self.answer_input.clear()
        self.answer_input.setFocus()

    def check_answer(self):
        try:
            answer = int(self.answer_input.text())
            correct = sum(self.current_numbers) == answer

            if correct:
                self.correct_answers += 1
                # self.stats_label.setText(f"correct: {self.correct_answers}")
                self.session_time += 20

                self.flash_background(QColor(144, 238, 144))  # Зеленый
            else:
                self.incorrect_answers += 1
                # self.stats_label.setText(f"error: ")

                self.flash_background(QColor(255, 182, 193))  # Красный

            self.generate_question()
            self.update_interface()
            # self.update_interface()

        except ValueError:
            pass
    def flash_background(self, color):
        original = self.palette().color(self.backgroundRole())
        self.setStyleSheet(f"background-color: {color.name()};")
        QTimer.singleShot(200, lambda: self.setStyleSheet(f"background-color: {original.name()};"))




    def update_interface(self):
        self.time_label.setText(f">{self.session_time} сек")
        self.stats_label.setText(f"Correct:{self.correct_answers} / Not:{self.incorrect_answers} / Tot:{self.total_questions}")

    def show_results(self):
        results = (
            f"Всего вопросов: {self.total_questions}\n"
            f"Правильных ответов: {self.correct_answers}\n"
            f"Неправильных ответов: {self.incorrect_answers}\n"
            f"Точность: {self.correct_answers/max(1, self.total_questions)*100:.1f}"
        )
        QMessageBox.information(self, "Результаты сессии", results)

    def save_to_csv(self):
        filename = "session_05_main.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writ = csv.writer(file)
            if not file_exists:
                writ.writerow(["corr", "in-corr", "total", "%"])
            writ.writerow([self.correct_answers, self.incorrect_answers, self.total_questions,
                           f"{self.correct_answers/max(1, self.total_questions)*100:.1f}"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Puls_5()
    window.show()

    sys.exit(app.exec_())