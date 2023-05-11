# n : 원소의 개수
n = int(input())

dic = {}

for _ in range(n):
    x, y = tuple(map(int, input().split()))

    if x in dic:
        # 동일한 x좌표 갖는 점들에 대해
        # 가장 작은 y값으로 설정
        if dic[x] > y:
            dic[x] = y
    else:
        dic[x] = y

# 남아있는 점들의 y값의 합 출력
cnt = 0
for x in dic:
    cnt += dic[x]

print(cnt)