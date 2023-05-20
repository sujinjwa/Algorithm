# 3명의 사람이 초기 위치 입력 받기
pos = list(map(int, input().split()))

pos.sort() # 오름차순 정렬

# Case 1: 이미 연속된 수인 경우
if (pos[1] - pos[0]) <= 1 and (pos[2] - pos[1]) <= 1:
    print(0)

# Case 2: 한 번만 이동하면 연속된 수가 되는 경우
elif (pos[1] - pos[0]) <= 2 and (pos[2] - pos[1]) <= 2:
    print(1)

# Case 3: 그 외의 경우
# pos[0]부터 pos[1] 까지의 거리와, pos[1]부터 pos[2] 까지의 거리 중
# 더 멀리 있는 거리에서 -1 한 만큼 최대 이동할 수 있다
else:
    longer = max((pos[1] - pos[0]), (pos[2] - pos[1]))
    print(longer - 1)