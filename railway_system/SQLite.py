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

    def insert_train(self, train):
        self.cursor.execute('''INSERT INTO train
                            (nickname, train_type, type_wagon, max_pas/weight, count_wagons, average_speed)
                            VALUES (?,?,?,?,?,?)''',
                            (train.nickname, train.train_type, train.type_wagons, train.max, train.count_wagons, train.average_speed))
        self.conn.commit()
        self.cursor.close()

    def insert_schedule(self, schedule):
        self.cursor.execute('''INSERT INTO schedule
                            (nickname, date_sending, date_arrival, time_sending, time_arrival, time_travel, train_type)
                            VALUES (?,?,?,?,?,?,?)''',
                            (schedule.nickname, schedule.date_departures, schedule.date_arrival, schedule.time_departures,
                             schedule.time_arrival, schedule.time_travel, schedule.train_type))
        self.conn.commit()
        self.cursor.close()

# sql = SQL()
# for key, value in sql.select_cities().items():
#     print(key, value)