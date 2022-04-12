n = int(input())
arr = [0] * 101

for _ in range(n):
    start, end = tuple(map(int, input().split()))
    for i in range(start, end+1):
        arr[i] += 1

max_idx = 1
max_cnt = 0
for j in range(2, len(arr)):
    if arr[j] > arr[max_idx]:
        max_idx = j
    max_cnt = arr[max_idx]

print(max_cnt)