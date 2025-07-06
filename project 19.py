def second_index(text1: str, some_str1: str):
    target = text1.find(some_str1)
    target1 = text1.find(some_str1, target + 1)
    if target1 == -1:
        return None
    return target1


text = input("Введіть рядок:")
some_str = input("Введіть символи які хочете знайти:")

print(second_index(text, some_str))
print(second_index("Hello, hello", "lo"))
