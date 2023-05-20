n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for elem2 in arr2:
    is_exist = True
    if elem2 not in arr1:
        is_exist = False

    print(1 if is_exist else 0, end=' ')