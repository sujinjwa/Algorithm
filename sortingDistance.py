class Position:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

n = int(input())

given_inputs = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dots = [
    Position(idx+1, x, y)
    for idx, (x, y) in enumerate(given_inputs)
]

dots.sort(key=lambda x: abs(x.x)+abs(x.y))

for dot in dots:
    print(dot.number)