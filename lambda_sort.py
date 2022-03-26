n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    people.append(Person(name, int(height), int(weight)))

people.sort(key=lambda x : x.height)

for person in people:
    print(person.name, person.height, person.weight)