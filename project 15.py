

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

        day_declination = ""
        if 11 <= day1 % 100 <= 14:
            day_declination = "Днів"
        elif 2 <= day1 % 10 <= 4:
            day_declination = "Дні"
        elif 1 == day1 % 10:
            day_declination = "День"
        else:
            day_declination = "Днів"

        user_input2 = f"{day1} {day_declination} {str(hour1).zfill(2)}:{str(minute1).zfill(2)}:{str(minute2).zfill(2)}"
        print(user_input2)

        break




