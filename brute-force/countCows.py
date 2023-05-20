n = int(input()) # 소 마릿수 입력 받기
height = list(map(int, input().split())) # n마리의 각 소의 키 입력 받기

cnt = 0 # 위치와 키 모두 오름차순인 3쌍의 소의 수
for i in range(n):
    for j in range(i+1, n):
        if height[i] <= height[j]: # 만약 i번째 소가 j번째 소보다 키가 작을 경우
            for k in range(j+1, n):
                if height[j] <= height[k]: # 만약 j번째 소가 k번째 소보다 키가 작을 경우
                    cnt += 1

print(cnt)