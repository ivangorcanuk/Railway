import sqlite3


class SQL:

    def __init__(self):
        self.conn = sqlite3.connect('railway_system.bd')
        self.cursor = self.conn.cursor()

    def select_cities(self):
        dict_city = {}
        self.cursor.execute('''SELECT city, geo_lat, geo_lon FROM city''')
        element = self.cursor.fetchall()
        for city in element:
            dict_city[city[0]] = city[1], city[2]
        self.cursor.close()

        return dict_city

# sql = SQL()
# for key, value in sql.select_cities().items():
#     print(key, value)