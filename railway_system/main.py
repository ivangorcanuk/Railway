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

from GUI import *
from data import WorkingUtils
from SQLite import SQL


class MergerSQL:
    def __init__(self):
        self.sql = SQL()
        self.dict_city = self.sql.select_cities()  # вытянули словарь с городами

    def create_train(self, nickname, train_type, type_wagons, max, count_wagons, average_speed):  # создаем поезд
        train = WorkingUtils.registration_train(nickname, train_type, type_wagons, max, count_wagons, average_speed)
        self.sql.insert_train(train)  # сохранили в базу

    def create_schedule(self, nickname, date_departures, date_arrival,
                        time_departures, time_arrival, time_travel, train_type):  # создаем расписание
        schedule = WorkingUtils.registration_schedule(nickname, date_departures, date_arrival,
                                                      time_departures, time_arrival, time_travel, train_type)
        self.sql.insert_train(schedule)  # сохранили в базу

    def formul_distance(self, otk, kud):
        x_1 = self.dict_city[otk][0]
        x_2 = self.dict_city[otk][1]
        y_1 = self.dict_city[kud][0]
        y_2 = self.dict_city[kud][1]
        return WorkingUtils.distance(x_1, x_2, y_1, y_2)


class MergerData:
    def __init__(self):
        self.list_num = 0

    @staticmethod  # забираем нужное кол-во цифр
    def count_num(num):
        return WorkingUtils.count_num(num)
# menu1 = input('номер поезда')
# menu2 = input('название поезда')
# menu3 = input('тип поезда')
# menu4 = str()
# menu5_1 = str()
# menu5_2 = str()
# menu6 = str()
# if menu3 == 'Пассажирский':
#     menu4 = input('тип пассажирского поезда')
#     menu5_1 = input('кол-во пассажиров')
#     menu6 = input('кол-во вагонов')
# elif menu3 == 'Грузовой':
#     menu5_2 = input('максимально перевозимый вес')
#     menu6 = input('кол-во вагонов')
#
# obj = WorkingUtils.registration_train(menu1, menu2, menu3, menu4, menu5_1, menu5_2, menu6)
# print(obj.nickname)


if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.mainloop()