import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QMainWindow
# from PySide6.QtCore import Qt  # Добавляем импорт Qt

from ui_calc_main import Ui_MainWindow
from database import Database


class Calculator(QMainWindow):
    """Инициализация главного окна приложения."""
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создание и настройка поля ввода
        self.input_field = self.ui.le_number
        self.input_field.returnPressed.connect(self.on_enter_pressed)

        # Создание и настройка поля для вывода результата
        self.result_field = self.ui.le_result

        # Создание и настройка многострочного текстового поля для отображения данных
        self.text_field = self.ui.textEdit

        # Создаем экземпляр класса базы данных
        self.database = Database('calc_database.db')

        # Загрузка данных при запуске
        self.load_from_database()

        self.input_field.textChanged.connect(self.calculate)

        self.show()


    def calculate(self):
        """Вычисление выражения, введенного в input_field."""
        expression = self.input_field.text()
        try:
            # Вычисляем выражение и выводим результат
            result = eval(expression)
            self.result_field.setText(str(result))
            return True, str(result)
        except Exception as e:
            self.result_field.setText("Ошибка")
            return False, "error"

    def on_enter_pressed(self):
        """Обработка нажатия Enter: вычисление и отображение результата."""
        success, result = self.calculate()
        if success:
            # self.text_field.setText(f"{self.input_field.text()} = {result}")
            self.text_field.append(f"{self.input_field.text()} = {result}")
            # self.database.insert_text(f"{self.input_field.text()} = {result}")
            # print("txt save!")

        # Сохранение отображаемых данных в базу данных.
        data_to_save = self.text_field.toPlainText().split('\n')
        if data_to_save:
            self.database.insert_data(data_to_save)
            print("Данные сщзранены в базе данных.")
            print(f"{data_to_save}")

    def load_from_database(self):
        """Загрузка и отображение последних сохраненных данных из базы данных."""
        data_from_db = self.database.get_last_data()
        for item in data_from_db:
            self.text_field.append(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()
    sys.exit(app.exec())
