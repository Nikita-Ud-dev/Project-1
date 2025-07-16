def is_even(digit: int):
    """ Перевірка чи є парним число """
    print("#" * 20)
    return digit % 2 == 0

    # if result == 0:
    #     print("#" * 20)
    #     return True
    # elif result > 0:
    #     print("#" * 20)
    #     return False
    # return None

print(is_even(2)) #== True, 'Test1'
print(is_even(5)) #== False, 'Test2'
print(is_even(0)) #== True, 'Test3'

