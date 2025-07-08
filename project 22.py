import string

def is_palindrome(text: str):
    strip1 = text.strip()

    lst1 = list(strip1)
    for punctuation1 in lst1:
        if punctuation1 in string.punctuation:  #string.punctuation
            lst1.remove(punctuation1)
    string1 = "".join(lst1)

    lst2 = string1.split() #Роблю спліт для того щоб об'єднати всі рядки в один рядок, та змінюю регістр на малі символи.
    string2 = "".join(lst2).lower()

    lst3 = []
    for string4 in string2[::-1]: # З кінця беру символи із рядка і вставляю у новий список потім створюю із списка рядок.
        lst3.append(string4)
    string5 = "".join(lst3)

    if string5 == string2: #Зрівнюю списки на паліандром.
        print("#" * 20)
        return True
    elif string5 != string2:
        print("#" * 20)
        return False
    return None


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))
