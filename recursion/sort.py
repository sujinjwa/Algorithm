n = int(input())
arr = list(map(int, input().split()))

def print_arr(arr):
    for elem in arr:
        print(elem, end=' ')
    print()

arr.sort()
print_arr(arr)
arr.sort(reverse=True)
print_arr(arr)