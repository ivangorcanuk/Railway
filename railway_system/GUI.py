import tkinter as tk
from tkinter import ttk
from main import MainLogic, MergerData
import datetime
import calendar


class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self.mainLogic = MainLogic()
        self.list_city = list()
        for keys in self.mainLogic.dict_city.keys():
            self.list_city.append(keys)
        self.geometry(f'430x360+500+50')
        self.title('Railway')

        # self.img = tk.PhotoImage(file='images/zoo.png')
        # tk.Label(self, image=self.img).pack()

        self.button(self, 'Расписание', self.open_window1).place(x=60, y=30, width=300, height=20)
        self.button(self, 'Поезда', self.open_window2).place(x=60, y=60, width=300, height=20)
        self.button(self, 'Задачи', self.open_window4).place(x=60, y=90, width=300, height=20)
        self.button(self, 'Exit', self.open_window5).place(x=60, y=200, width=300, height=20)

    @staticmethod
    def window():
        window = tk.Toplevel()
        window.grab_set()
        window.geometry(f'430x360+500+50')
        return window

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
    def radiobutton(window, value, variable, com):
        return tk.Radiobutton(window, text=value, font=('Arial', 13), variable=variable, value=value, command=com)

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
        self.parent = parent
        self.dict_train = self.parent.mainLogic.dict_train  # сохранили словарь с поездами
        self.dict_schedule = self.parent.mainLogic.dict_schedule  # сохранили словарь с маршрутами
        self.list_id_train = list()  # создали список с id поездов, у которых есть маршрут
        for key in self.dict_schedule.keys():
            self.list_id_train.append(self.dict_schedule[key][0])  # заполнили его
        self.window_schedule = None  # окно для регистрации маршрута

        self.title('Просмотр расписания')
        self.geometry(f'430x360+500+50')
        self.value_year = tk.StringVar(self, '2023')  # в каком году
        self.combo4 = None  # время отправки (часы)
        self.combo4_1 = None  # время отправки (минуты)
        self.window_train_choose = None  # окно для выбора поездов при регистрации нового маршрута
        self.train = tk.StringVar()  # тот самый поезд которого выберет пользователь
        self.route = None  # выбранный пользователем маршрут

        MainMenu.label(self, text='Откуда:').place(x=10, y=10, width=65, height=20)
        self.combo1 = ttk.Combobox(self, values=self.parent.list_city, font=('Arial', 10))
        self.combo1.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=40, width=50, height=20)
        self.combo2 = ttk.Combobox(self, values=self.parent.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Когда:').place(x=10, y=70, width=60, height=20)
        MainMenu.button(self, 'V', self.open_window4).place(x=140, y=70, width=40, height=20)
        self.combo3 = ttk.Combobox(self, values=MergerData.count_num(1, 31), font=('Arial', 10))
        self.combo3.place(x=190, y=70, width=40, height=20)
        self.combo3_1 = ttk.Combobox(self, values=MergerData.count_num(1, 12), font=('Arial', 10))
        self.combo3_1.place(x=230, y=70, width=40, height=20)
        MainMenu.entry(self, self.value_year).place(x=270, y=70, width=40, height=20)

        self.text = MainMenu.text(self)
        self.update()
        self.text.place(x=10, y=100, width=410, height=220)

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=80, height=20)
        MainMenu.button(self, 'Удалить', self.delete).place(x=160, y=330, width=80, height=20)
        MainMenu.button(self, 'Добавить', self.examination).place(x=250, y=330, width=80, height=20)
        MainMenu.button(self, 'Искать', self.search).place(x=340, y=330, width=80, height=20)

    def open_window4(self):
        calendar = Calendar(self)
        calendar.grab_set()

    def delete(self):  # удаляет маршрут, но не удаляет поезд
        self.parent.mainLogic.delete_schedule(self.route)
        self.update()

    def update(self):  # обновить
        self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне
        for value in self.dict_schedule.values():  # проходим циклом по словарю с маршрутами
            otkuda = value[1] + ' - ' + value[2] + ' - ' + value[3]
            kuda = value[4] + ' - ' + value[5] + ' - ' + value[6]
            self.text.insert('end', f'{value[0]} - {otkuda} \n'
                                    f'              {kuda} \n'
                                    f'              Время в пути - {value[7]} \n')  # выводим строку
            self.text.insert('end', '\n')

    def search(self):  # поиск
        if self.combo1.get() and self.combo2.get() and self.combo3.get() and self.combo3_1.get():
            self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне
            can_not = True
            data = datetime.date(int(self.value_year.get()), int(self.combo3_1.get()), int(self.combo3.get()))
            for key, value in self.dict_schedule.items():
                if value[1] == self.combo1.get() and value[4] == self.combo2.get() and value[2] == str(data):
                    self.route = key
                    otkuda = value[1] + ' - ' + value[2] + ' - ' + value[3]
                    kuda = value[4] + ' - ' + value[5] + ' - ' + value[6]
                    self.text.insert('end', f'{value[0]} - {otkuda} \n'
                                            f'              {kuda} \n'
                                            f'              Время в пути - {value[7]} \n')  # выводим строку
                    self.text.insert('end', '\n')
                    can_not = False
                    break
            if can_not:
                print('erv')
                self.text.insert('end', f' Ничего не найдено')  # выводим строку

    def examination(self):  # проверка на свободные поезда
        for key in self.dict_train.keys():
            if key not in self.dict_schedule.keys():  # есть ли нет первичного ключа поезда среди вторичных ключей маршрутов
                return self.route_registration()
        self.text.delete('1.0', 'end')  # иначе удалили предыдущий текст в текстовом окне
        self.text.insert('end', f' Нет свободного поезда. \n')

    def route_registration(self):  # создали окно для регистрации маршрута
        self.window_schedule = MainMenu.window()

        MainMenu.label(self.window_schedule, text='Откуда:').place(x=10, y=40, width=65, height=20)
        self.combo1 = ttk.Combobox(self.window_schedule, values=self.parent.list_city, font=('Arial', 10))
        self.combo1.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self.window_schedule, text='Куда:').place(x=10, y=70, width=50, height=20)
        self.combo2 = ttk.Combobox(self.window_schedule, values=self.parent.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=70, width=230, height=20)

        MainMenu.label(self.window_schedule, text='Дата отправления:').place(x=10, y=100, width=150, height=20)
        self.combo3 = ttk.Combobox(self.window_schedule, values=MergerData.count_num(1, 31), font=('Arial', 10))
        self.combo3.place(x=190, y=100, width=40, height=20)
        self.combo3_1 = ttk.Combobox(self.window_schedule, values=MergerData.count_num(1, 12), font=('Arial', 10))
        self.combo3_1.place(x=230, y=100, width=40, height=20)
        MainMenu.entry(self.window_schedule, self.value_year).place(x=270, y=100, width=40, height=20)

        MainMenu.label(self.window_schedule, text='Время отправки:').place(x=10, y=130, width=130, height=20)
        self.combo4 = ttk.Combobox(self.window_schedule, values=MergerData.count_num(0, 24), font=('Arial', 10))
        self.combo4.place(x=190, y=130, width=40, height=20)
        self.combo4_1 = ttk.Combobox(self.window_schedule, values=MergerData.count_num(0, 60), font=('Arial', 10))
        self.combo4_1.place(x=230, y=130, width=40, height=20)

        MainMenu.button(self.window_schedule, 'Назад', self.window_schedule.destroy).place(x=10, y=330, width=90, height=20)
        MainMenu.button(self.window_schedule, 'Сохранить', self.wind_train_choose).place(x=330, y=330, width=90, height=20)

    def wind_train_choose(self):
        if self.combo1.get() and self.combo2.get() and self.combo3.get() and self.combo3_1.get() and str(self.combo4.get()) and str(self.combo4_1.get()):
            self.window_train_choose = MainMenu.window()

            MainMenu.label(self.window_train_choose, text='Выберите поезд,\n который поедет по новому маршруту').place(x=10, y=40, width=410, height=50)

            MainMenu.entry(self.window_train_choose, self.train).place(x=145, y=95, width=140, height=20)

            text = MainMenu.text(self.window_train_choose)
            for key, value in self.dict_train.items():
                if key not in self.list_id_train:  # если ли нет первичного ключа поезда среди вторичных ключей маршрутов
                    stroka = key + ' - ' + value[0] + ' - ' + value[1] + ' - ' + \
                             str(value[2]) + ' - ' + str(value[3]) + ' - ' + str(value[4])
                    text.insert('end', f'{stroka}\n')  # выводим строку
            text.place(x=10, y=130, width=410, height=190)

            MainMenu.button(self.window_train_choose, 'Назад', self.window_train_choose.destroy).place(x=10, y=330, width=90, height=20)
            MainMenu.button(self.window_train_choose, 'Сохранить', self.save).place(x=330, y=330, width=90, height=20)

    def save(self):
        if self.train.get():  # добавить, чтобы проверка осуществлялась согласно списку существующих поездов
            data_time = datetime.datetime(int(self.value_year.get()), int(self.combo3_1.get()), int(self.combo3.get()),
                                          int(self.combo4.get()), int(self.combo4_1.get()))
            self.parent.mainLogic.create_schedule(self.combo1.get(), self.combo2.get(), data_time, self.train.get())  # создали маршрут
            self.update()
            self.window_train_choose.destroy()
            self.window_schedule.destroy()


