l = [2, 3, 32, 12, 5, 7]
l2 = [5]
l3 = []
l4 = [30, 5, 7, 15, 40]

l3.append(1)

x1 = l.pop(-1)
x2 = l2.pop(-1)
x3 = l3.pop(-1)
x4 = l4.pop(-1)

l.insert(0, x1)
l2.insert(0, x2)
l3.insert(0, x3)
l4.insert(0, x4)

del l3[-1]

print(l)
print(l2)
print(l3)
print(l4)
