
ex = "Результат:"
user_input10 = input("Розпочати роботу?(y = так;):")
if user_input10 != "y":
    print("Перевірте введенні данні та спробуйте ще раз.")


while user_input10 == "y":
    user_input1 = float(input("Введіть перше  число:"))
    user_inputX = input("Ввиберіть операцію (+,-,*,/):")
    user_input2 = float(input("Введіть друге число:"))
    if user_inputX == "+":
        print(ex, user_input1 + user_input2)
        user_input11 = input("Продовжити роботу?(y = так; n = ні;) :")
        if user_input11 == "y":
            continue
        elif user_input11 == "n":
            print("Обчислення закінченно")
            break
        else:
            print("Перевірте введенні данні та спробуйте ще раз.")
            break

    elif user_inputX == "-":
        print(ex, user_input1 - user_input2)
        user_input12 = input("Продовжити роботу?(y = так; n = ні;) :")
        if user_input12 == "y":
            continue
        elif user_input12 == "n":
            print("Обчислення закінченно")
            break

        else:
            print("Перевірте введенні данні та спробуйте ще раз.")
            break
    elif user_inputX == "*":
        print(ex, user_input1 * user_input2)
        user_input13 = input("Продовжити роботу?(y = так; n = ні;) :")
        if user_input13 == "y":
            continue
        elif user_input13 == "n":
            print("Обчислення закінченно")
            break
        else:
            print("Перевірте введенні данні та спробуйте ще раз.")
            break
    elif user_inputX == "/":
        print(ex, user_input1 / user_input2)
        user_input14 = input("Продовжити роботу?(y = так; n = ні;) :")
        if user_input14 == "y":
            continue
        elif user_input14 == "n":
            print("Обчислення закінченно")
            break
        else:
            print("Перевірте введенні данні та спробуйте ще раз.")
            break

    else:
        print("Перевірте введенні данні та спробуйте ще раз.")
        break

