import sqlite3


class DBhandler:

    def __init__(self):
        self.conn = sqlite3.connect('railway_system.bd')
        self.cursor = self.conn.cursor()

    def select_cities(self):  # выписали все названия городов с их координатами
        dict_city = dict()
        self.cursor.execute('''SELECT city, geo_lat, geo_lon FROM city''')
        element = self.cursor.fetchall()
        for city in element:
            dict_city[city[0]] = city[1], city[2]
        return dict_city

    def select_train(self):  # выписали все названия поездов с их характеристиками
        dict_train = dict()
        self.cursor.execute('''SELECT nickname, train_type, wagon_type, max_capacity, wagons_count, average_speed FROM train''')
        element = self.cursor.fetchall()
        for trait in element:
            dict_train[trait[0]] = trait[1], trait[2], trait[3], trait[4], trait[5]
        return dict_train

    def select_schedule(self):  # выписали все маршруты
        dict_schedule = dict()
        self.cursor.execute('''SELECT id, train_nickname, otkuda, date_sending, time_sending, kuda, date_arrival, time_arrival, time_travel FROM schedule''')
        element = self.cursor.fetchall()
        for trait in element:
            dict_schedule[trait[0]] = trait[1], trait[2], trait[3], trait[4], trait[5], trait[6], trait[7], trait[8]
        return dict_schedule

    def insert_train(self, train):
        self.cursor.execute('''INSERT INTO train
                            (nickname, train_type, wagon_type, max_capacity, wagons_count, average_speed)
                            VALUES (?,?,?,?,?,?)''',
                            (train.nickname, train.train_type, train.type_wagons, train.max_load, train.count_wagons, train.average_speed))
        self.conn.commit()

    def insert_schedule(self, id_schedule, id_train, schedule):
        self.cursor.execute('''INSERT INTO schedule
                            (id, train_nickname, otkuda, date_sending, time_sending, kuda, date_arrival, time_arrival, time_travel)
                            VALUES (?,?,?,?,?,?,?,?,?)''',
                            (id_schedule, id_train, schedule.otkuda, str(schedule.date_sending), str(schedule.time_sending),
                             schedule.kuda, str(schedule.date_arrival), str(schedule.time_arrival), str(schedule.time_travel)))
        self.conn.commit()

    def delete_train(self, nickname):  # удалили поезд по его id
        print(nickname)
        self.cursor.execute(f'''DELETE FROM train WHERE nickname = {nickname} ''')
        self.conn.commit()