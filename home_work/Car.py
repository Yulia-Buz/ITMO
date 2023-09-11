class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def year_of_manuf(self):
        print(self.year)

    def car_type(self):
        print(self.type)

    def car_color(self):
        print(self.color)

Auto = Car('зеленый', 'седан', '2019')
Auto.start()
Auto.stop()
Auto.year_of_manuf()
Auto.car_type()
Auto.car_color()
