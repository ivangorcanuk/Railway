from math import radians, cos, sin, asin, sqrt


class Instrumen:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


"""Базовый класс с общей информацией о всех поездах"""


class TrainBase:
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


class Passenger(TrainBase):  # пассажирский
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


class Cargo(TrainBase):  # грузовой
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


class Schedule:  # расписание
    otkuda = Instrumen()  # откуда едет поезд
    date_sending = Instrumen()  # дата отправления
    time_sending = Instrumen()  # время отправления
    kuda = Instrumen()  # куда едет поезд
    date_arrival = Instrumen()  # дата прибытия
    time_arrival = Instrumen()  # время прибытия
    time_travel = Instrumen()  # время в пути

    def __init__(self, otkuda, date_sending, time_sending, kuda, date_arrival, time_arrival, time_travel):
        self._otkuda = otkuda
        self._date_sending = date_sending
        self._time_sending = time_sending
        self._kuda = kuda
        self._date_arrival = date_arrival
        self._time_arrival = time_arrival
        self._time_travel = time_travel


class WorkingUtils:

    @staticmethod  # возвращает список с нужным кол-вом чисел
    def count_num(min_number, max_number):
        list_numbers = list()
        i = 0
        while i < max_number:
            i += 1
            list_numbers.append(i)
        if min_number:
            return list_numbers
        else:
            list_numbers.insert(0, 0)
            return list_numbers  # добавили 0 в начале списка

    @staticmethod
    def distance(dict_city, otk, kud):
        lat1 = dict_city[otk][0]
        lon1 = dict_city[otk][1]
        lat2 = dict_city[kud][0]
        lon2 = dict_city[kud][1]
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

    @staticmethod
    def id_installation(dict_id):
        i = 0
        while i <= len(dict_id) + 1:
            i += 1
            if i not in dict_id.keys():
                return i
