n = int(input()) # 블럭의 개수 : n개
pos = [
    int(input()) # 각 위치별 블럭 수
    for _ in range(n)
]

# step 1. 모든 블럭의 평균 구하기
avg = sum(pos) // n

# step 2. 이동해야 할 블럭 횟수 구하기
cnt = 0 # 블럭 이동해야 할 횟수
for elem in pos:
    if elem > avg:
        cnt += (elem - avg)

print(cnt)