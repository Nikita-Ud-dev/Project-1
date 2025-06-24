l1 = [0, 1, 7, 2, 4, 8]
l2 = [1, 3, 5]
l3 = [6]
l4 = []

y1 = l1.copy()
y2 = l2.copy()
y3 = l3.copy()
y4 = l4.copy()

if not list(l1):
    l1.append(0)
elif not list(l2):
    l2.append(0)
elif not list(l3):
    l3.append(0)
elif not  list(l4):
    l4.append(0)

x1 = sum(l1[::2]) * l1[-1]
x2 = sum(l2[::2]) * l2[-1]
x3 = sum(l3[::2]) * l3[-1]
x4 = sum(l4[::2]) * l4[-1]

print(y1, '=>', x1)
print(y2, '=>', x2)
print(y3, '=>', x3)
print(y4, '=>', x4)