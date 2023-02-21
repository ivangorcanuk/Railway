import tkinter as tk
from tkinter import ttk
from main import MergerSQL, MergerData
import datetime


class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self.mainLogic = MergerSQL()
        self.list_city = list()
        for keys in self.mainLogic.dict_city.keys():
            self.list_city.append(keys)
        self.geometry(f'430x360+500+50')
        self.title('Railway')

        # self.img = tk.PhotoImage(file='images/zoo.png')
        # tk.Label(self, image=self.img).pack()

        self.button(self, 'Расписание', self.open_window1).place(x=60, y=30, width=300, height=20)
        self.button(self, 'Поезда', self.open_window2).place(x=60, y=60, width=300, height=20)
        self.button(self, 'Зарегестрировать маршрут', self.open_window4).place(x=60, y=120, width=300, height=20)
        self.button(self, 'Exit', self.open_window5).place(x=60, y=200, width=300, height=20)

    @staticmethod
    def button(window, text, command):
        return tk.Button(window, text=text, font=('Arial', 13), command=command)

    @staticmethod
    def label(window, text, color='black'):
        return tk.Label(window, text=text, font=('Arial', 13), foreground=color)

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
        viewing_schedule = ViewingSchedule(self)
        viewing_schedule.grab_set()

    def open_window2(self):
        train_view = TrainView(self)
        train_view.grab_set()

    def open_window4(self):
        create_route = ScheduleRegistration(self)
        create_route.grab_set()

    def open_window5(self):
        self.destroy()


"""Просмотр расписания"""


class ViewingSchedule(tk.Toplevel):  # просмотр расписания
    def __init__(self, parent):
        super().__init__(parent)
        self.list_city = parent.list_city
        self.title('Просмотр расписания')
        self.geometry(f'430x360+500+50')
        self.value_year = tk.StringVar(self, '2023')  # в каком году
        self.valueStr = tk.StringVar(self, '1')
        self.combo4 = None  # время отправки (часы)
        self.combo4_1 = None  # время отправки (минуты)

        MainMenu.label(self, text='Откуда:').place(x=10, y=10, width=65, height=20)
        self.combo1 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.combo1.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=40, width=50, height=20)
        self.combo2 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Когда:').place(x=10, y=70, width=60, height=20)
        self.combo3 = ttk.Combobox(self, values=MergerData.count_num(31), font=('Arial', 10))
        self.combo3.place(x=190, y=70, width=40, height=20)
        self.combo3_1 = ttk.Combobox(self, values=MergerData.count_num(12), font=('Arial', 10))
        self.combo3_1.place(x=230, y=70, width=40, height=20)
        MainMenu.entry(self, self.value_year).place(x=270, y=70, width=40, height=20)

        MainMenu.radiobutton(self, 'пассажирский', self.valueStr).place(x=50, y=100, width=130, height=20)
        MainMenu.radiobutton(self, 'грузовой', self.valueStr).place(x=250, y=100, width=90, height=20)

        self.text = MainMenu.text(self)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=10, y=130, width=410, height=190)

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=80, height=20)
        MainMenu.button(self, 'Добавить', self.window).place(x=250, y=330, width=80, height=20)
        MainMenu.button(self, 'Искать', self.search).place(x=340, y=330, width=80, height=20)

    def search(self):
        print(self.valueStr.get())

    def window(self):  # создали окно для регистрации маршрута
        window_schedule = tk.Toplevel()
        window_schedule.grab_set()
        window_schedule.geometry(f'430x360+500+50')
        window_schedule.title(f'Создать новый маршрут')

        MainMenu.label(window_schedule, text='Откуда:').place(x=10, y=40, width=65, height=20)
        self.combo1 = ttk.Combobox(window_schedule, values=self.list_city, font=('Arial', 10))
        self.combo1.place(x=190, y=40, width=230, height=20)

        MainMenu.label(window_schedule, text='Куда:').place(x=10, y=70, width=50, height=20)
        self.combo2 = ttk.Combobox(window_schedule, values=self.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=70, width=230, height=20)

        MainMenu.label(window_schedule, text='Дата отправления:').place(x=10, y=100, width=60, height=20)
        self.combo3 = ttk.Combobox(window_schedule, values=MergerData.count_num(31), font=('Arial', 10))
        self.combo3.place(x=190, y=100, width=40, height=20)
        self.combo3_1 = ttk.Combobox(window_schedule, values=MergerData.count_num(12), font=('Arial', 10))
        self.combo3_1.place(x=230, y=100, width=40, height=20)
        MainMenu.entry(window_schedule, self.value_year).place(x=270, y=100, width=40, height=20)

        MainMenu.label(window_schedule, text='Время отправки:').place(x=10, y=130, width=130, height=20)
        self.combo4 = ttk.Combobox(window_schedule, values=MergerData.count_num(24), font=('Arial', 10))
        self.combo4.place(x=190, y=130, width=40, height=20)
        self.combo4_1 = ttk.Combobox(window_schedule, values=MergerData.count_num(59), font=('Arial', 10))
        self.combo4_1.place(x=230, y=130, width=40, height=20)

        MainMenu.button(window_schedule, 'Назад', window_schedule.destroy).place(x=10, y=330, width=90, height=20)
        MainMenu.button(window_schedule, 'Сохранить', self.save).place(x=330, y=330, width=90, height=20)

    def save(self):
        date_sending = self.combo3.get() + '-' + self.combo3_1.get() + '-' + self.value_year.get()  # дата отправления
        time_sending = datetime.timedelta(hours=int(self.combo4.get()), minutes=int(self.combo4_1.get()))  # время отправления
        print(f'Откуда - {self.combo1.get()} \n'
              f'Куда - {self.combo2.get()} \n'
              f'Дата отправления - {date_sending} \n'
              f'Время отправления - {time_sending}')


