def decorator(func):
    number_test = 0

    def wrapper(*args, **kwargs):
        nonlocal number_test
        number_test += 1
        print("#" * 20)
        print(f"Test{number_test}")
        return func(*args, **kwargs)
    return wrapper

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __add__(self, other):
        if self.b == other.b:
            result = self.a + other.a
            return Fraction(result, self.b)
        else:
            denominator = self.b * other.b

            new_number1 = self.a * (denominator // self.b)
            new_number2 = other.a * (denominator // other.b)

            result_numerator = new_number1 + new_number2

            # divider = math.gcd(result_numerator, denominator)

            # final_numerator = result_numerator // divider
            # final_denominator = denominator // divider
            # self.a = final_numerator
            # self.b = final_denominator
            return Fraction(result_numerator, denominator)

    def __sub__(self, other):
        if self.b == other.b:
            result = self.a - other.a
            return Fraction(result, self.b)
        else:
            denominator = self.b * other.b

            new_number1 = self.a * (denominator // self.b)
            new_number2 = other.a * (denominator // other.b)

            result_numerator = new_number1 - new_number2

            return Fraction(result_numerator, denominator)

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

    @decorator
    def show_result(self):
        print(f"Fraction: {self.a}, {self.b}")

    @decorator
    def show_true(self, operator, opject1):
        if operator == "==":
            print(self.a / self.b == opject1.a / opject1.b)
        elif operator == ">":
            print(self.a / self.b > opject1.a / opject1.b)
        elif operator == "<":
            print(self.a / self.b < opject1.a / opject1.b)
        elif operator == "!=":
            print(self.a / self.b != opject1.a / opject1.b)

x = Fraction
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
x.show_result(f_c)

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
x.show_result(f_d)

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
x.show_result(f_e)

assert f_d < f_c  # True
x.show_true(f_d,"<", f_c)

assert f_d > f_e  # True
x.show_true(f_d,">", f_e)

assert f_a != f_b  # True
x.show_true(f_a,"!=", f_b)

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)

assert f_1 == f_2  # True
x.show_true(f_1, "==", f_2)
print('OK')
