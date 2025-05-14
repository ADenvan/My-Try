import sys
import asyncio
import random
from PySide6.QtCore import QThread, Signal, Slot, QObject
from PySide6.QtWidgets import QApplication, QMainWindow
from googletrans import Translator
from database import Database
from ui_game import Ui_MainWindow

# Асинхронный переводчик с кэшированием
class AsyncTranslator(QObject):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.cache = {}

    async def translate(self, text, src='ru', dest='en'):
        try:
            if text in self.cache:
                return self.cache[text]
            
            translated = await self.translator.translate(text, src=src, dest=dest)
            result = translated.text
            self.cache[text] = result
            return result
        except Exception as e:
            raise e

# Рабочий поток для выполнения асинхронных задач
class WorkerThread(QThread):
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, coroutine):
        super().__init__()
        self.coroutine = coroutine

    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(self.coroutine)
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация компонентов
        self.database = Database('trans_database.db')
        self.translator = AsyncTranslator()
        self.session_words = []
        self.current_word = None

        # Настройка сигналов
        self.ui.input_text.textChanged.connect(self.schedule_translation)
        self.ui.en_le_text.returnPressed.connect(self.check_answer)
        self.ui.start_session.clicked.connect(self.start_session)
        self.ui.save_word_button.clicked.connect(self.add_words_to_db)

        # Загрузка данных
        self.load_initial_data()

    def load_initial_data(self):
        """Загрузка начальных данных из БД и JSON"""
        self.database.load_from_json('words_js_file.json')
        self.words = self.database.words_dict
        self.update_history()

    def schedule_translation(self):
        """Запланировать перевод с задержкой"""
        text = self.ui.input_text.toPlainText().strip()
        if text:
            self.run_async_task(self.translator.translate(text), self.handle_translation_result)

    def start_session(self):
        """Начать тренировочную сессию"""
        count = self.ui.session_spinbox.value()
        self.session_words = random.sample(list(self.words.items()), count)
        self.next_word()

    def next_word(self):
        """Показать следующее слово"""
        if not self.session_words:
            self.ui.check_qeust_ans_text.append("Сессия завершена!")
            return

        self.current_word = self.session_words.pop()
        self.ui.ru_qeustion.setText(self.current_word[0])
        self.ui.en_le_text.clear()

    def check_answer(self):
        """Проверить ответ пользователя"""
        user_answer = self.ui.en_le_text.text().strip().lower()
        correct = self.current_word[1].lower()
        
        if user_answer == correct:
            message = f"✓ Правильно: {self.current_word[0]} -> {correct}"
        else:
            message = f"✗ Ошибка: {self.current_word[0]} | Ваш ответ: {user_answer} | Правильно: {correct}"
        
        self.ui.check_qeust_ans_text.append(message)
        self.next_word()

    def add_words_to_db(self):
        """Добавить слова в базу данных"""
        ru = self.ui.input_text.toPlainText().strip()
        en = self.ui.output_text.toPlainText().strip()
        
        if ru and en:
            self.database.add_word_in_db(en, ru)
            self.database.save_to_json('words_js_file.json')
            self.words[ru] = en
            self.update_history()
            self.ui.check_qeust_ans_text.append(f"Добавлено: {ru} - {en}")

    def update_history(self):
        """Обновить историю"""
        data = self.database.get_table_db()
        self.ui.check_qeust_ans_text.clear()
        for item in data:
            self.ui.check_qeust_ans_text.append(f"{item[1]} - {item[2]}")

    def run_async_task(self, coroutine, callback):
        """Запуск асинхронной задачи"""
        def handle_result(result):
            callback(result)
            worker.deleteLater()

        def handle_error(error):
            self.ui.output_text.setText(f"Ошибка: {error}")
            worker.deleteLater()

        worker = WorkerThread(coroutine)
        worker.finished.connect(handle_result)
        worker.error.connect(handle_error)
        worker.start()

    def handle_translation_result(self, result):
        """Обработка результата перевода"""
        self.ui.output_text.setPlainText(result)
        self.ui.save_word_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec())
