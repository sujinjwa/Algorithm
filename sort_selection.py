n = int(input()) # 원소 개수: n개
arr = list(map(int, input().split())) # n개의 숫자 입력 받기

# 선택 정렬 알고리즘 구현
for i in range(n):

    minimum = i

    # 최솟값 제외한 나머지 값들 중 최솟값 위치 구하여 minimum에 저장
    for j in range(i + 1, n):
        if arr[j] < arr[minimum]:
            minimum = j
    
    # 나머지 수들 중 가장 작은 값(arr[minimum])을 정해진 위치(i)에 배치
    arr[i], arr[minimum] = arr[minimum], arr[i]

# 오름차순 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')