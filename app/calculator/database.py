import json
import sqlite3

class Database:
    def __init__(self, db_name):
        """Инициализируем соединение с базой данных и создаем таблицу, если она не существует."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Создаем таблицу в базе данных для хранения данных."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS saved_data (
                                id INTEGER PRIMARY KEY,
                                data TEXT
                                )''')
        self.connection.commit()

    def insert_data(self, data):
        """Вставляем данные в базу данных."""
        data_json = json.dumps(data)
        self.cursor.execute("INSERT INTO saved_data (data) VALUES (?)", (data_json,))
        self.connection.commit()

    def get_last_data(self):
        """Получаем последний сохраненный набор данных из базы данных."""
        self.cursor.execute("SELECT data FROM saved_data ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchone()
        return json.loads(result[0]) if result else []


    # def __init__(self, db_name):
    #     self.connection = sqlite3.connect(db_name)
    #     self.cursor = self.connection.cursor()
    #     self.create_table()
    #
    # def create_table(self):
    #     self.cursor.execute('''CREATE TABLE IF NOT EXISTS saved_text (
    #                             id INTEGER PRIMARY KEY,
    #                             text TEXT
    #                             )''')
    #     self.connection.commit()
    #
    # def insert_text(self, data):
    #     data_json = json.dumps(data)
    #     self.cursor.execute("INSERT INTO saved_text (text) VALUES (?)", (data_json,))
    #     self.connection.commit()
    #
    # def get_last_data(self):
    #     """Получаем последний сохраненный набор данных из базы данных."""
    #     self.cursor.execute("SELECT data FROM saved_data ORDER BY id DESC LIMIT 1")
    #     result = self.cursor.fetchone()
    #     return json.loads(result[0]) if result else []