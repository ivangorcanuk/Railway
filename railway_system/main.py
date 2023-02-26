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
import datetime


class MergerSQL:
    def __init__(self):
        self.sql = DBhandler()
        self.dict_city = self.sql.select_cities()  # вытянули словарь с городами
        self.dict_train = self.sql.select_train()  # вытянули словарь с поездами
        self.dict_schedule = self.sql.select_schedule()  # вытянули словарь с маршрутами

    def create_train(self, nickname, train_type, type_wagons, count_wagons, average_speed):  # создаем поезд
        max_load = WorkingUtils.max_load(type_wagons, count_wagons)  # вернули максимальную нагрузку
        train = WorkingUtils.registration_train(nickname, train_type, type_wagons, max_load, count_wagons, average_speed)
        id = WorkingUtils.id_installation(self.dict_train)
        print(id, train.nickname, train.train_type, train.type_wagons,
              train.max_load, train.count_wagons, train.average_speed)
        self.sql.insert_train(id, train)  # сохранили в базу

    def create_schedule(self, otkuda, kuda, date_time, train_name):  # создаем расписание
        distance = WorkingUtils.distance(self.dict_city, otkuda, kuda)
        id_train = int()
        for key, value in self.dict_train.items():
            if value[0] == str(train_name):
                id_train = key
        speed = self.dict_train[id_train][5]  # сохранили скорость
        travel_time = datetime.timedelta(hours=distance // speed, minutes=distance % speed)  # время в пути
        date_time_arrival = date_time + travel_time  # дата прибытия
        id_schedule = WorkingUtils.id_installation(self.dict_schedule)
        schedule = WorkingUtils.registration_schedule(otkuda, date_time.date(), date_time.time(),
                                            kuda, date_time_arrival.date(), date_time_arrival.time(), travel_time)
        print(f'Откуда - {schedule.otkuda} \n'
              f'Дата отправления - {schedule.date_sending} \n'
              f'Время отправления - {schedule.time_sending} \n'
              f'Куда - {schedule.kuda} \n'
              f'Дата прибытия - {schedule.date_arrival} \n'
              f'Время прибытия - {schedule.time_arrival} \n'
              f'Дистанция - {distance} \n'
              f'Скорость - {speed} \n'
              f'Время в пути - {schedule.time_travel} \n'
              f'id - {id_schedule}')
        self.sql.insert_schedule(id_schedule, id_train, schedule)  # сохранили в базу


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