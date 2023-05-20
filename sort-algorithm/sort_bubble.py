n = int(input()) # 원소 n개
arr = list(map(int, input().split())) # 배열 입력 받기

# 거품 정렬 알고리즘 구현
# i : 교환 여부를 확인하기 위해 전체 값 (n개)를 한 바퀴 돌기 위함 
for i in range(n):
    # j : 첫번째 원소부터 n - 1 - i까지의 인접한 숫자끼리 비교하기 위함
    # 이때, n - 1 - i번째 원소부터 마지막 원소까지는 오름차순으로 정렬되어 있으므로,
    # 이 구간은 제외하고 비교해도 된다
    for j in range(n - 1 - i):
        
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# 오름차순 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')