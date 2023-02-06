from train_tupe import Passenger, Cargo


class WorkingUtils:

    @staticmethod
    def registration_train(number, nickname, train_type, max_capacity_pas, max_weight, type_passenger_train, count_wagons):
        obj = None
        if train_type == 'Пассажирский':
            obj = Passenger(number, nickname, train_type, max_capacity_pas, type_passenger_train, count_wagons)
        elif train_type == 'Грузовой':
            obj = Cargo(number, nickname, train_type, max_weight, count_wagons)
        return obj

    @staticmethod
    def formation_train():
        pass
        # list_count_wagons = list()
        # for i in