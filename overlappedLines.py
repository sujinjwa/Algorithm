n = int(input()) # 선분의 개수 : n개

# n개의 줄에 걸쳐 각 선분의 끝 점 (x1, 0), (x2, 1) 중 x1, x2 입력 받기
points = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0 # 겹치는 선분의 개수

for i in range(n): # n개의 선분 중 두 개의 선분 선택하는 모든 경우 순회
    for j in range(n):

        if j == i: # 같은 선분 비교는 제외
            continue

        # 첫 번째로 선택한 선분의 시작점(x1_1)과 끝점(x2_1)
        x1_1 = points[i][0]
        x2_1 = points[i][1]

        # 두 번째로 선택한 선분의 시작점(x1_2)과 끝점(x2_2)
        x1_2 = points[j][0]
        x2_2 = points[j][1]

        if x1_1 <= x1_2 and x2_1 >= x2_2: # 두 선분이 겹칠 경우
            cnt += 1 # 겹치는 선분의 개수 + 1
            break

        elif x1_1 >= x1_2 and x2_1 <= x2_2: # 두 선분이 겹칠 경우
            cnt += 1
            break

print(n - cnt) # 겹치지 않는 선분의 개수 출력