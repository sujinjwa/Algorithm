n = int(input())
arr = [0] * 100

for _ in range(n):
    start, end = tuple(map(int, input().split()))
    for i in range(start, end+1):
        arr[i] += 1

print(arr)

idx = 0
max_cnt = 0
for i in range(1, len(arr)):
    if arr[i] > arr[idx]:
        max_cnt = arr[i]

print(max_cnt)