arr = list(map(int, input().split()))

idx = 0
for i in range(10):
    if arr[i] == 0:
        idx = i
        break

for elem in arr[idx-1::-1]:
    print(elem, end=' ')