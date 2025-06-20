l = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3]
l3 = [1, 2, 3, 4, 5]
l4 = [1]
l5 = []

lx1 = l[:3]
lxx1 = l[3:]

lx2 = l2[:2]
lxx2 = l2[-1:]

lx3 = l3[:3]
lxx3 = l3[3:]

lx4 = l4[:1]
lxx4 = l4[2:]

lx5 = l5[:1]
lxx5 = l5[1:]

l = [lx1] + [lxx1]
l2 = [lx2] + [lxx2]
l3 = [lx3] + [lxx3]
l4 = [lx4] + [lxx4]
l5 = [lx5] + [lxx5]

print(l)
print(l2)
print(l3)
print(l4)
print(l5)
