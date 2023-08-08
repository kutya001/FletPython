# TODO
# 1 - Получение списка таблиц

# 2 - Создание/Удаление таблиц

# 3 - Именение структуры таблиц
#     - Добавление и удаление столбцов(колонок)
#     - Изменение типов и свойств столбцов

# 4 - Изменение данных в таблицах
#     - Чтение
#     - Добавление
#     - Изменение(Обновление)
#     - Удаление

# 5 - Настройка доступа

# 6 - регистрация и авторизация
import psycopg2 as ps

from psycopg2 import extras

class DBManager:

    def __init__(self, db_connection) -> None:
        self._db = db_connection
        self.cursor = db_connection.cursor(cursor_factory=extras.RealDictCursor)


    def select_all(self, table: str):
        query = f"""SELECT * FROM {table}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_all_tb(self):
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def create(self, table: str, **kwargs):
        fields_name = ', '.join((name for name in kwargs.keys()))
        values = "(%s)" * len(kwargs.values())
        query = f"""INSERT INTO {table} ({fields_name}) values""" + values
        self.cursor.execute(query, tuple(values for value in kwargs.values()))
        self._db.commit()