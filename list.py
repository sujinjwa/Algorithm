n = int(input())

_list = list(map(int, input().split()))

def even(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2

even(_list)

for elem in _list:
    print(elem, end=' ')