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
    list_train_type = ['пассажирский', 'грузовой']

    def __init__(self, nickname=str(), train_type=str(), average_speed=int()):
        self._nickname = nickname
        self._train_type = train_type
        self._average_speed = average_speed

    # def __gt__(self, other):
    #     return self._weight < other


"""Классы делящие поезда на пассажирские/грузовые"""


class Passenger(MainInf):  # пассажирский
    max_load = Instrumen()  # максималтная вместимость пассажиров
    type_wagons = Instrumen()  # тип поезда общий/плацкарт/купе
    count_wagons = Instrumen()  # кол-во вагонов
    list_type_wagons = ['общий', 'плацкарт', 'купе']
    list_count_places = [70, 54, 36]

    def __init__(self, nickname=str(), train_type=str(), type_wagons=str(), max_load=int(), count_wagons=str(), average_speed=str()):
        super().__init__(nickname, train_type, average_speed)
        self._max_load = max_load
        self._type_wagons = type_wagons
        self._count_wagons = count_wagons


class Cargo(MainInf):  # грузовой
    max_load = Instrumen()  # максималтно перевозимый вес
    type_wagons = Instrumen()  # тип вагонов открытый/закрытый
    count_wagons = Instrumen()  # кол-во вагонов
    list_type_wagons = ['открытый', 'крытый']
    list_max_load = [70, 60]

    def __init__(self, nickname, train_type, type_wagons, max_load, count_wagons, average_speed):
        super().__init__(nickname, train_type, average_speed)
        self._max_load = max_load
        self._count_wagons = count_wagons
        self._type_wagons = type_wagons


class Schedule(MainInf):  # расписание
    date_sending = Instrumen()  # дата отправления
    time_sending = Instrumen()  # время отправления
    time_arrival = Instrumen()  # время прибытия
    time_travel = Instrumen()  # время в пути

    def __init__(self, nickname, date_sending, time_sending, time_arrival, time_travel, train_type):
        super().__init__(nickname, train_type)
        self._date_sending = date_sending
        self._time_sending = time_sending
        self._time_arrival = time_arrival
        self._time_travel = time_travel