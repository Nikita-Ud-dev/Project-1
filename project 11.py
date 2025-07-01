import keyword
import string

user_input = str(input("Введіть ім'я змінної:"))
lst1 = user_input.split(" ")
low = user_input.islower()

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

punctuation0 =  ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
                 ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\'", "]",
                 "^", "`", "{", "|", "}", "~"]

punctuation2 = ["__", "___", "____", "_____"]

stop = 1
while True:
    if stop == 30:
        print(True)
        break
    elif stop > 90:
        break
    for char in user_input:
        if char == " ":
            print(False , 1)
            stop = stop + 90
            break
        elif char in punctuation0: # string.punctuation "Не беремо виняток: '_'"
            print(False, 3)
            stop = stop + 90
            break
        elif stop == 30:
            break
        elif stop > 90:
            break
####################################################
    for char1 in lst1:  # "'__', '___', '____', '_____'"
        if char1 in punctuation2:
            print(False, 4)
            stop = stop + 90
            break
####################################################
        elif char1 in keyword.kwlist:#keyword.kwlist
            print(False, 5)
            stop = stop + 90
            break
        elif char1 == "match":
            print(False, 6)
            stop = stop + 90
            break
        elif char1 == "type":
            print(False, 7)
            stop = stop + 90
            break
####################################################
        elif char1[0] in numbers: # numbers
            print(False, 8)
            stop = stop + 90
            break
        elif stop == 30:
                break
        elif stop > 90:
                break
####################################################
    for letter in user_input:
        if letter in string.ascii_uppercase:  # Перевірка регістру
            print(False, 10)
            stop = stop + 90
            break
        elif stop > 90:
            break
        elif stop == 30:
            break
        else:
            stop = stop + 1















