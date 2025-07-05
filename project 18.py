def correct_sentence(text: str):
    lst = []
    split1 = f"{text}".split()
    split2 = split1[0].title()
    for string1 in split1:
        lst.append(string1)
    del lst[0]
    string1 = "".join(split2)

    string2 = "".join(lst)
    if not list(lst):
        string = f"{string1}"
        if string[-1] in ".":
            return string
        elif string[-1] != ".":
            string = f"{string1}."
            return string
    else:
        string = f"{string1} {string2}"

    if string[-1] in ".":
        return string
    elif string[-1] != ".":
        string = f"{string1} {string2}."
        return string
    return None


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))