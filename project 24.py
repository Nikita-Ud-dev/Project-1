from collections import OrderedDict

def popular_words (text: str, words: list):
    text1 = text.lower().split()

    lst1 = []
    for word in words:
        count1 = text1.count(word)
        lst1.append(count1)

    zip1 = zip(words, lst1)
    ordered_d1 = OrderedDict(zip1)

    return ordered_d1
    # Тут в мене невдачні дублі якщо цікаво

    # for word in text1:
    #     if word in words:
    #         count1 = text1.count(word)
    #         lst1.append(count1)
    #         for word1 in text1:
    #             if word1 == word:
    #                 text1.remove(word1)
    # for zero in range(len(words)):
    #     if len(words) > len(lst1):
    #         lst1.append(0)

    # for number in lst1:
    #     pass
    #     for key  in words:
    #         ordered_d1[key] = number
    # x = lst1[::1]
    # string1 = "".join(str(result))
    # ord_dict1 = {result}
    # for key in words:
    #     ordered_d1[key] = None

    #  = ordered_d1.fromkeys(words, lst1)
    # return ord_dict1

    # for word1 in text1:
    #     if word in words:
    #         if word == words[0]:
    #             lst1.append(words.count(int(word)))

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'one', 'two', 'near']))