def say_hi(name: str, age: int):
    if age <= 0:
        return f"Your age is not a positive number {name}"
    return f"Hi. My name is {name} and I'm {age} years old"

print(say_hi(name= "Alex", age= 35))
print(say_hi(name= "Frank", age= 68))
print(say_hi(name= "Nik", age= 0))
