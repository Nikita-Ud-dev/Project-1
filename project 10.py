import random

l1 = []
l2 = []

for randoms1 in range(random.randint(3, 10)):
    l1.append(random.randint(1,100))

for number in l1[0], l1[2], l1[-2]:
    l2.append(number)

print(l1, '==', l2)


