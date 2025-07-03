

user_input = int(input("Введіть ціле число:"))

while True:
    if user_input > 8639999:
        print("Перевірте введенні данні та спробуйте ще раз.")
        break
    elif user_input < 0:
        print("Перевірте введенні данні та спробуйте ще раз.")
        break

    else:
        minute = 60
        hour = 60 * 60
        day = 24 * 60 * 60

        day1 = user_input // day
        day2 = user_input % day
        hour1 = day2 // hour
        hour2 = day2 % hour
        minute1 = hour2 // minute
        minute2 = hour2 % minute

        user_input2 = f"{day1} Днів {str(hour1).zfill(2)}:{str(minute1).zfill(2)}:{str(minute2).zfill(2)}"
        print(user_input2)

        break




