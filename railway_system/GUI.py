import tkinter as tk
from tkinter import ttk
from main import MergerSQL, MergerData
import datetime

mergerSQL = MergerSQL()
mergerData = MergerData()
list_city = list()
for keys in mergerSQL.dict_city.keys():
    list_city.append(keys)


class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self.geometry(f'430x360+500+50')
        self.title('Zoo')

        # self.img = tk.PhotoImage(file='images/zoo.png')
        # tk.Label(self, image=self.img).pack()

        self.button(self, 'Посмотреть маршруты', self.open_window1).place(x=60, y=30, width=300, height=20)
        self.button(self, 'Создать маршрут', self.open_window2).place(x=60, y=60, width=300, height=20)
        self.button(self, 'Exit', self.destroy).place(x=60, y=150, width=300, height=20)

    @staticmethod
    def button(window, text, command):
        return tk.Button(window, text=text, font=('Arial', 13), command=command)

    @staticmethod
    def label(window, text):
        return tk.Label(window, text=text, font=('Arial', 13))

    @staticmethod
    def entry(window, variable):
        return tk.Entry(window, font=('Arial', 10), textvariable=variable)

    @staticmethod
    def radiobutton(window, value, variable):
        return tk.Radiobutton(window, text=value, font=('Arial', 13), variable=variable, value=value)

    @staticmethod
    def text(window):
        return tk.Text(window, font=('Arial', 13), bg='#a5a29c')

    def open_window1(self):
        viewing_routes = ViewingRoutes(self)
        viewing_routes.grab_set()

    def open_window2(self):
        create_route = CreateRoute(self)
        create_route.grab_set()


"""Просмотр маршрутов"""


class ViewingRoutes(tk.Toplevel):  # просмотр маршрутов
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Просмотр маршрутов')
        self['bg'] = '#33ffe6'
        self.geometry(f'430x360+500+50')
        self.value_year = tk.StringVar(self, '2023')  # в каком году

        MainMenu.label(self, text='Откуда:').place(x=10, y=10, width=65, height=20)
        self.combo1 = ttk.Combobox(self, values=list_city, font=('Arial', 10))
        self.combo1.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=40, width=50, height=20)
        self.combo2 = ttk.Combobox(self, values=list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Когда:').place(x=10, y=70, width=60, height=20)
        self.combo1 = ttk.Combobox(self, values=MergerData.count_num(31), font=('Arial', 10))
        self.combo1.place(x=100, y=70, width=40, height=20)
        self.combo1 = ttk.Combobox(self, values=MergerData.count_num(12), font=('Arial', 10))
        self.combo1.place(x=140, y=70, width=40, height=20)
        MainMenu.entry(self, self.value_year).place(x=180, y=70, width=40, height=20)

        MainMenu.button(self, 'Искать', self.open_window3).place(x=280, y=70, width=60, height=20)

        self.text = MainMenu.text(self)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=10, y=100, width=410, height=250)

    def open_window3(self):
        pass


"""Создать маршрут"""