class Calendar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Calendar')
        self.days = []  # в дальнейшем в нем будут храниться поля таблицы. Каждое такое поле соответствует определенному дню.
        self.now = datetime.datetime.now()  # текущая дата
        self.year = self.now.year  # год календаря который в данный момент отображается
        self.month = self.now.month  # месяц календаря которых в данный момент отображается

        prew_button = tk.Button(self, text='<', command=self.prew)
        prew_button.grid(row=0, column=0, sticky='nsew')
        next_button = tk.Button(self, text='>', command=self.next)
        next_button.grid(row=0, column=6, sticky='nsew')
        self.info_label = tk.Label(self, text='0', width=1, height=1,
                              font=('Verdana', 16, 'bold'), fg='blue')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

        for n in range(7):
            lbl = tk.Label(self, text=calendar.day_abbr[n], width=1, height=1,
                           font=('Verdana', 10, 'normal'), fg='darkblue')
            lbl.grid(row=1, column=n, sticky='nsew')
        for row in range(6):
            for col in range(7):
                lbl = tk.Label(self, text='0', width=4, height=2,
                               font=('Arial', 13, 'bold'))
                lbl.grid(row=row + 2, column=col, sticky='nsew')
                self.days.append(lbl)
        self.fill()

    def prew(self):  # вызывается при нажатии на клавишу '<' смены месяца
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next(self):  # вызывается при нажатии на клавишу '>' смены месяца
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def fill(self):  # перерисовывает календарь.
        self.info_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)  # наименование месяца и год
        month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            prew_month_days = calendar.monthrange(self.year - 1, 12)[1]  # Вычисляем количество дней в предыдущем месяце
        else:
            prew_month_days = calendar.monthrange(self.year, self.month - 1)[1]
        week_day = calendar.monthrange(self.year, self.month)[0]  # номер дня недели первого числа месяца
        for n in range(month_days):
            self.days[n + week_day]['text'] = n + 1  # заполняем номера дней выбранного месяца
            self.days[n + week_day]['fg'] = 'black'  # отображать будем их черным цветом
            if self.year == self.now.year and self.month == self.now.month and n == self.now.day:
                self.days[n + week_day]['background'] = 'green'  # если это текущий день, то его фон делаем зелёным
            else:
                self.days[n + week_day]['background'] = 'lightgray'  # иначе светло-серым
        for n in range(week_day):
            self.days[week_day - n - 1]['text'] = prew_month_days - n  # заполняем числа предыдущего месяца
            self.days[week_day - n - 1]['fg'] = 'gray'  # отображать будем их серым цветом
            self.days[week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6 * 7 - month_days - week_day):
            self.days[week_day + month_days + n]['text'] = n + 1  # заполняем числа следующего месяца
            self.days[week_day + month_days + n]['fg'] = 'gray'  # отображать будем их серым цветом
            self.days[week_day + month_days + n]['background'] = '#f3f3f3'


