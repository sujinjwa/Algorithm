import sys

n = int(input()) # 점 개수 : n개

# n개의 줄에 걸쳐 각 점의 위치 (x, y) 입력 받기
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

minOfMax = sys.maxsize 
for i in range(2, 100, 2): # x축과 평행한 직선 (y = i)
    for j in range(2, 100, 2): # y축과 평행한 직선 (x = j)
        
        # space1 : y축보다는 위, x축보다는 왼쪽에 위치한 점의 개수
        space1 = 0
        for x, y in points:
            if x < j and y > i:
                space1 += 1
        
        # space2 : y축보다는 위, x축보다는 오른쪽에 위치한 점의 개수
        space2 = 0
        for x, y in points:
            if x > j and y > i:
                space2 += 1
        
        # space3 : y축보다는 밑, x축보다는 오른쪽에 위치한 점의 개수
        space3 = 0
        for x, y in points:
            if x > j and y < i:
                space3 += 1
        
        # space4 : y축보다는 밑, x축보다는 왼쪽에 위치한 점의 개수
        space4 = 0
        for x, y in points:
            if x < j and y < i:
                space4 += 1
        
        max_space = max(space1, space2, space3, space4) # 4군데로 분할된 공간 중 가장 점이 많은 구역의 점의 개수
        minOfMax = min(max_space, minOfMax) # 최대 점의 개수 중 최솟값(점의 개수가 가장 균등하게 나뉘는 때) 구하기

print(minOfMax)