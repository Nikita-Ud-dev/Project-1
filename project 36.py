def decorator(func):
    number_test = 0

    def wrapper(*args, **kwargs):
        nonlocal number_test
        number_test += 1
        print("#" * 20)
        print(f"Test{number_test}")
        return func(*args, **kwargs)
    return wrapper


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    # def get_width(self):
    #     width = self.get_square() / self.height
    #     return width
    #
    # def get_height(self):
    #     height = self.get_square() / self.width
    #     return height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        s = self.get_square() + other.get_square()
        # y = Rectangle(self.get_width(), self.get_height())
        # y = self.get_width() * self.get_height()
        # x1 = Rectangle(self.get_width(), self.get_height())
        # x2 = x / self.height
        # x4 = x / self.width
        height = s / self.get_square()
        width = s / height
        # print(height * width)
        # print(other.get_winth * other.get_height)
        if height * width == s:
            return Rectangle(width, height)
        raise ValueError("Не правильне значення")


    def __mul__(self, n):
        new_s = self.get_square() * n
        height = new_s / self.get_square()
        width = new_s / height
        # print(height * width == new_s)
        if height * width == new_s:
            return Rectangle(width, height)
        raise ValueError("Не правильнe значення")
    @decorator
    def __str__(self):
        return (f"Площа прямокутника: {self.get_square()}\n"
                f"Висота прямокутника: {self.height}\n"
                f"Ширина прямокутника: {self.width}")


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1)
assert r1.get_square() == 8, 'Test1'
print(r2)
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
print(r3)
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
print(r4)
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
