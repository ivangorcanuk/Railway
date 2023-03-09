from tkinter import *
from tkinter import ttk
from main import MainLogic, MergerData
import datetime
import calendar
# при создании маршрута не видит поезда, которые были заняты маршрутом ранее
# добавить список со свободными поездами в окно рачпичания и передовать его как парамет в функцию
# убрать лишний селф в переменных
# переименовать переменные и функции
# убрать повторение перменных в разных окнах
# наладить удаление
# добавить листбокс вместо текстового окна

class MainMenu(Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self.mainLogic = MainLogic()
        self.geometry(f'430x360+500+50')
        self.title('Railway')

        self.button(self, 'Расписание', self.viewing_schedule).place(x=60, y=30, width=300, height=20)
        self.button(self, 'Поезда', self.train_view).place(x=60, y=60, width=300, height=20)
        self.button(self, 'Exit', self.destroy).place(x=60, y=200, width=300, height=20)

    def viewing_schedule(self):
        viewing_schedule = ViewingSchedule(self)
        viewing_schedule.grab_set()

    def train_view(self):
        train_view = TrainView(self)
        train_view.grab_set()

    @staticmethod
    def window():
        window = Toplevel()
        window.grab_set()
        window.geometry(f'430x360+500+50')
        return window

    @staticmethod
    def button(window, text, command):
        return Button(window, text=text, font=('Arial', 13), command=command)

    @staticmethod
    def label(window, text, color='black'):
        return Label(window, text=text, font=('Arial', 13), foreground=color)

    @staticmethod
    def entry(window, variable):
        return Entry(window, font=('Arial', 10), textvariable=variable)

    @staticmethod
    def radiobutton(window, value, variable, com):
        return Radiobutton(window, text=value, font=('Arial', 13), variable=variable, value=value, command=com)

    @staticmethod
    def text(window):
        return Text(window, font=('Arial', 13), bg='#a5a29c')


"""Просмотр расписания"""


class ViewingSchedule(Toplevel):  # просмотр расписания
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.list_city = list()  # список с названиями городов
        for keys in self.parent.mainLogic.dict_city.keys():
            self.list_city.append(keys)
        self.dict_train = self.parent.mainLogic.dict_train  # сохранили словарь с поездами
        self.dict_schedule = self.parent.mainLogic.dict_schedule  # сохранили словарь с маршрутами
        self.list_id_train = list()  # создали список с id поездов, у которых есть маршрут
        for key in self.dict_schedule.keys():
            self.list_id_train.append(self.dict_schedule[key][0])  # заполнили его
        self.value_year = StringVar(self, '2023')  # в каком году

        self.title('Просмотр расписания')
        self.geometry(f'430x360+500+50')
        # self.window_schedule = None  # окно для регистрации маршрута
        # self.dispatch_time_hours = None  # время отправки (часы)
        # self.dispatch_time_minutes = None  # время отправки (минуты)
        # self.window_train_choose = None  # окно для выбора поездов при регистрации нового маршрута
        # self.train = StringVar()  # тот самый поезд которого выберет пользователь
        # self.route = None  # выбранный пользователем маршрут

        MainMenu.label(self, text='Откуда:').place(x=10, y=10, width=65, height=20)
        self.otkuda = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.otkuda.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=40, width=50, height=20)
        self.kuda = ttk.Combobox(self, values=self.list_city, font=('Arial', 10))
        self.kuda.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Когда:').place(x=10, y=70, width=60, height=20)
        MainMenu.button(self, 'V', self.open_window4).place(x=140, y=70, width=40, height=20)
        self.dispatch_day = ttk.Combobox(self, values=MergerData.count_num(1, 31), font=('Arial', 10))
        self.dispatch_day.place(x=190, y=70, width=40, height=20)  # день отправки
        self.dispatch_month = ttk.Combobox(self, values=MergerData.count_num(1, 12), font=('Arial', 10))
        self.dispatch_month.place(x=230, y=70, width=40, height=20)  # месяц отправки
        MainMenu.entry(self, self.value_year).place(x=270, y=70, width=40, height=20)  # год отправки

        self.update()

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=80, height=20)
        MainMenu.button(self, 'Удалить', self.delete).place(x=160, y=330, width=80, height=20)
        MainMenu.button(self, 'Добавить', self.examination).place(x=250, y=330, width=80, height=20)
        MainMenu.button(self, 'Искать', self.search).place(x=340, y=330, width=80, height=20)

    def open_window4(self):
        calendar = Calendar(self)
        calendar.grab_set()

    def delete(self):  # удаляет маршрут, но не удаляет поезд
        print(self.route)
        self.parent.mainLogic.delete_schedule(self.route)
        self.update()

    def update(self):  # обновить
        listbox_city = Variable(value=self.list_city)
        text = Listbox(self, font=('Arial', 13))
        for i in self.dict_schedule:  # проходим циклом по словарю с маршрутами
            otkuda = self.dict_schedule[i][1] + ' - ' + self.dict_schedule[i][2] + ' - ' + self.dict_schedule[i][3]
            kuda = self.dict_schedule[i][4] + ' - ' + self.dict_schedule[i][5] + ' - ' + self.dict_schedule[i][6]
            route = f'{otkuda} \n {kuda} \n Время в пути - {self.dict_schedule[i][7]} \n'
            text.insert(i, route)  # выводим строку
            #text.inser
        text.place(x=10, y=100, width=410, height=220)
        # self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне
        # for value in self.dict_schedule.values():  # проходим циклом по словарю с маршрутами
        #     otkuda = value[1] + ' - ' + value[2] + ' - ' + value[3]
        #     kuda = value[4] + ' - ' + value[5] + ' - ' + value[6]
        #     self.text.insert('end', f'{value[0]} - {otkuda} \n'
        #                             f'              {kuda} \n'
        #                             f'              Время в пути - {value[7]} \n')  # выводим строку
        #     self.text.insert('end', '\n')

    def search(self):  # поиск
        if self.otkuda.get() and self.kuda.get() and self.dispatch_day.get() and self.dispatch_month.get():
            self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне
            can_not = True
            data = datetime.date(int(self.value_year.get()), int(self.combo3_1.get()), int(self.combo3.get()))
            for key, value in self.dict_schedule.items():
                if value[1] == self.combo1.get() and value[4] == self.combo2.get() and value[2] == str(data):
                    route = key
                    otkuda = value[1] + ' - ' + value[2] + ' - ' + value[3]
                    kuda = value[4] + ' - ' + value[5] + ' - ' + value[6]
                    self.text.insert('end', f'{value[0]} - {otkuda} \n'
                                            f'              {kuda} \n'
                                            f'              Время в пути - {value[7]} \n')  # выводим строку
                    self.text.insert('end', '\n')
                    can_not = False
                    break
            if can_not:
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
        self.combo41 = ttk.Combobox(self.window_schedule, values=MergerData.count_num(0, 24), font=('Arial', 10))
        self.combo41.place(x=190, y=130, width=40, height=20)
        self.combo4_1 = ttk.Combobox(self.window_schedule, values=MergerData.count_num(0, 60), font=('Arial', 10))
        self.combo4_1.place(x=230, y=130, width=40, height=20)

        MainMenu.button(self.window_schedule, 'Назад', self.window_schedule.destroy).place(x=10, y=330, width=90, height=20)
        MainMenu.button(self.window_schedule, 'Сохранить', self.wind_train_choose).place(x=330, y=330, width=90, height=20)

    def wind_train_choose(self):
        if self.combo1.get() and self.combo2.get() and self.combo3.get() and self.combo3_1.get() and str(self.combo41.get()) and str(self.combo4_1.get()):
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
                                          int(self.combo41.get()), int(self.combo4_1.get()))
            self.parent.mainLogic.create_schedule(self.combo1.get(), self.combo2.get(), data_time, self.train.get())  # создали маршрут
            self.update()
            self.window_train_choose.destroy()
            self.window_schedule.destroy()


