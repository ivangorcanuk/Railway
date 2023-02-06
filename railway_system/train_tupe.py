class Instrumen:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


"""Базовый класс с общей информацией о всех поездах"""


class MainInf:
    number = Instrumen()  # номер поезда
    nickname = Instrumen()  # название поезда
    train_type = Instrumen()  # тип поезда пассажирский(True)/грузовой(False)

    def __init__(self, number, nickname, train_type):
        self._number = number
        self._nickname = nickname
        self._train_type = train_type

    # def __gt__(self, other):
    #     return self._weight < other


"""Классы делящие поезда на пассажирские/грузовые"""


class Passenger(MainInf):  # пассажирский
    max_capacity_pas = Instrumen()  # максималтная вместимость пассажиров
    type_passenger_train = Instrumen()  # тип поезда общий/плацкарт/купе
    count_wagons = Instrumen()  # кол-во вагонов

    def __init__(self, number, nickname, train_type, max_capacity_pas, type_passenger_train, count_wagons):
        super().__init__(number, nickname, train_type)
        self._max_capacity_pas = max_capacity_pas
        self._type_passenger_train = type_passenger_train
        self._count_wagons = count_wagons


class Cargo(MainInf):  # грузовой
    max_weight = Instrumen()  # максималтно перевозимый вес
    count_wagons = Instrumen()  # кол-во вагонов

    def __init__(self, number, nickname, train_type, max_weight, count_wagons):
        super().__init__(number, nickname, train_type)
        self._max_weight = max_weight
        self._count_wagons = count_wagons