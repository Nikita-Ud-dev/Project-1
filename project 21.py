def add_one(some_list1):
    lst1 = []
    for digit in some_list1:
        lst1.append(str(digit))
    string3 = "".join(lst1)
    integer1 = int(string3) + 1
    lst2 = list(str(integer1))
    lst3 = []
    for string in lst2:
        lst3.append(int(string))
    return lst3

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))