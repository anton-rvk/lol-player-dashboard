import sqlite3
import os.path

class SummonerDatabase():

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "summoner-db.db")

        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def execute_sql(self, query):
        return self._cursor.execute(query)

    
