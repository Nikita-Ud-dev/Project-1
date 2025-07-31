# def decorator(func): # Не встиг прономерувати студентів через декоратор хочу вчасно здавати матеріал
#     number_student = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal number_student
#         number_student += 1
#         print(f"Student{number_student}")
#         return func(*args, **kwargs)
#
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


# f"{print("#" * 20)}"
class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    # @decorator
    def __str__(self):
        return (f"First_name: {self.first_name}\n"
                f"Last_name: {self.last_name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Record_book: {self.record_book}\n")


# f"{print("#" * 20)}\n"
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        # self.find_student1 = find_student1

    def add_student(self, student):
        # self.add_student1 = True
        self.group.add(student)
        # if self.add_student1:
        #     self.group.add("\n")
        # self.add_student1 = False

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return self.group.discard(student)
        return None

    def find_student(self, last_name):

        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
        # print(last_name)
        # for object1 in str(self.group):
        #     if object1 in last_name:
        #         return last_name
        # return None

        # find_last_name = ""
        # # self.group = last_name
        # for last_name in self.group:
        #     find_last_name = find_last_name + str(last_name)
        #
        # x = self.group
        # print(find_last_name.find())

        # if last_name in self.group:
        #     return last_name
        # return None

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students = all_students + str(student)
            all_students = all_students + "\n"
        # all_students = all_students.join(x)
        # print(all_students)

        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
print(st1)
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
