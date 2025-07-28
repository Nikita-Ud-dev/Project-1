class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self): # Вивід результату покупки як в докуметації
        result = f"User: {self.user}\nItem:"
        for item, cnt in self.products.items():
            result += f"\n{item.name}: {cnt} pcs."
        return result


    def get_total(self):
        total = 0
        for item, cnt in self.products.items(): # Тут я перебераю ключ значення, створюю змінну, яка буде зберігати результат. Потім беру атребут ціни і помножую на значення(кількість)
            total += item.price * cnt
        return total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )

# print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
buyer1 = User("Oleg", "Subotov", "01452893")
# print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print("#" * 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print("#" * 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
