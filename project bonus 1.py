def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """
    count = 0
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            nonlocal count
            result = None
            for _ in range(repeat_count):
                result = func(*args, **kwargs)
                count += 1
            return result

        def inner_function():
            return count

        wrapped_func.get_count1 = inner_function
        return wrapped_func
    return wrapper

@repeat_decorator(4)
def example_function(a=1, b=2):
    return a , b

print(example_function())
print(example_function.get_count1())