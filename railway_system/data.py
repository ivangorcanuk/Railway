from train_tupe import Passenger, Cargo, Schedule, MainInf
from math import radians, cos, sin, asin, sqrt


class WorkingUtils:

    @staticmethod  # регистрация поезда
    def registration_train(nickname, train_type, type_wagons, max, count_wagons, average_speed):
        if train_type == MainInf.list_train_type[0]:  # если поезд пассажирский
            return Passenger(nickname, train_type, type_wagons, max, count_wagons, average_speed)
        else:
            return Cargo(nickname, train_type, type_wagons, max, count_wagons, average_speed)

    @staticmethod  # создание расписания
    def registration_schedule(nickname, date_sending, time_sending, time_arrival, time_travel, train_type):
        return Schedule(nickname, str(date_sending), str(time_sending)[0:4], str(time_arrival)[0:4], str(time_travel)[0:4], train_type)

    @staticmethod  # возвращает список с нужным кол-вом чисел  
    def count_num(num):
        list_numbers = list()
        i = 0
        while i < num:
            i += 1
            list_numbers.append(i)
        return list_numbers

    @staticmethod
    def distance(lat1, lon1, lat2, lon2):
        lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))  # преобразовать десятичные градусы в радианы
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2  # формула гаверсинуса
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        return round(km)  # округлили

    @staticmethod
    def max_load(typ_wagon, count_wagons):
        if typ_wagon == Passenger.list_type_wagons[0]:  # если тип вагонов общий
            return count_wagons * Passenger.list_count_places[0]
        elif typ_wagon == Passenger.list_type_wagons[1]:  # если тип вагонов плацкар
            return count_wagons * Passenger.list_count_places[1]
        elif typ_wagon == Passenger.list_type_wagons[2]:  # если тип вагонов купе
            return count_wagons * Passenger.list_count_places[2]
        elif typ_wagon == Cargo.list_type_wagons[0]:  # если тип вагонов открытый
            return count_wagons * Cargo.list_max_load[0]
        elif typ_wagon == Cargo.list_type_wagons[1]:  # если тип вагонов закрытый
            return count_wagons * Cargo.list_max_load[0]


x_1 = 53.902287
x_2 = 52.111402
y_1 = 27.561824
y_2 = 26.102295

#print(FormulasUtils.distance(x_1, x_2, y_1, y_2))