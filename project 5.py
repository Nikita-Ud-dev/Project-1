user_input1 = float(input("Введіть перше  число:"))
user_inputX = input("Ввиберіть операцію (+,-,*,/):")
user_input2 = float(input("Введіть друге число:"))

ex = "Результат:"

if user_inputX == "+":
    print(ex, user_input1 + user_input2)
elif user_inputX == "-":
    print(ex, user_input1 - user_input2)
elif user_inputX == "*":
    print(ex, user_input1 * user_input2)
elif user_inputX == "/":
    print(ex, user_input1 / user_input2)
else:
    print("Перевірте введенні данні та спробуйте ще раз.")





