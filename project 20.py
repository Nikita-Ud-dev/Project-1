def common_elements():
    set1 = {0}
    set2 = {0}
    for set_add1 in  range(3, 100, 3):
        set1.add(set_add1)
    for set_add2 in range(5, 100, 5):
        set2.add(set_add2)
    intersection_set = set1.intersection(set2)
    return intersection_set


print(common_elements())
