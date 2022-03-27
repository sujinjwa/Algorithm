first, second = tuple(map(int, input().split()))
arr = [0, first, second]

for i in range(3, 11):
    arr.append((arr[i-1] + arr[i-2])%10)

for elem in arr[1::]:
    print(elem, end=' ')