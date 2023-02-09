class Instrumen:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


"""Базовый класс с общей информацией о всех поездах"""


class MainInf:
    nickname = Instrumen()  # название поезда
    train_type = Instrumen()  # тип поезда пассажирский(True)/грузовой(False)
    average_speed = Instrumen()  # средняя скорость

    def __init__(self, nickname=str(), train_type=str(), average_speed=100):
        self._nickname = nickname
        self._train_type = train_type
        self._average_speed = average_speed

    # def __gt__(self, other):
    #     return self._weight < other


"""Классы делящие поезда на пассажирские/грузовые"""


class Passenger(MainInf):  # пассажирский
    max_capacity_pas = Instrumen()  # максималтная вместимость пассажиров
    type_passenger_train = Instrumen()  # тип поезда общий/плацкарт/купе
    count_wagons = Instrumen()  # кол-во вагонов

    def __init__(self, nickname, train_type, max_capacity_pas, type_passenger_train, count_wagons, average_speed):
        super().__init__(nickname, train_type, average_speed)
        self._max_capacity_pas = max_capacity_pas
        self._type_passenger_train = type_passenger_train
        self._count_wagons = count_wagons


class Cargo(MainInf):  # грузовой
    max_weight = Instrumen()  # максималтно перевозимый вес
    type_wagons = Instrumen()  # тип вагонов открытый/закрытый
    count_wagons = Instrumen()  # кол-во вагонов

    def __init__(self, nickname, train_type, max_weight, count_wagons, average_speed, type_wagons):
        super().__init__(nickname, train_type, average_speed)
        self._max_weight = max_weight
        self._count_wagons = count_wagons
        self._type_wagons = type_wagons


class Schedule(MainInf):  # расписание
    date_departures = Instrumen()  # дата отправления
    date_arrival = Instrumen()  # дата прибытия
    time_departures = Instrumen()  # время отправления
    time_arrival = Instrumen()  # время прибытия
    time_travel = Instrumen()  # время в пути

    def __init__(self, nickname, date_departures, date_arrival, time_departures, time_arrival, time_travel, train_type):
        super().__init__(nickname, train_type)
        self._date_departures = date_departures
        self._date_arrival = date_arrival
        self._time_departures = time_departures
        self._time_arrival = time_arrival
        self._time_travel = time_travel