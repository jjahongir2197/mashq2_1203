# 2) Student Grade Manager

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        return f"{self.name} | Grades: {self.grades} | Avg: {self.average():.2f}"


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))

    def find(self, name):
        for s in self.students:
            if s.name == name:
                return s

    def show_students(self):
        for s in self.students:
            print(s.info())


def run():
    school = School()

    while True:
        print("\n1 Add Student")
        print("2 Add Grade")
        print("3 Show Students")
        print("4 Exit")

        c = input()

        if c == "1":
            school.add_student(input("Name: "))

        elif c == "2":
            s = school.find(input("Name: "))
            if s:
                s.add_grade(int(input("Grade: ")))

        elif c == "3":
            school.show_students()

        else:
            break


run()
