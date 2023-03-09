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

# Продумать

from GUI import *
from SQLite import DBhandler
from train_tupe import Passenger, Cargo, Schedule, TrainBase, WorkingUtils
import datetime


class MainLogic:
    def __init__(self):
        self.__sql = DBhandler()
        self.dict_city = self.__sql.select_cities()  # вытянули словарь с городами
        self.dict_train = self.__sql.select_train()  # вытянули словарь с поездами
        self.dict_schedule = self.__sql.select_schedule()  # вытянули словарь с маршрутами

    def create_train(self, nickname, train_type, type_wagons, count_wagons, average_speed):  # создаем поезд
        max_load = WorkingUtils.max_load(type_wagons, count_wagons)  # вернули максимальную нагрузку
        if train_type == TrainBase.list_train_type[0]:  # если поезд пассажирский
            train = Passenger(nickname, train_type, type_wagons, max_load, count_wagons, average_speed)
        else:
            train = Cargo(nickname, train_type, type_wagons, max_load, count_wagons, average_speed)
        self.dict_train[nickname] = (train_type, type_wagons, max_load, count_wagons, average_speed)
        #self.__sql.insert_train(train)  # сохранили в базу

    def create_schedule(self, otkuda, kuda, date_time, train_name):  # создаем расписание
        distance = WorkingUtils.distance(self.dict_city, otkuda, kuda)  # нашли дистанцию
        speed = self.dict_train[train_name][4]  # сохранили скорость
        travel_time = datetime.timedelta(hours=distance // speed, minutes=distance % speed)  # время в пути
        date_time_arrival = date_time + travel_time  # дата прибытия
        schedule = Schedule(otkuda, date_time.date(), date_time.time(),
                                            kuda, date_time_arrival.date(), date_time_arrival.time(), travel_time)
        id_schedule = WorkingUtils.id_installation(self.dict_schedule)
        self.dict_schedule[id_schedule] = (train_name, otkuda, str(date_time.date()), str(date_time.time()),
                                            kuda, str(date_time_arrival.date()), str(date_time_arrival.time()), str(travel_time))
        self.__sql.insert_schedule(id_schedule, train_name, schedule)  # сохранили в базу

    def delete_train(self, nickname):  # удаляем поезд
        self.__sql.delete_train(nickname)  # из базы
        del self.dict_train[nickname]  # из словаря

    def delete_schedule(self, iD):  # удаляем поезд
        self.__sql.delete_schedule(iD)  # из базы
        del self.dict_schedule[iD]  # из словаря


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