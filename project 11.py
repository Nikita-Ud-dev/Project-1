import keyword

user_input = str(input("Введіть ім'я змінної:"))
lst1 = user_input.split(" ")

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

punctuation0 =  ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
                 ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\'", "]",
                 "^", "`", "{", "|", "}", "~"]

punctuation2 = ["__", "___", "____", "_____"]

for space in user_input:
    if space == " ":
        print(False)
        break
    elif space == "":
        print(False)
        break
    else:
        break
####################################
for char in user_input: # string.punctuation "Не беремо виняток: '_'"
    if char in punctuation0:
        print(False)
        break
    else:
        continue
####################################
for punctuation1 in lst1: # "'__', '___', '____', '_____'"
    if punctuation1 in punctuation2:
        print(False)
        break
    else:
        continue
####################################
for keyword1 in lst1: #keyword.kwlist
    if keyword1 in keyword.kwlist:
        print(False)
        break
    elif keyword1 == "match":
        print(False)
        break
    elif keyword1 == "type":
        print(False)
        break
    else:
        continue
####################################
for number in lst1: # numbers
    if number[0] in numbers:
        print(False)
        break
    else:
        break
####################################
low = user_input.lower()

user_input2 = "".join(user_input)
for letter in user_input:
    if not low == letter:
        print(False)
        break
    else:
        print(True)
        break