"""Просмотр поездов"""


class TrainView(tk.Toplevel):  # просмотр поездов
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Просмотр поездов')
        self.geometry(f'430x360+500+50')

        self.train_name = tk.StringVar()  # название поезда
        self.valueStr = tk.StringVar(self, '1')  # тип поезда (радиокнопка)
        self.load_max = tk.StringVar()  # максимальная нагрузка поезда
        self.wagon_typ = tk.IntVar()  # тип вагонов
        self.wagon_count = tk.StringVar()  # кол-во вагонов
        self.spead = tk.StringVar()  # скорость

        MainMenu.label(self, 'Укажите имя поезда:').place(x=10, y=10, width=180, height=20)
        MainMenu.entry(self, self.train_name).place(x=200, y=10, width=140, height=20)
        MainMenu.button(self, 'Удалить', self.destroy).place(x=350, y=10, width=70, height=20)
        MainMenu.label(self, 'Будьте внимательны, вместе с поездом так же \n удалится расписание по которому он ходил!', 'red').place(x=10, y=40, width=410, height=40)

        MainMenu.radiobutton(self, 'пассажирский', self.valueStr).place(x=50, y=90, width=130, height=20)
        MainMenu.radiobutton(self, 'грузовой', self.valueStr).place(x=250, y=90, width=90, height=20)

        self.text = MainMenu.text(self)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=10, y=120, width=410, height=200)

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=60, height=20)
        MainMenu.button(self, 'Искать', self.search).place(x=360, y=330, width=60, height=20)
        MainMenu.button(self, 'Создать', self.train_create).place(x=280, y=330, width=70, height=20)

    def search(self):
        print(self.train_name.get(), self.valueStr.get())

    def train_create(self):
        if self.valueStr.get() == MergerData.list_train_type[0]:
            count_wag = MergerData.count_num(20)  # вытянули список с цифрами из которых пользователь выберет кол-во ыагонов
            window_train = self.window(count_wag)

            MainMenu.label(window_train, text='Выберите тип вагонов:\n'
                                              '(общий - 70 мест\n'
                                              ' плацкарт - 54 места\n'
                                              ' купе - 36 мест').place(x=10, y=40, width=200, height=80)
            self.wagon_typ = ttk.Combobox(window_train, values=MergerData.list_type_pas, font=('Arial', 10))
            self.wagon_typ.place(x=220, y=70, width=200, height=20)

        elif self.valueStr.get() == MergerData.list_train_type[1]:
            count_wag = MergerData.count_num(50)
            window_train = self.window(count_wag)

            MainMenu.label(window_train, text='Выберите тип вагонов:\n'
                                              '(открытый - 70т\n'
                                              ' закрытый - 50т)').place(x=10, y=40, width=200, height=80)
            self.wagon_typ = ttk.Combobox(window_train, values=MergerData.list_type_car, font=('Arial', 10))
            self.wagon_typ.place(x=220, y=70, width=200, height=20)

    def save(self):
        print(f'Название - {self.train_name.get()} \n'
              f'Тип поезда - {self.valueStr.get()} \n'
              f'Тип вагонов - {self.wagon_typ.get()} \n'
              f'Кол-во вагонов - {self.wagon_count.get()} \n'
              f'Макс нагрузка - {MergerData.max_load(str(self.wagon_typ.get()), int(self.wagon_count.get()))} \n'
              f'Скорость - {self.spead.get()}')

    def window(self, count_wag):  # создали окно для регистрации поезда
        window_train = tk.Toplevel()
        window_train.grab_set()
        window_train.geometry(f'430x360+500+50')
        window_train.title(f'Создать {MergerData.list_train_type[0]} поезд')

        MainMenu.label(window_train, text='Укажите название поезда:').place(x=10, y=10, width=200, height=20)
        MainMenu.entry(window_train, self.train_name).place(x=220, y=10, width=200, height=20)

        MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=130, width=200, height=20)
        self.wagon_count = ttk.Combobox(window_train, values=count_wag, font=('Arial', 10))
        self.wagon_count.place(x=220, y=130, width=200, height=20)

        MainMenu.label(window_train, text='Укажите скорость:').place(x=10, y=160, width=150, height=20)
        MainMenu.entry(window_train, self.spead).place(x=220, y=160, width=200, height=20)

        MainMenu.button(window_train, 'Назад', window_train.destroy).place(x=10, y=330, width=60, height=20)
        MainMenu.button(window_train, 'Сохранить', self.save).place(x=330, y=330, width=90, height=20)
        return window_train