class CreateRoute(tk.Toplevel):  # создать маршрут
    def __init__(self, parent):
        super().__init__(parent)
        self['bg'] = '#33ffe6'
        self.geometry(f'430x380+500+50')
        self.title('Создать маршрут')
        self.value_year = tk.StringVar(self, '2023')  # в каком году

        MainMenu.label(self, text='Выберите тип поезда:').place(x=10, y=10, width=175, height=20)
        self.combo1 = ttk.Combobox(self, values=mergerData.list_train_type, font=('Arial', 10))
        self.combo1.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Откуда:').place(x=10, y=40, width=65, height=20)
        self.combo2 = ttk.Combobox(self, values=list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=70, width=50, height=20)
        self.combo3 = ttk.Combobox(self, values=list_city, font=('Arial', 10))
        self.combo3.place(x=190, y=70, width=230, height=20)

        MainMenu.label(self, text='Когда:').place(x=10, y=100, width=60, height=20)
        self.combo4 = ttk.Combobox(self, values=MergerData.count_num(31), font=('Arial', 10))
        self.combo4.place(x=190, y=100, width=40, height=20)
        self.combo4_1 = ttk.Combobox(self, values=MergerData.count_num(12), font=('Arial', 10))
        self.combo4_1.place(x=230, y=100, width=40, height=20)
        MainMenu.entry(self, self.value_year).place(x=270, y=100, width=40, height=20)

        MainMenu.label(self, text='Время отправки:').place(x=10, y=130, width=130, height=20)
        self.combo5 = ttk.Combobox(self, values=MergerData.count_num(24), font=('Arial', 10))
        self.combo5.place(x=190, y=130, width=40, height=20)
        self.combo5_1 = ttk.Combobox(self, values=MergerData.count_num(59), font=('Arial', 10))
        self.combo5_1.place(x=230, y=130, width=40, height=20)

        self.combo6 = None
        self.combo7 = None

        MainMenu.button(self, 'Далее', self.open_window).place(x=280, y=160, width=60, height=20)

    def open_window(self):
        tp = self.combo1.get() == 'пассажирский'
        if tp:
            window_train = self.create_window()

            MainMenu.label(window_train, text='Выберите тип вагонов:\n'
                                      '(общий - 70 мест\n'
                                      ' плацкарт - 54 места\n'
                                      ' купе - 36 мест').place(x=10, y=10, width=200, height=80)
            self.combo6 = ttk.Combobox(window_train, values=mergerData.list_type_pas, font=('Arial', 10))
            self.combo6.place(x=220, y=40, width=200, height=20)

            MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=100, width=200, height=20)
            self.combo7 = ttk.Combobox(window_train, values=MergerData.count_num(20), font=('Arial', 10))
            self.combo7.place(x=220, y=100, width=200, height=20)

        else:
            window_train = self.create_window()

            MainMenu.label(window_train, text='Выберите тип вагонов:\n'
                                              '(открытый\n'
                                              ' закрытый').place(x=10, y=10, width=200, height=80)
            self.combo6 = ttk.Combobox(window_train, values=mergerData.list_type_car, font=('Arial', 10))
            self.combo6.place(x=220, y=40, width=200, height=20)

            MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=100, width=200, height=20)
            self.combo7 = ttk.Combobox(window_train, values=MergerData.count_num(50), font=('Arial', 10))
            self.combo7.place(x=220, y=100, width=200, height=20)

    def create_window(self):  # создание окна
        window_train = tk.Toplevel()
        window_train.grab_set()
        window_train.geometry(f'430x380+500+50')
        window_train['bg'] = '#33ffe6'
        window_train.title(f'Создать {self.combo1.get()} маршрут')
        MainMenu.button(window_train, 'Сохранить', self.save).place(x=280, y=130, width=60, height=20)
        return window_train

    def save(self):
        otk = self.combo2.get()
        kud = self.combo3.get()
        nickname = self.combo2.get() + ' - ' + self.combo3.get()  # название поезда
        train_type = self.combo1.get()  # тип поезда пассажирский/грузовой
        type_wagons = self.combo6.get()  # тип поезда общий/плацкарт/купе либо вагонов открытый/закрытый
        count_wagons = int(self.combo7.get())  # кол-во вагонов
        max_load = MergerData.max_load(type_wagons, count_wagons)  # максималтная нагрузка
        average_speed = 100
        date_sending = self.combo4.get() + '-' + self.combo4_1.get() + '-' + self.value_year.get()  # дата отправления
        time_sending = datetime.timedelta(hours=int(self.combo5.get()), minutes=int(self.combo5_1.get()))  # время отправления
        distance = mergerSQL.formul_distance(otk, kud)  # км
        travel_time = datetime.timedelta(hours=distance // average_speed, minutes=distance % average_speed)  # время в пути
        time_arrival = time_sending + travel_time
        # time_sending = str(time_sending)
        # time_arrival = str(time_arrival)
        # travel_time = str(travel_time)
        # time_sending = time_sending[0:4]
        # time_arrival = time_arrival[0:4]
        # travel_time = travel_time[0:4]

        mergerSQL.create_train(nickname, train_type, type_wagons, count_wagons, average_speed)  # создали поезд
        mergerSQL.create_schedule(nickname, date_sending, time_sending, time_arrival, travel_time, train_type)  # создали поезд

        print(f'Название поезда - {nickname} \n'
              f'Тип поезда - {train_type} \n'
              f'Максимальная нагрузка - {max_load} \n'
              f'Кол-во вагонов - {count_wagons} \n'
              f'Дата отправления - {date_sending} \n'
              f'Время отправления - {time_sending} \n'
              f'Время прибытия - {time_sending + travel_time} \n'
              f'Км - {distance} \n'
              f'Веря в пути - {travel_time}')