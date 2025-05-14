import random
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                               QPushButton, QVBoxLayout, QHBoxLayout, 
                               QProgressBar, QMessageBox)
from PySide6.QtCore import QTimer, Qt, Signal, QObject
from PySide6.QtGui import QIntValidator, QColor

class MathTrainer(QWidget):
    update_gui = Signal()

    def __init__(self):
        super().__init__()
        self.session_time = 30
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_questions = 0
        self.session_active = False
        self.current_numbers = (0, 0)
        self.init_ui()
        self.setup_timers()
        
    def init_ui(self):
        self.setWindowTitle("Математический Тренажер")
        self.setFixedSize(400, 300)
        
        # Создание элементов интерфейса
        self.time_label = QLabel(f"Время: {self.session_time} сек")
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(self.session_time)
        
        self.question_label = QLabel("Нажмите Старт для начала")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-size: 24px; color: #333;")
        
        self.answer_input = QLineEdit()
        self.answer_input.setValidator(QIntValidator(0, 100))
        self.answer_input.setDisabled(True)
        self.answer_input.returnPressed.connect(self.check_answer)
        
        self.stats_label = QLabel("Правильно: 0 | Неправильно: 0 | Всего: 0")
        
        self.start_btn = QPushButton("Старт")
        self.start_btn.clicked.connect(self.toggle_session)
        
        # Настройка layout
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.stats_label)
        layout.addWidget(self.start_btn)
        
        self.setLayout(layout)
        self.update_gui.connect(self.update_interface)
        
    def setup_timers(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
    def generate_question(self):
        self.current_numbers = (random.randint(0, 5), random.randint(0, 5))
        self.question_label.setText(
            f"{self.current_numbers[0]} + {self.current_numbers[1]} = ?"
        )
        self.answer_input.clear()
        self.answer_input.setFocus()
        
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
        self.timer.start(1000)
        self.update_interface()
        
    def end_session(self):
        self.session_active = False
        self.timer.stop()
        self.answer_input.setDisabled(True)
        self.start_btn.setText("Старт")
        self.show_results()
        
    def update_timer(self):
        self.session_time -= 1
        self.progress_bar.setValue(self.progress_bar.maximum() - self.session_time)
        
        if self.session_time <= 0:
            self.end_session()
        else:
            self.update_gui.emit()
            
    def check_answer(self):
        try:
            answer = int(self.answer_input.text())
            correct = sum(self.current_numbers) == answer
            
            if correct:
                self.correct_answers += 1
                self.flash_background(QColor(144, 238, 144))  # Зеленый
            else:
                self.incorrect_answers += 1
                self.flash_background(QColor(255, 182, 193))  # Красный
                
            self.total_questions += 1
            self.generate_question()
            self.update_interface()
            
        except ValueError:
            pass
            
    def flash_background(self, color):
        original = self.palette().color(self.backgroundRole())
        self.setStyleSheet(f"background-color: {color.name()};")
        QTimer.singleShot(200, lambda: self.setStyleSheet(f"background-color: {original.name()};"))
            
    def update_interface(self):
        self.time_label.setText(f"Время: {self.session_time} сек")
        self.stats_label.setText(
            f"Правильно: {self.correct_answers} | "
            f"Неправильно: {self.incorrect_answers} | "
            f"Всего: {self.total_questions}"
        )
        
    def show_results(self):
        results = (
            f"Всего вопросов: {self.total_questions}\n"
            f"Правильных ответов: {self.correct_answers}\n"
            f"Неправильных ответов: {self.incorrect_answers}\n"
            f"Точность: {self.correct_answers/max(1, self.total_questions)*100:.1f}%"
        )
        QMessageBox.information(self, "Результаты сессии", results)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    trainer = MathTrainer()
    trainer.show()
    sys.exit(app.exec())