import tkinter as tk
from tkinter import ttk
from main import Merger

merger = Merger()
list_count_wagons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_type_train = ['общий', 'плацкарт', 'купе']


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

    def exit(self):
        pass
        # data.save_info_file()
        # self.destroy()


"""Просмотр маршрутов"""


class ViewingRoutes(tk.Toplevel):  # просмотр маршрутов
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Просмотр маршрутов')
        self['bg'] = '#33ffe6'
        self.geometry(f'430x360+500+50')

        self.value_where = tk.StringVar()  # откуда едет пассажир
        self.value_there = tk.StringVar()  # куда едет пассажир
        self.value_days = tk.StringVar()  # в какой день
        self.value_month = tk.StringVar()  # в каком месяце
        self.value_year = tk.StringVar(self, '2023')  # в каком году

        MainMenu.label(self, text='Откуда:').place(x=10, y=10, width=65, height=20)
        MainMenu.label(self, text='Куда:').place(x=10, y=40, width=50, height=20)
        MainMenu.label(self, text='Когда:').place(x=10, y=70, width=60, height=20)

        MainMenu.entry(self, self.value_where).place(x=100, y=10, width=220, height=20)
        MainMenu.entry(self, self.value_there).place(x=100, y=40, width=220, height=20)
        MainMenu.entry(self, self.value_days).place(x=100, y=70, width=30, height=20)
        MainMenu.entry(self, self.value_month).place(x=140, y=70, width=30, height=20)
        MainMenu.entry(self, self.value_year).place(x=180, y=70, width=30, height=20)

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
        self.list_train_type = ['Пассажирский', 'Грузовой']
        self.list_passenger_train = ['общий', 'плацкарт', 'купе']

        MainMenu.label(self, text='Откуда:').place(x=10, y=10, width=65, height=20)
        self.combo1 = ttk.Combobox(self, values=merger.list_city, font=('Arial', 10))
        self.combo1.place(x=190, y=10, width=230, height=20)

        MainMenu.label(self, text='Куда:').place(x=10, y=40, width=50, height=20)
        self.combo2 = ttk.Combobox(self, values=merger.list_city, font=('Arial', 10))
        self.combo2.place(x=190, y=40, width=230, height=20)

        MainMenu.label(self, text='Когда:').place(x=10, y=70, width=60, height=20)
        self.combo3 = ttk.Combobox(self, values=self.list_train_type, font=('Arial', 10))
        self.combo3.place(x=190, y=70, width=230, height=20)

        MainMenu.label(self, text='Выберите тип поезда:').place(x=10, y=100, width=175, height=20)
        self.combo4 = ttk.Combobox(self, values=self.list_train_type, font=('Arial', 10))
        self.combo4.place(x=190, y=100, width=230, height=20)

        MainMenu.button(self, 'Далее', self.open_window).place(x=280, y=130, width=60, height=20)

    def open_window(self):
        if self.combo4.get() == 'Пассажирский':
            window_train = tk.Toplevel()
            window_train.grab_set()
            window_train.geometry(f'430x380+500+50')
            window_train['bg'] = '#33ffe6'
            window_train.title('Создать пассажирский маршрут')

            MainMenu.label(window_train, text='Выберите тип вагонов:\n'
                                      '(общий - 70 мест\n'
                                      ' плацкарт - 54 места\n'
                                      ' купе - 36 мест').place(x=10, y=10, width=200, height=80)
            combo1 = ttk.Combobox(window_train, values=list_type_train, font=('Arial', 10))
            combo1.place(x=220, y=40, width=200, height=20)

            MainMenu.label(window_train, text='Выберите кол-во вагонов:').place(x=10, y=100, width=200, height=20)
            combo2 = ttk.Combobox(window_train, values=list_count_wagons + list_count_wagons, font=('Arial', 10))
            combo2.place(x=220, y=100, width=200, height=20)

            MainMenu.button(window_train, 'Сохранить', self.open_window).place(x=280, y=130, width=60, height=20)
