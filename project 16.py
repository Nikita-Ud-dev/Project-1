
user_input = int(input("Введіть ціле число:"))
lst = list(str(user_input))

while user_input >= 9:
    result = 1
    for number in lst:
       result = result * int(number)
    user_input = result
    lst = list(str(user_input))

print(user_input)
