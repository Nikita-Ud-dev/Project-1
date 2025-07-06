def second_index(text: str, some_str: str ):
        target = text.find(some_str)
        target1 = text.find(some_str,target + 1)
        if target1 == -1:
                return None
        return target1

text = input("Введіть рядок:")
some_str = input("Введіть символи які хочете знайти:")

print(second_index(text, some_str))
print(second_index("Hello, hello", "lo"))




