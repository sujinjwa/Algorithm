n = int(input()) # 원소의 개수 : n개
arr = list(map(int, input().split())) # n개의 원소 입력 받기

# 삽입 정렬 알고리즘 구현
for i in range(1, n):
    key = arr[i] # 삽입하고자 하는 숫자 key 설정
    # i보다 작은 모든 index 조회(i-1 부터 0까지)
    for j in range(i-1, -1, -1):
        
        # j가 인덱스 범위 넘어가거나, arr[j]와 key 두 수가 오름차순 정렬이 된 경우
        if j < 0 or arr[j] <= key:
            break
        
        # key와 arr[j] 두 수 간 오름차순 정렬이 필요한 경우
        # 두 수의 값 교체
        arr[j + 1] = arr[j]
        arr[j] = key

# 오름차순 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')