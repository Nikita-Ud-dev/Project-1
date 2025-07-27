import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    def filter1(text: str, element1: str = "<", element2: str = ">"):
        del_element = False # Це мій перемикач який показує що я не в зоні тегу або в зоні
        lst1 = []

        for letter in text:
            if letter == element1:
                del_element = True # Увійшов зону ігнорування символів
                continue
            if letter == element2:
                del_element = False # Вийшов із зони тегу
                continue
            if not del_element:
                lst1.append(letter)

        return "".join(lst1)

    result_file1 = filter1(html)

    with codecs.open(result_file, "w", "utf-8") as file1:
        file1.write(result_file1)

        return result_file1


delete_html_tags("draft.html")

# протягом двох днів навіть трьох спроби зробити робочий фільтр, але на жаль вони не зовсім вдалі тому що дублювали висновок так що так.

# index = text.find(element1)
# index1 = text.find(element2)

# while True:
        # if index1 == -1:
        #    break
# [index: index1 + 1]
# for element in text[index:index1 + 1]:
#     text = text.replace(element, "|", 1)
# if "|" in text:
#     text = text[index1 + 1:]
# index = text.find(element1, index + 1)
# index1 = text.find(element2, index1 + 1)

# result3 = text.split("|")
        # result4 = "".join(result3).split()
        # result5 = "".join(result4)
        # result = "".join(lst1).split("|")
        # # for space in result:
        # #     result.insert(0, " ")
        # result1 = "".join(result)

# while True:
#     if stop > 1000:
#         # x = string.join(lst2)
#         print(x1)
#         break
#
#     for element in x1:
#         if element == element1:
#             index = x1.find(element1)
#
#             for del_element in x1[index:-1:]:
#                 if del_element == element2:
#                     index1 = x1.find(del_element)
#                     for del_element1 in x1[index:index1 + 1:]:
#                         x1.replace(del_element1, " ")
#
#                     index = x1.find(element1, index + 1)
#                     index1 = x1.find(element2, index1 + 1)
#                     break
#         elif element == ">":
#             continue
#         elif stop > 1000:
#             break
#         elif element == "|":
#             stop += 1000
#             break
#         else:
#             lst3.append(element)
#             stop += 1


# lst1 = []
# lst1.append("|")
# lst2 = []
# lst3 = []

# element1 = "<"
# element2 = ">"
# stop = 0
# for not_even in range(1, 1000 + 1, 2):
#     lst1.append(not_even)
# for evet in range(2, 1001 + 1, 2):
#     lst2.append(evet)


# string = ""
# x1 = html + "|"

# html = "< sdsdasadsads> 123212 ? asasdsda < aasdada >"
