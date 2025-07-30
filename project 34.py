def decorator(func):
    number_test = 0

    def func1(*args, **kwargs):
        nonlocal number_test
        number_test += 1
        print("#" * 20)
        print(f"Test{number_test}")
        return func(*args, **kwargs)
    return func1


class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
       self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

        # if max_max >= self.max_value:
        #     return max_max

    def set_min(self, min_min):
        self.min_value = min_min

        # if min_min >= self.min_value:
        #     return min_min

    def step_up(self):
        # form self.current in range(self.min_value, self.max_value):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимум")
        self.current += 1

    def step_down(self):
        # for self.current in range(self.min_value, self.max_value, -1):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто минимум")
        self.current -= 1

    def get_current(self):
        return self.current

    @decorator
    def show_result(self):
        print("#" * 20)
        print(f"Рахунок значення:{self.current}")


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

counter.show_result()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)# Достигнут максимум

counter.show_result()
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

counter.show_result()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум

counter.show_result()
assert counter.get_current() == 7, 'Test4'

