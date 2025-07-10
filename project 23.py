def find_unique_value(some_list: list):
    for number in some_list: # Перебераю елементи в списку
        if some_list.count(number) == 1: # Умова: якщо елемент зустрічаеться лише раз то він і є унікальнім.
            print("#" * 20)
            return number
    print("#" * 20)
    return "В списку немає унікального числа"



print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))