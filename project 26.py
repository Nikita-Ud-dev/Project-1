def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    stop = 0
    while stop < end:
        yield begin
        x1 = func(begin)
        begin = x1
        stop += 1

    print("#" * 20)
from inspect import isgenerator

gen = some_gen(2, 4, pow)
print(isgenerator(gen)) #== True, 'Test1'
print(list(gen)) #== [2, 4, 16, 256], 'Test2'
print('OK')