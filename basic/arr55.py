n = int(input())
arr = []

five_cnt = 0
cnt = 0
while True:
    if five_cnt == 2:
        break

    cnt += 1
    arr.append(n * cnt)

    if (n * cnt) % 5 == 0:
        five_cnt += 1

for elem in arr:
    print(elem, end=' ')