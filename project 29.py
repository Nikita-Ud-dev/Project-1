import math

def prime_generator(end: int):
    for number1 in range(2, end + 1):
        result = math.sqrt(number1)
        for number in range(2, int(result) + 1):
            x = number1 % number
            if x == 0:
                break
        else:
            yield number1

from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen)) #== True, 'Test0'
print(list(prime_generator(10))) #== [2, 3, 5, 7], 'Test1'
print(list(prime_generator(15))) #== [2, 3, 5, 7, 11, 13], 'Test2'
print(list(prime_generator(29))) #== [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'


# def numbers(digit: int):
#     if digit < 2:
#         return False
#     for digit1 in range(2, int(digit ** 0.5) + 1):
#         if digit % digit1 == 0:
#             return False
#     return True

# if numbers(number):