"""Просмотр поездов"""


class TrainView(tk.Toplevel):  # просмотр поездов
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Просмотр поездов')
        self.geometry(f'430x360+500+50')

        self.mainLogic = parent.mainLogic
        self.dict_train = self.mainLogic.dict_train  # сохранили словарь с поездами
        self.window_train = None  # окно для регистрации поездов
        self.train_name = tk.StringVar()  # название поезда
        self.valueStr = tk.StringVar(self, '1')  # тип поезда
        self.load_max = tk.StringVar()  # максимальная нагрузка поезда
        self.wagon_typ = tk.IntVar()  # тип вагонов
        self.wagon_count = tk.StringVar()  # кол-во вагонов
        self.spead = tk.StringVar()  # скорость

        MainMenu.label(self, 'Укажите имя поезда:').place(x=10, y=10, width=180, height=20)
        MainMenu.entry(self, self.train_name).place(x=200, y=10, width=140, height=20)
        MainMenu.button(self, 'Удалить', self.delete).place(x=350, y=10, width=70, height=20)
        MainMenu.label(self, 'Будьте внимательны, вместе с поездом так же \n удалится расписание по которому он ходил!', 'red').place(x=10, y=40, width=410, height=40)

        self.text = MainMenu.text(self)
        self.update()
        self.text.place(x=10, y=120, width=410, height=200)

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=80, height=20)
        MainMenu.button(self, 'Создать', self.tup_choose).place(x=340, y=330, width=80, height=20)

    def update(self):
        self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне
        for key, value in self.dict_train.items():
            stroka = key + ' - ' + value[0] + ' - ' + value[1] + ' - ' + \
                     str(value[2]) + ' - ' + str(value[3]) + ' - ' + str(value[4])
            self.text.insert('end', f'{stroka}\n')  # выводим строку

    def delete(self):  # удалили поезд
        if self.train_name.get() in self.dict_train:
            self.mainLogic.delete_train(self.train_name.get())
            #del self.dict_train[self.train_name.get()]  # удалили из словаря поезд
        self.update()  # обновили окно

    def com(self):  # создали окно для регистрации поезда
        label_text = str()
        wagon_typ = list()
        count_wag = list()
        if self.valueStr.get() == 'пассажирский':
            print('пассажирский')
            label_text = 'Выберите тип вагонов: \n (общий - 70 мест \n плацкарт - 54 места \n купе - 36 мест'
            wagon_typ = MergerData.list_type_pas
            count_wag = MergerData.count_num(1, 20)
        elif self.valueStr.get() == 'грузовой':
            print('грузовой')
            label_text = 'Выберите тип вагонов: \n (открытый - 70т \n закрытый - 50т)'
            wagon_typ = MergerData.list_type_car
            count_wag = MergerData.count_num(1, 50)
        self.train_create(label_text, wagon_typ, count_wag)

    def tup_choose(self):  # выбрать тип поезда
        self.window_train = MainMenu.window()
        self.window_train.title(f'Создать поезд')

        MainMenu.radiobutton(self.window_train, 'пассажирский', self.valueStr, self.com).place(x=50, y=10, width=130, height=20)
        MainMenu.radiobutton(self.window_train, 'грузовой', self.valueStr, self.com).place(x=270, y=10, width=100, height=20)

    def train_create(self, label_text, wagon_typ, count_wag):  # создали окно для регистрации поезда
        self.train_name = tk.StringVar()
        self.spead = tk.StringVar()

        MainMenu.label(self.window_train, text='Укажите название поезда:').place(x=10, y=40, width=200, height=20)
        MainMenu.entry(self.window_train, self.train_name).place(x=220, y=40, width=200, height=20)

        MainMenu.label(self.window_train, text=label_text).place(x=10, y=70, width=200, height=80)
        self.wagon_typ = ttk.Combobox(self.window_train, values=wagon_typ, font=('Arial', 10))
        self.wagon_typ.place(x=220, y=70, width=200, height=20)

        MainMenu.label(self.window_train, text='Выберите кол-во вагонов:').place(x=10, y=160, width=200, height=20)
        self.wagon_count = ttk.Combobox(self.window_train, values=count_wag, font=('Arial', 10))
        self.wagon_count.place(x=220, y=160, width=200, height=20)

        MainMenu.label(self.window_train, text='Укажите скорость:').place(x=10, y=190, width=150, height=20)
        MainMenu.entry(self.window_train, self.spead).place(x=220, y=190, width=200, height=20)

        MainMenu.button(self.window_train, 'Назад',  self.window_train.destroy).place(x=10, y=330, width=60, height=20)
        MainMenu.button(self.window_train, 'Сохранить', self.save).place(x=330, y=330, width=90, height=20)

    def save(self):
        if self.train_name.get() and self.valueStr.get() and self.wagon_typ.get() and self.wagon_count.get() and self.spead.get():
            self.mainLogic.create_train(self.train_name.get(), self.valueStr.get(), str(self.wagon_typ.get()), int(self.wagon_count.get()), self.spead.get())
            print(f'Название - {self.train_name.get()} \n'
                  f'Тип поезда - {self.valueStr.get()} \n'
                  f'Тип вагонов - {self.wagon_typ.get()} \n'
                  f'Кол-во вагонов - {self.wagon_count.get()} \n'
                  f'Макс нагрузка - {MergerData.max_load(str(self.wagon_typ.get()), int(self.wagon_count.get()))} \n'
                  f'Скорость - {self.spead.get()}')
            self.window_train.destroy()
            self.update()


