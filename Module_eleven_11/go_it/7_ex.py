# Реалізуйте для класу Vector операції додавання та віднімання векторів.
# Тобто перевизначите для нього математичні оператори __add__ та __sub__
#
# Є два вектори: a з координатами (x1, y1) та b з координатами (x2, y2).
#
# Тоді додавання векторів b + a - це новий вектор з координатами (x2 + x1, y2 + y1).
# Віднімання – зворотна операція, b - a - це новий вектор з координатами (x2 - x1, y2 - y1)

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        result_x = self.coordinates.x + vector.coordinates.x
        result_y = self.coordinates.y + vector.coordinates.y
        b = Point(result_x,result_y)
        return Vector(b)

    def __sub__(self, vector):
        result_x = self.coordinates.x - vector.coordinates.x
        result_y = self.coordinates.y - vector.coordinates.y
        a = Point(result_x,result_y)
        return Vector(a)

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
