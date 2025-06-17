user_input = int(input("Введіть п'яти значне число:"))

number0 = (user_input % 10)
number1 = (user_input // 10)
number2 = (user_input // 100)
number3 = (user_input // 1000)
number4 = (user_input // 10000)

ex1 = (number1 % 10)
ex2 = (number2 % 10)
ex3 = (number3 % 10)

print(number0,ex1,ex2,ex3,number4)