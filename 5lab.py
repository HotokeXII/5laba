#ЛАБА №5
#задание 1: базовый класс и методы
import datetime


class Book():
    title = ''
    author = ''
    year = 0
    def get_info(self):
        print('название книги:', self.title, '; автор:', self.author, '; год издания:', self.year)
x = Book()
x.title = 'русские яйца'
x.author = 'шальной шкибидист'
x.year = 2025
x.get_info()

#задание 2: работа с конструктором
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
circle = Circle(10)
print('радиус равен', circle.get_radius())
circle.set_radius(15)
print('измененный радиус равен', circle.get_radius())