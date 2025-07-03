import string

string1 = list(string.ascii_letters)
lst2 = []
lst3 = []
user_input = str(input("введіть через дефіс дві літери:"))

lst = user_input.split("-")

for letter in  lst:
    lst2.append(letter)

start = string1.index(lst2[0])
end = string1.index(lst2[-1])
func = string1[start:end+1]
lst3.extend(func)

user_input2 = "".join(lst3)
print(user_input2)
