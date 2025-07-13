def difference(*args: int or float):
    lst1 = list(args)

    if not list(lst1):
        lst1.append(0)

    result = max(lst1) - min(lst1)
    result1 = round(result, 2)

    print("#" * 20)
    return result1

print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())