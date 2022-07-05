n = int(input()) # 원소 n개
arr = list(map(int, input().split())) # 배열 입력 받기

# 거품 정렬 알고리즘 구현
for i in range(n):
    for j in range(n - 1 - i):
        
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# 오름차순 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')