n = int(input()) # 원소 개수: n개
arr = list(map(int, input().split())) # n개의 숫자 입력 받기

# 선택 정렬 알고리즘 구현
for i in range(n):

    minimum = i # i번째에 위치할 최솟값의 위치 구하기 위한 변수

    # 최솟값 제외한 나머지 값들(i + 1 부터 마지막 원소까지) 하나씩
    # arr[minimum]과 비교하며 조회!
    # arr[minimum]보다 작다면 minimum에 해당 위치 대입하여
    # 최종적으로 i번째에 위치할 최솟값의 위치 구하기
    for j in range(i + 1, n):
        if arr[j] < arr[minimum]: # 만약 minimum보다 작은 숫자 찾은 경우
            minimum = j
    
    # i + 1 부터 마지막 원소까지의 조회 끝난 후
    # i번째 위치의 값(arr[i])과 최솟값(minimum) 끼리 swap
    arr[i], arr[minimum] = arr[minimum], arr[i]

# 오름차순으로 선택 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')