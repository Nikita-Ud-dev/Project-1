
user_input = int(input("Введіть чотирьох значне число:"))

if user_input < -1:
    print("Введіть чотирьох значне число вище -1")
else:
    print("Так все правильно")

if user_input > 9999:
    print("Введіть чотирьох значне число нижче 10000")
else:
    print("Так все правильно")

number0 = (user_input // 1000)
number1 = (user_input // 100)
number2 = (user_input // 10)
number3 = (user_input % 10)

ex = (number1 % 10)
ex1 = (number2 % 10)

print(number0)
print(ex)
print(ex1)
print(number3)