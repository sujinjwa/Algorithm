class Student:
    def __init__(self, number, height, weight):
        self.number = number
        self.height = height
        self.weight = weight

n = int(input())
students = []

for i in range(n):
    given_inputs = tuple(input().split())
    height = given_inputs[0]
    weight = given_inputs[1]
    students.append(Student(i+1, int(height), int(weight)))

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)