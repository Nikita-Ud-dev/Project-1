l = [2, 3, 32, 12, 5, 7]
l2 = [5]
l3 = []
l4 = [30, 5, 7, 15, 40]

l.insert(0,111)
l2.insert(0,111)
l3.insert(0,111)
l4.insert(0,111)

l.insert(0, l.pop(-1))
l2.insert(0, l2.pop(-1))
l3.insert(0, l3.pop(-1))
l4.insert(0, l4.pop(-1))

l.remove(111)
l2.remove(111)
l3.remove(111)
l4.remove(111)

print(l)
print(l2)
print(l3)
print(l4)
