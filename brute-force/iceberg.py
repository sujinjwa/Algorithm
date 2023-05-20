n = int(input()) # 빙산의 개수 : n
Hs = [
    int(input()) # 각 빙산의 높이
    for _ in range(n)
]

max_cnt = 0 # 빙산의 최대 개수

# 1부터 가장 높은 빙산의 높이 - 1 까지 높이 i 설정하고,
# 높이가 1씩 높아질 때마다 빙산의 개수 확인
for i in range(1, max(Hs)):
    height = i # 높이 : i
    cnt = 0 # 높이 별 각 빙산의 개수
    arr = [0] * n # n개의 빙산 순서대로 나열
    
    for j in range(len(Hs)):
        if height < Hs[j]: # height보다 해당 빙산의 높이가 더 높다면
            arr[j] += 1
        
    # 1 에서 바로 다음 0이 올 때 덩어리 1개인 것임
    for k in range(1, len(arr)):
        if arr[k-1] == 1 and arr[k] == 0: # 빙산 끊어진 부분 있다면
            cnt += 1
        if k == n-1 and arr[k] == 1: # 마지막 위치에 빙산 있다면
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)