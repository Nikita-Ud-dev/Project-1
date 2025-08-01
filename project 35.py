# def decorator(func): # Не встиг прономерувати студентів через декоратор хочу вчасно здавати матеріал
#     number_student = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal number_student
#         number_student += 1
#         print(f"Student{number_student}")
#         return func(*args, **kwargs)
#     return wrapper

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f"First_name: {self.first_name}\n"
                f"Last_name: {self.last_name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}")

class Student(Human):
    number_student = 0

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        Student.number_student += 1
        self.number_student1 = Student.number_student
        # self.string = str(decorator)
    # @decorator
    # def print_student_with_numbering(self):
    #
    #     print()
    #     print(self)
    # def number_student1(self):
    #     string = ""
    #     for text in self.string:
    #         string = string + str(text)
    #     print(string)
    # def number_student(self):
    #     return (f"{self.string}\n"
    #             f"First_name: {self.first_name}\n"
    #             f"Last_name: {self.last_name}\n"
    #             f"Age: {self.age}\n"
    #             f"Gender: {self.gender}\n"
    #             f"Record_book: {self.record_book}\n")
    # @decorator
    def __str__(self):
        return (f"Student {self.number_student1}\n"
                f"First_name: {self.first_name}\n"
                f"Last_name: {self.last_name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Record_book: {self.record_book}\n")

class Group:

    def __init__(self, number):
        self.number = number
        self.group = [] # Замінив сет на лист щоб зберегти порядок, і я бачу що я не захищенний від дублікатів
        # self.max_group = max_group

    # def set_max_student_in_group(self, max_max):
    #     self.max_group = max_max

    def add_student(self, student):
        if len(self.group) >= 10:
            raise ValueError(f"Досягнутo максимальне значення {len(self.group)} студентів")
        else:
            self.group.append(student)
        # print(len(self.group))

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return self.group.remove(student)
        return None

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n"
        for student in self.group:
            all_students = all_students + str(student)
            all_students = all_students + "\n"
        return f'Number:{self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 27, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Konor', 'AN145')
st4 = Student('Female', 23, 'Christina', 'Onex', 'AN145')
st5 = Student('Female', 20, 'Dasha', 'Komarova', 'AN145')
st6 = Student('Male', 22, 'Artem', 'Borsh', 'AN145')
st7 = Student('Male', 21, 'Roma', 'Salat', 'AN145')
st8 = Student('Male', 21, 'Nikita', 'Formula', 'AN145')
st9 = Student('Male', 24, 'Gleb', 'Chicken', 'AN145')
st10 = Student('Female', 26, 'Sonya', 'Flaver', 'AN145')
st11 = Student('Female', 27, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
# gr.add_student(st11)

print(gr)
try:
    gr.add_student(st11)
except ValueError as e:
    print(e)





