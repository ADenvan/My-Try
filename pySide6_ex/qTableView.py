import sys
import csv
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QLabel, QTableView,
                               QDialog, QHeaderView)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex


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
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None


class ResultsDialog(QDialog):
    def __init__(self, correct, incorrect, total, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Результаты сессии")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.tableView = QTableView()

        # Создаем модель данных
        headers = ["Правильные", "Неправильные", "Всего"]
        data = [[correct, incorrect, total]]
        self.model = ResultsTableModel(data, headers)

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.tableView)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.correct = 0
        self.incorrect = 0
        self.total = 0

        self.setWindowTitle("Тренажер")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.stats_label = QLabel(
            f"Правильно: {self.correct}\n"
            f"Неправильно: {self.incorrect}\n"
            f"Всего вопросов: {self.total}"
        )
        self.stats_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.stats_label)

        buttons_layout = QHBoxLayout()

        self.correct_btn = QPushButton("Правильный ответ")
        self.correct_btn.clicked.connect(self.add_correct)
        buttons_layout.addWidget(self.correct_btn)

        self.incorrect_btn = QPushButton("Неправильный ответ")
        self.incorrect_btn.clicked.connect(self.add_incorrect)
        buttons_layout.addWidget(self.incorrect_btn)

        layout.addLayout(buttons_layout)

        self.end_btn = QPushButton("Завершить сессию")
        self.end_btn.clicked.connect(self.end_session)
        layout.addWidget(self.end_btn)

    def add_correct(self):
        self.correct += 1
        self.total += 1
        self.update_stats()

    def add_incorrect(self):
        self.incorrect += 1
        self.total += 1
        self.update_stats()

    def update_stats(self):
        self.stats_label.setText(
            f"Правильно: {self.correct}\n"
            f"Неправильно: {self.incorrect}\n"
            f"Всего вопросов: {self.total}"
        )

    def end_session(self):
        dialog = ResultsDialog(self.correct, self.incorrect, self.total, self)
        dialog.exec()
        self.save_to_csv()

    def save_to_csv(self):
        filename = "session_results.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Правильные", "Неправильные", "Всего вопросов"])
            writer.writerow([self.correct, self.incorrect, self.total])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())