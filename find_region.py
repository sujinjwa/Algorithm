n = int(input())

class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

people = []
for _ in range(n):
    name, address, region = tuple(input().split())
    people.append(Person(name, address, region))

names = []
for i in range(n):
    names.append(people[i].name)

names.sort()
last_name = names[n-1]

for i in range(n):
    if last_name == people[i].name:
        print(f"name {people[i].name}")
        print(f"addr {people[i].address}")
        print(f"city {people[i].region}")