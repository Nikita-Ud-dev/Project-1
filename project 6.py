l = [2, 3, 32, 12, 5, 7]
l2 = [5]
l3 = []
l4 = [30, 5, 7, 15, 40]

if l == []:
    l.append(111)
elif l2 == []:
    l2.append(111)
elif l3 == []:
    l3.append(111)
elif l4 == []:
    l4.append(111)

x1 = l.pop(-1)
x2 = l2.pop(-1)
x3 = l3.pop(-1)
x4 = l4.pop(-1)

l.insert(0, x1)
l2.insert(0, x2)
l3.insert(0, x3)
l4.insert(0, x4)

if l == [111]:
    l.remove(111)
elif l2 == [111]:
    l2.remove(111)
elif l3 == [111]:
    l3.remove(111)
elif l4 == [111]:
    l4.remove(111)

print(l)
print(l2)
print(l3)
print(l4)
