n = int(input()) # 개발자 n명
# n개의 줄에 걸쳐 각 개발자 일하는 시간 입력
hours = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_hours = 0 # 개발자 겹치는 최댓값 0으로 초기화

for i in range(n):
    arr = [0] * 1000 # 운행 되고 있는 시간대 나타내는 배열
    cnt = 0 # 운행되고 있는 시간

    for j in range(n):
        if j == i: # i번째 개발자 제외
            continue
        
        h1 = hours[j][0] # 각 개발자의 일 시작하는 시간
        h2 = hours[j][1] # 각 개발자의 일 끝나는 시간

        # 각 개발자 일하는 구간에 + 1
        # 일하는 "구간"이므로 범위는 h1부터 h2 - 1까지임
        for k in range(h1, h2):
            arr[k] += 1
    
    for elem in arr: # 운행 되고 있는 총 시간 : cnt
        if elem >= 1:
            cnt += 1

    max_hours = max(max_hours, cnt) # 운행 되고 있는 시간 중 최댓값 구하기

print(max_hours)