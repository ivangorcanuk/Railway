import sqlite3


class SQL:

    def __init__(self):
        self.conn = sqlite3.connect('railway_system.bd')
        self.cursor = self.conn.cursor()

    def select_cities(self):
        list_city = list()
        self.cursor.execute('''SELECT city FROM city''')
        element = self.cursor.fetchall()
        for city in element:
            list_city.append(city)
        self.cursor.close()

        return list_city