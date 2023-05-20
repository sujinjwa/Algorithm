MAX_X = 10

n = int(input()) # 좌표의 개수 : n개

# n개의 각 좌표 x, y 값 입력 받기
points = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0 # 출력 변수

# x축, y축 기준 0 ~ 10의 모든 직선에 대해 전부 시도
for i in range(MAX_X + 1): # x축에 평행한 y = i 인 직선
    for j in range(MAX_X + 1): # x축에 평행한 y = j 인 직선
        for k in range(MAX_X + 1): # x축에 평행한 y = k 인 직선

            # success : 직선 3개로 모든 점 지나게 할 수 있으면 true
            success = True

            # case 1) x축에 평행한 직선 3개로
            # 모든 점을 지나게 할 수 있는 경우
            for x, y in points:
                # 해당 점이 직선에 닿으면 넘어간다
                if x == i or x == j or x == k:
                    continue

                success = False
            
            if success:
                ans = 1
            

            # case 2) x축에 평행한 직선 2개와 y축에 평행한 직선 1개로
            # 모든 점 지나게 할 수 있는 경우
            success = True # success = True로 초기화
            for x, y in points:
                # 해당 점이 직선에 닿으면 넘어간다
                if x == i or x == j or y == k:
                    continue

                success = False
            
            if success:
                ans = 1

            # case 3) x축에 평행한 직선 1개와 y축에 평행한 직선 1개로
            # 모든 점 지나게 할 수 있는 경우
            success = True # success = True로 초기화
            for x, y in points:
                # 해당 점이 직선에 닿으면 넘어간다
                if x == i or y == j or y == k:
                    continue
                
                success = False
            
            if success:
                ans = 1
            
            # case 4) y축에 평행한 직선 3개로
            # 모든 점 지나게 할 수 있는 경우
            success = True # success = True로 초기화
            for x, y in points:
                if y == i or y == j or y == k:
                    continue

                success = False
            
            if success:
                ans = 1

print(ans)