def first_word(text: str):
    """ Пошук першого слова """

    punctuation12 = "."
    punctuation13 = ","
    text = text.replace(punctuation12, " ")
    text = text.replace(punctuation13, " ")

    split1 = text.split()
    print("#" * 20)
    return split1[0]


print(first_word("Hello world")) #== "Hello", 'Test1'
print(first_word("greetings, friends")) #== "greetings", 'Test2'
print(first_word("don't touch it")) #== "don't", 'Test3'
print(first_word(".., and so on ...")) #== "and", 'Test4'
print(first_word("hi")) #== "hi", 'Test5'
print(first_word("Hello.World")) #== "Hello", 'Test6'
