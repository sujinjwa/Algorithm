# 양수 직사각형: 모든 칸의 숫자들이 양수여야 함(음수 X)
# 가능한 양수 직사각형 중 크기가 최대인 직사각형의 크기 구하기

ans = 0
n, m = tuple(map(int, input().split())) # n : 행의 크기, m : 열의 크기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 직사각형 영역 안에 음수 포함되어 있는지 확인. 포함된 경우 False 리턴
def not_negative_num(x1, y1, x2, y2):
    for row in range(x1, x2+1):
        for col in range(y1, y2+1):
            if grid[row][col] <= 0:
                return False

    return True

# 모든 직사각형을 조회할 때
# 왼쪽 상단 꼭짓점과 오른쪽 하단 꼭짓점의 위치를 하나씩 정하여 모든 직사각형 구하기
# 왼쪽 상단 꼭짓점: (x1, y1), 오른쪽 하단 꼭짓점: (x2, y2)
# 범위 => x1: 0~2, y1: 0~2, x2: x1~2, y2: y1~2
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                # 해당 직사각형이 양수 직사각형인 경우에만 ans를 최댓값으로 갱신
                if not_negative_num(x1, y1, x2, y2):
                    ans = max(ans, (x2-x1+1)*(y2-y1+1))

print(ans if ans > 0 else -1)