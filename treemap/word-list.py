from sortedcontainers import SortedDict

sd = SortedDict()
n = int(input())

for _ in range(n):
    word = input()

    if word not in sd:
        sd[word] = 1
    else:
        sd[word] += 1

for key, value in sd.items():
    print(key, value)