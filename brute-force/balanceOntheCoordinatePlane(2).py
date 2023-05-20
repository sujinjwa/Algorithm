MAX_X = 100

# 변수 선언 및 입력
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 100

# 모든 직선에 대해 전부 시도
for i in range(0, MAX_X + 1, 2):
    for j in range(0, MAX_X + 1, 2):

        # x = i, y = j 를 기준으로 나눴을 때의 m을 구하기
        # segment : x = i, y = j를 기준으로 1 ~ 4사분면의 점의 개수
        segment = [0] * 5

        for x, y in points:
            # k번째 점이 몇사분면인지 확인하고 해당 위치의 segment를 1 증가
            if x > i and y > j:
                segment[1] += 1
            elif x < i and y > j:
                segment[2] += 1
            elif x < i and y < j:
                segment[3] += 1
            else:
                segment[4] += 1

        # x = i, y = j로 나눴을때의 m을 구하기
        cur_m = max(segment)

        ans = min(ans, cur_m)

print(ans)