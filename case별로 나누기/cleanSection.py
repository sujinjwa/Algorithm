a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

area = [0] * 101

for i in range(a, b):
    area[i] += 1

for i in range(c, d):
    area[i] += 1

section = 0 # 청소한 구역
for elem in area:
    if elem >= 1:
        section += 1

print(section)