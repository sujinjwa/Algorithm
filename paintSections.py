# n번째 칸으로 이루어진 블록, k개의 명령
n, k = tuple(map(int, input().split()))
blocks = [0] * (n+1)

# k개 줄에 걸쳐 Ai부터 Bi까지 블록을 각각 1개씩 쌓으라는 명령 입력
inputs = [
    list(map(int, input().split()))
    for _ in range(k)
]

# 블록을 특정 구간에 쌓아주기
for i in range(k):
    idx_1 = inputs[i][0]
    idx_2 = inputs[i][1]
    for j in range(idx_1, idx_2+1, 1):
        blocks[j] += 1

# 최댓값 출력
print(max(blocks))