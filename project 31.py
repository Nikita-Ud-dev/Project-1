def is_even(number: int):
    even = ("0", "2", "4", "6", "8")
    not_even = ("1", "3", "5", "7", "9")
    string = str(number)

    if string[-1] in even:
        print("#" * 20)
        return True
    elif string[-1] in not_even:
        print("#" * 20)
        return False
    return None

print(is_even(2494563894038**2))#== True, 'Test1'
print(is_even(1056897**2)) #== False, 'Test2'
print(is_even(24945638940387**3)) #== False, 'Test3'
