import string
user_input = str(input("Введіть назву hashtag:"))

stop = 1
ex = "Довжина рядка"

while True:
    if stop > 350:
        break
    elif stop == 140:
        break

    for punctuation0 in user_input:
        if punctuation0 in string.punctuation: # Якщо є string.punctuation
            lst0 = list(user_input)
            for delete in lst0:
                if delete in string.punctuation:
                    lst0.remove(delete)
                elif stop > 350:
                    break
                else:
                    stop = stop + 1
                    continue
            user_input0 = "".join(lst0)
            user_input1 = user_input0[:139]
            user_input2 = user_input1.title()
            lst = user_input2.split()
            user_input3 = f"{"#" + "".join(lst)}"
            print(user_input3)
            print(ex, ":", len(user_input3))
            stop = stop + 350
            break


        elif stop == 140: # Якщо немає string.punctuation
            user_input4 = user_input[:139]
            user_input5 = user_input4.title()
            lst1 = user_input5.split()
            user_input6 = "".join(lst1)
            user_input7 = f"{"#" + "".join(lst1)}"
            print(user_input7)
            print(ex, ":", len(user_input7))
            break

        else:
            stop = stop + 1
            continue