"""Регистрация расписания"""


class ScheduleRegistration(tk.Toplevel):  # регистрация расписания
    def __init__(self, parent):
        super().__init__(parent)
        self.mainLogic = parent.mainLogic  # сохранили объект класса MergerSQL
        self.list_city = parent.list_city  # сохранили список с городами
        self['bg'] = '#33ffe6'
        self.geometry(f'430x380+500+50')
        self.title('Регистрация расписания')
        self.value_year = tk.StringVar(self, '2023')  # в каком году

        MainMenu.label(self, text='Выберите тип поезда:').place(x=10, y=10, width=175, height=20)
        self.combo1 = ttk.Combobox(self, values=MergerData.list_train_type, font=('Arial', 10))
        self.combo1.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Откуда:').place(x=10, y=40, width=65, height=20)
        self.combo2 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=70, width=50, height=20)
        self.combo3 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
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
            self.combo6 = ttk.Combobox(window_train, values=MergerData.list_type_pas, font=('Arial', 10))
            self.combo6.place(x=220, y=40, width=200, height=20)

            MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=100, width=200, height=20)
            self.combo7 = ttk.Combobox(window_train, values=MergerData.count_num(20), font=('Arial', 10))
            self.combo7.place(x=220, y=100, width=200, height=20)

        else:
            window_train = self.create_window()

            MainMenu.label(window_train, text='Выберите тип вагонов:\n'
                                              '(открытый\n'
                                              ' закрытый').place(x=10, y=10, width=200, height=80)
            self.combo6 = ttk.Combobox(window_train, values=MergerData.list_type_car, font=('Arial', 10))
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
        nickname = self.combo2.get() + ' - ' + self.combo3.get()  # название поезда
        train_type = self.combo1.get()  # тип поезда пассажирский/грузовой
        type_wagons = self.combo6.get()  # тип поезда общий/плацкарт/купе либо вагонов открытый/закрытый
        count_wagons = int(self.combo7.get())  # кол-во вагонов
        max_load = MergerData.max_load(type_wagons, count_wagons)  # максималтная нагрузка
        average_speed = 100
        date_sending = self.combo4.get() + '-' + self.combo4_1.get() + '-' + self.value_year.get()  # дата отправления
        time_sending = datetime.timedelta(hours=int(self.combo5.get()), minutes=int(self.combo5_1.get()))  # время отправления
        distance = self.mainLogic.formul_distance(self.combo2.get(), self.combo3.get())  # нашли расстояние
        travel_time = datetime.timedelta(hours=distance // average_speed, minutes=distance % average_speed)  # время в пути
        time_arrival = time_sending + travel_time

        self.mainLogic.create_train(nickname, train_type, type_wagons, count_wagons, average_speed)  # создали поезд
        self.mainLogic.create_schedule(date_sending, time_sending, time_arrival, travel_time)  # создали поезд

        print(f'Название поезда - {nickname} \n'
              f'Тип поезда - {train_type} \n'
              f'Максимальная нагрузка - {max_load} \n'
              f'Кол-во вагонов - {count_wagons} \n'
              f'Дата отправления - {date_sending} \n'
              f'Время отправления - {time_sending} \n'
              f'Время прибытия - {time_sending + travel_time} \n'
              f'Км - {distance} \n'
              f'Веря в пути - {travel_time}')