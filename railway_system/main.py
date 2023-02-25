# Программа управления железнодорожной системой
# railway system
# В проекте используются 4 сущности:
# Станции Station, с количеством путей, и типом -- пасажирские или грузовые
# Пути, соединяющие станции Track
# Поезда Train, каждый с уникальным номером, именованием модели, а так же типом вагоном
# грузовые/пассажирские, и соотвестевнно со допустимым тоннажем и кол-вом пассажиров
# Графики schedules (ну или типа строка  врасписании поездов), которые содержат время прибытия и время
# отправления и станции соответственно, ну и также поезд который по этому графику следует.
#
# В программе должна быть БД, и графический интерфейс, который позволит редактировать расписание для
# разных поездов, а также добавлять новые.
# Выводить расписание поездов для запрашиваемой станции
# Добавлять удалять поезда, станции
# Редактивровать расписание для станций
# Позволять рассчитать время пути между двумя выбранными станциями

# Разобраться с временными функциями
# При регистрации нового маршрута для получения скорости и id связать расписание с поездами
# При регистрации нового расписания выводить поезда, которые без маршрутов
# Осуществить удаление поездов (маршрут без поезда существовать не может, таким образом удалять поезда нужно вместе с маршрутом)

from GUI import *
from SQLite import DBhandler
from train_tupe import Passenger, Cargo, TrainBase, WorkingUtils


class MergerSQL:
    def __init__(self):
        self.sql = DBhandler()
        self.dict_city = self.sql.select_cities()  # вытянули словарь с городами
        self.dict_train = self.sql.select_train()  # вытянули словарь с поездами
        self.dict_schedule = self.sql.select_schedule()  # вытянули словарь с маршрутами
        self.train = None
        self.list_id_train = self.sql.select_id_train()

    def create_train(self, nickname, train_type, type_wagons, count_wagons, average_speed):  # создаем поезд
        max_load = WorkingUtils.max_load(type_wagons, count_wagons)  # вернули максимальную нагрузку
        self.train = WorkingUtils.registration_train(nickname, train_type, type_wagons, max_load, count_wagons, average_speed)
        list_id_train = self.sql.select_id_train()
        id = WorkingUtils.id_installation(list_id_train)
        print(id, self.train.nickname, self.train.train_type, self.train.type_wagons,
              self.train.max_load, self.train.count_wagons, self.train.average_speed)
        self.sql.insert_train(id, self.train)  # сохранили в базу

    def create_schedule(self, otkuda, kuda, date_time, train_name):  # создаем расписание
        distance = WorkingUtils.distance(self.dict_city, otkuda, kuda)
        id_train = int()
        for key, value in self.dict_train.items():
            if value[0] == str(train_name):
                id_train = key
        speed = self.dict_train[id_train][5]
        # schedule = WorkingUtils.registration_schedule(otkuda, date_sending, time_sending, kuda, date_arrival, time_arrival, time_travel)
        # print(schedule.otkuda, schedule.date_sending, schedule.time_sending, schedule.kuda,
        #       schedule.date_arrival, schedule.time_arrival, schedule.time_travel)
        print(f'Откуда - {otkuda} \n'
              f'Куда - {kuda} \n'
              f'Дата отправления - {date_time.date()} \n'
              f'Время отправления - {date_time.time()} \n'
              f'Дистанция - {distance} \n'
              f'Скорость - {speed}')
        #self.sql.insert_schedule(schedule, self.train)  # сохранили в базу

    # def formul_distance(self, otk, kud):
    #     x_1 = self.dict_city[otk][0]
    #     x_2 = self.dict_city[otk][1]
    #     y_1 = self.dict_city[kud][0]
    #     y_2 = self.dict_city[kud][1]
    #     return WorkingUtils.distance(x_1, x_2, y_1, y_2)


class MergerData:
    list_type_pas = Passenger.list_type_wagons
    list_type_car = Cargo.list_type_wagons
    list_train_type = TrainBase.list_train_type

    @staticmethod  # забираем нужное кол-во цифр
    def count_num(min_number, max_number):
        return WorkingUtils.count_num(min_number, max_number)

    @staticmethod
    def max_load(type_wagons, count_wagons):
        return WorkingUtils.max_load(type_wagons, count_wagons)


if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.mainloop()