n = int(input()) # n : 블럭의 수

# n개의 층으로 이루어진 1차원 젠가의 상태 입력 받기
arr = [
    int(input())
    for _ in range(n)
]

# 2번에걸쳐 특정 구간의 블럭들을 빼는 작업 진행
for _ in range(2):
    temp = [] # 제거 후 빈 젠가 내 숫자 순서 재배치 위한 빈 배열 생성

    # 제거한 블럭의 시작과 끝번째 수
    s1, e1 = tuple(map(int, input().split()))

    # 젠가의 위에서부터 s1번째부터 e1번째까지의 블럭 제거
    for i in range(s1 - 1, e1):
        arr[i] = 0
    
    # 제거 후 생긴 빈 공간 없애는 작업 진행
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        
        temp.append(arr[i])
    
    # 빈 공간 없앤 temp를 arr로 갱신
    arr = temp

# 제거 작업 후 남은 블록의 개수와 숫자들 출력 
print(len(arr))
for elem in arr:
    print(elem)