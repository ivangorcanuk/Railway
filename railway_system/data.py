from train_tupe import Passenger, Cargo, Schedule


class WorkingUtils:

    @staticmethod  # регистрация поезда
    def registration_train(number, nickname, train_type, max_capacity_pas, max_weight,
                           type_passenger_train, count_wagons, average_speed, type_wagons):
        train = train_type == 'Пассажирский'
        if train:
            obj = Passenger(number, nickname, train_type, max_capacity_pas, type_passenger_train, count_wagons, average_speed)
        else:
            obj = Cargo(number, nickname, train_type, max_weight, count_wagons, average_speed, type_wagons)
        return obj

    @staticmethod  # создание расписания
    def registration_schedule(nickname, date_departures, date_arrival, time_departures, time_arrival, time_travel, train_type):
        obj = Schedule(nickname, date_departures, date_arrival, time_departures, time_arrival, time_travel, train_type)
        return obj

    @staticmethod
    def count_num(num):
        list_numbers = list()
        i = 0
        while i < num:
            i += 1
            list_numbers.append(i)
        return list_numbers