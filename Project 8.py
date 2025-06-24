
l1 = [0, 1, 0, 12, 3]
l2 = [0]
l3 = [1, 0, 13, 0, 0, 0, 5]
l4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

x1 = l1.copy()
x2 = l2.copy()
x3 = l3.copy()
x4 = l4.copy()

for number in l1:
    if number != 0:
        continue
    elif number == 0:
        l1.remove(number)
        l1.append(0)
        continue

for number in l2:
    if number != 0:
        continue
    elif number == 0:
        l2.remove(number)
        l2.append(0)
        continue

for number in l3:
    if number != 0:
        continue
    elif number == 0:
        l3.remove(number)
        l3.append(0)
        continue

for number in l4:
    if number != 0:
        continue
    elif number == 0:
        l4.remove(number)
        l4.append(0)
        continue


print(x1,"->",l1)
print(x2,"->",l2)
print(x3,"->",l3)
print(x4,"->",l4)
