
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

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.record_book == other.record_book)


        # elif self.first_name :
        #     return self.first_name == other.first_name
        # elif self.last_name == other.last_name:
        #     return self.last_name == other.last_name
        # elif self.age == other.age:
        #     return self.age == other.age
        # elif self.gender == other.gender:
        #     return self.gender == other.gender
        # elif self.record_book == other.record_book:
        #     return self.record_book == other.record_book
        # return None


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


    def add_student(self, student):
        # if len(self.group) >= 10:
        #     raise ValueError(f"Досягнутo максимальне значення {len(self.group)} студентів")
        # else:
        if student not in self.group:
            self.group.append(student)
        else:
            print("Виявлено дублікат студенту\n")

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