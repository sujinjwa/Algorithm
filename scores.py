scores = list(map(int, input().split()))
arr = [0] * 11

for score in scores:
    if score == 0:
        break
    arr[score // 10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {arr[i]}")