from train_tupe import Passenger, Cargo, Schedule
import math


class WorkingUtils:

    @staticmethod  # регистрация поезда
    def registration_train(nickname, train_type, type_wagons, max, count_wagons, average_speed):
        train = train_type == 'Пассажирский'
        if train:
            obj = Passenger(nickname, train_type, type_wagons, max, count_wagons, average_speed)
        else:
            obj = Cargo(nickname, train_type, type_wagons, max, count_wagons, average_speed)
        return obj

    @staticmethod  # создание расписания
    def registration_schedule(nickname, date_departures, date_arrival, time_departures, time_arrival, time_travel, train_type):
        obj = Schedule(nickname, date_departures, date_arrival, time_departures, time_arrival, time_travel, train_type)
        return obj

    @staticmethod  # возвращает список с нужным кол-вом чисел
    def count_num(num):
        list_numbers = list()
        i = 0
        while i < num:
            i += 1
            list_numbers.append(i)
        return list_numbers

    @staticmethod
    def distance(x_1, x_2, y_1, y_2):
        return math.sqrt(((x_1 - x_2)**2) + ((y_1 - y_2)**2))
        # Minsk = 53.902287, 27.561824
        # Pinsk = 52.111402, 26.102295

    @staticmethod
    def travel_time(distance, a):
        return distance / a

    @staticmethod
    def max_capacity(train, typ_wagon, count_wagons):
        train = train == 'пассажирский'
        if train:
            if typ_wagon == 'общий':
                pass



x_1 = 53.902287
x_2 = 52.111402
y_1 = 27.561824
y_2 = 26.102295

#print(FormulasUtils.distance(x_1, x_2, y_1, y_2))
