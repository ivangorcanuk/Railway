import sqlite3


class DBhandler:

    def __init__(self):
        self.conn = sqlite3.connect('railway_system.bd')
        self.cursor = self.conn.cursor()

    def select_cities(self):
        dict_city = {}
        self.cursor.execute('''SELECT city, geo_lat, geo_lon FROM city''')
        element = self.cursor.fetchall()
        for city in element:
            dict_city[city[0]] = city[1], city[2]

        return dict_city

    def insert_train(self, train):
        self.cursor.execute('''INSERT INTO train
                            (id, nickname, train_type, wagon_type, max_capacity, wagons_count, average_speed)
                            VALUES (?,?,?,?,?,?,?)''',
                            (train.nickname, train.train_type, train.type_wagons, train.max_load, train.count_wagons, train.average_speed))
        self.conn.commit()

    def insert_schedule(self, schedule, train):
        self.cursor.execute('''INSERT INTO schedule
                            (id, id_pers, otkuda, date_sending, time_sending, kuda, date_arrival, time_arrival, time_travel)
                            VALUES (?,?,?,?,?,?,?,?,?)''',
                            (train.nickname, schedule.date_sending, str(schedule.time_sending),
                             str(schedule.time_arrival), str(schedule.time_travel), train.train_type))
        self.conn.commit()