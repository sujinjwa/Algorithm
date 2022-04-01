class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

given_inputs = [
    tuple(input().split())
    for _ in range(5)
]

people = [
    Person(name, int(height), float(weight))
    for name, height, weight in given_inputs
]

people.sort(key=lambda x: x.name)
print('name')
for person in people:
    print(person.name, person.height, person.weight)

people.sort(key=lambda x: -x.height)
print('\nheight')
for person in people:
    print(person.name, person.height, person.weight)