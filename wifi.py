n, m = tuple(map(int, input().split())) # n : 숫자 개수, m : 와이파이 사용 가능한 거리
people = list(map(int, input().split()))

cnt = 0 # 와이파이 설치 개수

# case 1. 만약 와이파이 사용 가능한 거리가 0인 경우
#         살고 있는 사람 수 만큼 와이파이 개수 필요
if m == 0:
    for elem in people:
        if elem == 1:
            cnt += 1

# case 2. 와이파이 사용 가능한 거리가 0보다 긴 경우
#         하나의 와이파이로 사용할 수 있는 최대 사람의 수 : 2 * m + 1
else:
    i = 0
    while True:

        if i >= n: # n개의 숫자 모두 탐색한 이후 break
            break
        
        # 사람 발견한 경우
        # i + m + 1 자리에 와이파이 설치해야
        # 하나의 와이파이로 최대한 많은 사람 쓸 수 있다
        if people[i] == 1:
                i += (m * 2 + 1) 
                cnt += 1 # 와이파이 개수 갱신
        
        # 사람 없는 경우 다음 index 탐색하기 위해 i + 1
        else: i += 1

print(cnt)