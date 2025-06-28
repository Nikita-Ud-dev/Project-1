
user_input = str(input("Введіть ім'я змінної:"))
lst1 = user_input.split(" ")

for space in user_input:
    if space == " ":
        print(False)
    elif space == "":
        print(False)
    else:
        continue
####################################
for punctuation in user_input: # string.punctuation
    if punctuation == "!":
        print(False)
    elif punctuation == '"':
        print(False)
    elif punctuation == "#":
        print(False)
    elif punctuation == "$":
        print(False)
    elif punctuation == "%":
        print(False)
    elif punctuation == "&":
        print(False)
    elif punctuation == "'":
        print(False)
    elif punctuation == "(":
        print(False)
    elif punctuation == ")":
        print(False)
    elif punctuation == "*":
        print(False)
    elif punctuation == "+":
        print(False)
    elif punctuation == ",":
        print(False)
    elif punctuation == "-":
        print(False)
    elif punctuation == ".":
        print(False)
    elif punctuation == "/":
        print(False)
    elif punctuation == ":":
        print(False)
    elif punctuation == ";":
        print(False)
    elif punctuation == "<":
        print(False)
    elif punctuation == "=":
        print(False)
    elif punctuation == ">":
        print(False)
    elif punctuation == "?":
        print(False)
    elif punctuation == "@":
        print(False)
    elif punctuation == "[":
        print(False)
    elif punctuation == "\"":
        print(False)
    elif punctuation == "]":
        print(False)
    elif punctuation == "^":
        print(False)
    elif punctuation == "`":
        print(False)
    elif punctuation == "{":
        print(False)
    elif punctuation == "|":
        print(False)
    elif punctuation == "}":
        print(False)
    elif punctuation == "~":
        print(False)
    else:
        continue
####################################
for punctuation1 in lst1:
    if punctuation1 == "__":
        print(False)
    elif punctuation1 == "___":
        print(False)
    elif punctuation1 == "____":
        print(False)
    elif punctuation1 == "_____":
        print(False)
    else:
        continue
####################################
for keyword in  lst1: #keyword.kwlist
    if keyword == "False":
        print(False)
    elif keyword == "None":
        print(False)
    elif keyword == "True":
        print(False)
    elif keyword == "and":
        print(False)
    elif keyword == "as":
        print(False)
    elif keyword == "assert":
        print(False)
    elif keyword == "async":
        print(False)
    elif keyword == "await":
        print(False)
    elif keyword == "break":
        print(False)
    elif keyword == "class":
        print(False)
    elif keyword == "continue":
        print(False)
    elif keyword == "def":
        print(False)
    elif keyword == "del":
        print(False)
    elif keyword == "elif":
        print(False)
    elif keyword == "else":
        print(False)
    elif keyword == "except":
        print(False)
    elif keyword == "finally":
        print(False)
    elif keyword == "for":
        print(False)
    elif keyword == "from":
        print(False)
    elif keyword == "global":
        print(False)
    elif keyword == "if":
        print(False)
    elif keyword == "import":
        print(False)
    elif keyword == "in":
        print(False)
    elif keyword == "is":
        print(False)
    elif keyword == "lambda":
        print(False)
    elif keyword == "nonlocal":
        print(False)
    elif keyword == "not":
        print(False)
    elif keyword == "or":
        print(False)
    elif keyword == "pass":
        print(False)
    elif keyword == "raise":
        print(False)
    elif keyword == "return":
        print(False)
    elif keyword == "try":
        print(False)
    elif keyword == "while":
        print(False)
    elif keyword == "with":
        print(False)
    elif keyword == "yield":
        print(False)
    elif keyword == "case":
        print(False)
    elif keyword == "match":
        print(False)
    elif keyword == "type":
        print(False)
    else:
        continue
####################################
for number in lst1: #tuple("0""1""2""3""4""5""6""7""8""9")
    if number[0] == "0":
        print(False)
    elif number[0] == "1":
        print(False)
    elif number[0] == "2":
        print(False)
    elif number[0] == "3":
        print(False)
    elif number[0] == "4":
        print(False)
    elif number[0] == "5":
        print(False)
    elif number[0] == "6":
        print(False)
    elif number[0] == "7":
        print(False)
    elif number[0] == "8":
        print(False)
    elif number[0] == "9":
        print(False)
    else:
        break
####################################
low = user_input.lower()
user_input2 = "".join(user_input)
for letter in lst1:
    if not low == letter:
        print(False, 3)
    else:
        print(True)
        continue
