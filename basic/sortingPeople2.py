class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

given_inputs = [
    tuple(input().split())
    for _ in range(n)
]

people = [
    Person(name, int(height), int(weight))
    for (name, height, weight) in given_inputs
]

people.sort(key=lambda x: (x.height, -x.weight))

for person in people:
    print(person.name, person.height, person.weight)