"""Задачи"""


class ScheduleRegistration(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.mainLogic = parent.mainLogic  # сохранили объект класса MainLogic
        self.list_city = parent.list_city  # сохранили список с городами
        self.geometry(f'430x360+500+50')
        self.title('Регистрация расписания')
        self.value_year = tk.StringVar(self, '2023')  # в каком году

        MainMenu.label(self, text='Откуда:').place(x=10, y=40, width=65, height=20)
        self.combo2 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=70, width=50, height=20)
        self.combo3 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.combo3.place(x=190, y=70, width=230, height=20)

        self.text = MainMenu.text(self)
        self.text.insert('end', f'')
        self.text.place(x=10, y=130, width=410, height=160)

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=60, height=20)
        MainMenu.button(self, 'Искать', self.search).place(x=360, y=330, width=60, height=20)

    def search(self):
        print(f'Откуда - {self.combo2.get()} \n'
              f'Куда - {self.combo3.get()}')


# class ScheduleRegistration(tk.Toplevel):  # регистрация расписания
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.mainLogic = parent.mainLogic  # сохранили объект класса MainLogic
#         self.list_city = parent.list_city  # сохранили список с городами
#         self['bg'] = '#33ffe6'
#         self.geometry(f'430x380+500+50')
#         self.title('Регистрация расписания')
#         self.value_year = tk.StringVar(self, '2023')  # в каком году
#
#         MainMenu.label(self, text='Выберите тип поезда:').place(x=10, y=10, width=175, height=20)
#         self.combo1 = ttk.Combobox(self, values=MergerData.list_train_type, font=('Arial', 10))
#         self.combo1.place(x=190, y=10, width=230, height=20)
#
#         MainMenu.label(self, text='Откуда:').place(x=10, y=40, width=65, height=20)
#         self.combo2 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
#         self.combo2.place(x=190, y=40, width=230, height=20)
#
#         MainMenu.label(self, text='Куда:').place(x=10, y=70, width=50, height=20)
#         self.combo3 = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
#         self.combo3.place(x=190, y=70, width=230, height=20)
#
#         MainMenu.label(self, text='Когда:').place(x=10, y=100, width=60, height=20)
#         self.combo4 = ttk.Combobox(self, values=MergerData.count_num(31), font=('Arial', 10))
#         self.combo4.place(x=190, y=100, width=40, height=20)
#         self.combo4_1 = ttk.Combobox(self, values=MergerData.count_num(12), font=('Arial', 10))
#         self.combo4_1.place(x=230, y=100, width=40, height=20)
#         MainMenu.entry(self, self.value_year).place(x=270, y=100, width=40, height=20)
#
#         MainMenu.label(self, text='Время отправки:').place(x=10, y=130, width=130, height=20)
#         self.combo5 = ttk.Combobox(self, values=MergerData.count_num(24), font=('Arial', 10))
#         self.combo5.place(x=190, y=130, width=40, height=20)
#         self.combo5_1 = ttk.Combobox(self, values=MergerData.count_num(59), font=('Arial', 10))
#         self.combo5_1.place(x=230, y=130, width=40, height=20)
#
#         self.combo6 = None
#         self.combo7 = None
#
#         MainMenu.button(self, 'Далее', self.open_window).place(x=280, y=160, width=60, height=20)
#
#     def open_window(self):
#         tp = self.combo1.get() == 'пассажирский'
#         if tp:
#             window_train = self.create_window()
#
#             MainMenu.label(window_train, text='Выберите тип вагонов:\n'
#                                       '(общий - 70 мест\n'
#                                       ' плацкарт - 54 места\n'
#                                       ' купе - 36 мест').place(x=10, y=10, width=200, height=80)
#             self.combo6 = ttk.Combobox(window_train, values=MergerData.list_type_pas, font=('Arial', 10))
#             self.combo6.place(x=220, y=40, width=200, height=20)
#
#             MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=100, width=200, height=20)
#             self.combo7 = ttk.Combobox(window_train, values=MergerData.count_num(20), font=('Arial', 10))
#             self.combo7.place(x=220, y=100, width=200, height=20)
#
#         else:
#             window_train = self.create_window()
#
#             MainMenu.label(window_train, text='Выберите тип вагонов:\n'
#                                               '(открытый\n'
#                                               ' закрытый').place(x=10, y=10, width=200, height=80)
#             self.combo6 = ttk.Combobox(window_train, values=MergerData.list_type_car, font=('Arial', 10))
#             self.combo6.place(x=220, y=40, width=200, height=20)
#
#             MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=100, width=200, height=20)
#             self.combo7 = ttk.Combobox(window_train, values=MergerData.count_num(50), font=('Arial', 10))
#             self.combo7.place(x=220, y=100, width=200, height=20)
#
#     def create_window(self):  # создание окна
#         window_train = tk.Toplevel()
#         window_train.grab_set()
#         window_train.geometry(f'430x380+500+50')
#         window_train['bg'] = '#33ffe6'
#         window_train.title(f'Создать {self.combo1.get()} маршрут')
#         MainMenu.button(window_train, 'Сохранить', self.save).place(x=280, y=130, width=60, height=20)
#         return window_train
#
#     def save(self):
#         nickname = self.combo2.get() + ' - ' + self.combo3.get()  # название поезда
#         train_type = self.combo1.get()  # тип поезда пассажирский/грузовой
#         type_wagons = self.combo6.get()  # тип поезда общий/плацкарт/купе либо вагонов открытый/закрытый
#         count_wagons = int(self.combo7.get())  # кол-во вагонов
#         max_load = MergerData.max_load(type_wagons, count_wagons)  # максималтная нагрузка
#         average_speed = 100
#         date_sending = self.combo4.get() + '-' + self.combo4_1.get() + '-' + self.value_year.get()  # дата отправления
#         time_sending = datetime.timedelta(hours=int(self.combo5.get()), minutes=int(self.combo5_1.get()))  # время отправления
#         distance = self.mainLogic.formul_distance(self.combo2.get(), self.combo3.get())  # нашли расстояние
#         travel_time = datetime.timedelta(hours=distance // average_speed, minutes=distance % average_speed)  # время в пути
#         time_arrival = time_sending + travel_time
#
#         self.mainLogic.create_train(nickname, train_type, type_wagons, count_wagons, average_speed)  # создали поезд
#         self.mainLogic.create_schedule(date_sending, time_sending, time_arrival, travel_time)  # создали поезд
#
#         print(f'Название поезда - {nickname} \n'
#               f'Тип поезда - {train_type} \n'
#               f'Максимальная нагрузка - {max_load} \n'
#               f'Кол-во вагонов - {count_wagons} \n'
#               f'Дата отправления - {date_sending} \n'
#               f'Время отправления - {time_sending} \n'
#               f'Время прибытия - {time_sending + travel_time} \n'
#               f'Км - {distance} \n'
#               f'Веря в пути - {travel_time}')