class Calendar(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Calendar')
        self.days = []  # в дальнейшем в нем будут храниться поля таблицы. Каждое такое поле соответствует определенному дню.
        self.now = datetime.datetime.now()  # текущая дата
        self.year = self.now.year  # год календаря который в данный момент отображается
        self.month = self.now.month  # месяц календаря которых в данный момент отображается

        prew_button = Button(self, text='<', command=self.prew)
        prew_button.grid(row=0, column=0, sticky='nsew')
        next_button = Button(self, text='>', command=self.next)
        next_button.grid(row=0, column=6, sticky='nsew')
        self.info_label = Label(self, text='0', width=1, height=1,
                              font=('Verdana', 16, 'bold'), fg='blue')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

        for n in range(7):
            lbl = Label(self, text=calendar.day_abbr[n], width=1, height=1,
                           font=('Verdana', 10, 'normal'), fg='darkblue')
            lbl.grid(row=1, column=n, sticky='nsew')
        for row in range(6):
            for col in range(7):
                lbl = Label(self, text='0', width=4, height=2,
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


class TrainView(Toplevel):  # просмотр поездов
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Просмотр поездов')
        self.geometry(f'430x360+500+50')

        self.mainLogic = parent.mainLogic
        self.dict_train = self.mainLogic.dict_train  # сохранили словарь с поездами
        self.list_train = list()
        for key in self.dict_train.keys():
            self.list_train.insert(0, key)  # заполнили список именами поездов

        MainMenu.button(self, 'Удалить', self.delete).place(x=250, y=330, width=80, height=20)
        MainMenu.label(self, 'Будьте внимательны, вместе с поездом так же \n удалится расписание по которому он ходил!', 'red').place(x=10, y=30, width=410, height=40)

        self.text = self.updat()

        MainMenu.button(self, 'Назад', self.destroy).place(x=10, y=330, width=80, height=20)
        MainMenu.button(self, 'Создать', self.tup_choose).place(x=340, y=330, width=80, height=20)

    def updat(self):
        text = Listbox(self, font=('Arial', 13))
        for key, value in self.dict_train.items():  # проходим циклом по словарю с маршрутами
            train = key + ' - ' + value[0] + ' - ' + value[1] + ' - ' + str(value[2])\
                    + ' - ' + str(value[3]) + ' - ' + str(value[4])
            text.insert(0, train)  # выводим строку
        text.place(x=10, y=100, width=410, height=220)
        return text

    def delete(self):  # удалили поезд
        selection = self.text.curselection()
        if len(selection) > 0:
            self.mainLogic.delete_train(self.list_train[selection[0]])  # удалили поезд из базы и словаря
            self.text.delete(selection[0])

    def com(self, window_train, train_typ):  # создали окно для регистрации поезда
        label_text = str()
        list_wagon_typ = list()
        list_count_wag = list()
        if train_typ.get() == 'пассажирский':
            label_text = 'Выберите тип вагонов: \n (общий - 70 мест \n плацкарт - 54 места \n купе - 36 мест'
            list_wagon_typ = MergerData.list_type_pas
            list_count_wag = MergerData.count_num(1, 20)
        elif train_typ.get() == 'грузовой':
            label_text = 'Выберите тип вагонов: \n (открытый - 70т \n закрытый - 50т)'
            list_wagon_typ = MergerData.list_type_car
            list_count_wag = MergerData.count_num(1, 50)
        self.train_create(window_train, train_typ, label_text, list_wagon_typ, list_count_wag)

    def tup_choose(self):  # выбрать тип поезда
        window_train = MainMenu.window()
        window_train.title(f'Создать поезд')
        train_typ = StringVar(window_train, '1')  # тип поезда

        MainMenu.radiobutton(window_train, 'пассажирский', train_typ, lambda: self.com(window_train, train_typ)).place(x=50, y=10, width=130, height=20)
        MainMenu.radiobutton(window_train, 'грузовой', train_typ, lambda: self.com(window_train, train_typ)).place(x=270, y=10, width=100, height=20)

    def train_create(self, window_train, train_typ, label_text, list_wagon_typ, list_count_wag):  # создали окно для регистрации поезда
        train_name = StringVar()
        spead = StringVar()

        MainMenu.label(window_train, text='Укажите название поезда:').place(x=10, y=40, width=200, height=20)
        MainMenu.entry(window_train, train_name).place(x=220, y=40, width=200, height=20)

        MainMenu.label(window_train, text=label_text).place(x=10, y=70, width=200, height=80)
        wagon_typ = ttk.Combobox(window_train, values=list_wagon_typ, font=('Arial', 10))
        wagon_typ.place(x=220, y=70, width=200, height=20)

        MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=160, width=200, height=20)
        count_wag = ttk.Combobox(window_train, values=list_count_wag, font=('Arial', 10))
        count_wag.place(x=220, y=160, width=200, height=20)

        MainMenu.label(window_train, text='Укажите скорость:').place(x=10, y=190, width=150, height=20)
        MainMenu.entry(window_train, spead).place(x=220, y=190, width=200, height=20)

        MainMenu.button(window_train, 'Назад',  window_train.destroy).place(x=10, y=330, width=60, height=20)
        MainMenu.button(window_train, 'Сохранить', lambda: self.save(window_train, train_name, train_typ, wagon_typ, count_wag, spead)).place(x=330, y=330, width=90, height=20)

    def save(self, window_train, train_name, train_typ, wagon_typ, count_wag, spead):
        if train_name.get() and train_typ.get() and wagon_typ.get() and count_wag.get() and spead.get():
            self.mainLogic.create_train(train_name.get(), train_typ.get(), str(wagon_typ.get()), int(count_wag.get()), int(spead.get()))
            # print(f'Название - {train_name.get()} \n'
            #       f'Тип поезда - {train_typ.get()} \n'
            #       f'Тип вагонов - {wagon_typ.get()} \n'
            #       f'Кол-во вагонов - {count_wag.get()} \n'
            #       f'Макс нагрузка - {MergerData.max_load(str(wagon_typ.get()), int(count_wag.get()))} \n'
            #       f'Скорость - {spead.get()}')
            window_train.destroy()
            self.list_train.insert(0, train_name.get())  # добавили новый поезд в список названий поездов
            self.text = self.updat()