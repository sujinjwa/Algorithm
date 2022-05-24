INT_MAX = 100

n = int(input()) # 사람들의 수

# n개의 줄에 걸쳐 각 사람의 위치와 알파벳 입력 받기
inputs = [
    input().split()
    for _ in range(n)
]

arr = [''] * (INT_MAX + 1) # 일직선 상 101칸의 빈 공간 선언

# 일직선 상 각 사람의 위치에 알파벳 정보 저장
for locat, alpha in inputs:
    locat = int(locat)
    arr[locat] = alpha

max_dis = 0 # 사람 간의 최대 거리
for i in range(INT_MAX + 1): # 완전 탐색하는 시작 점
    cnt_G = 0 # [i, j] 구간 내 'G'의 개수
    cnt_H = 0 # [i, j] 구간 내 'H'의 개수
    
    if arr[i] != '': # 해당 시작 점이 빈칸 아닌 경우
        if arr[i] == 'G':
            cnt_G += 1 # 시작 점이 'G'일 때 cnt_G + 1
        else:
            cnt_H += 1 # 시작 점이 'H'일 때 cnt_H + 1
        
        for j in range(i+1, INT_MAX + 1): # 시작점으로부터 탐색하고픈 끝 점
            if arr[j] != '': # 해당 끝 점이 빈칸이 아닌 경우
                if arr[j] == 'G':
                    cnt_G += 1 # 끝 점이 'G'일 때 cnt_G + 1
                else:
                    cnt_H += 1 # 끝 점이 'H'일 때 cnt_H + 1

                if cnt_G == cnt_H: # [i, j] 구간 내 G와 H의 개수가 같다면
                    max_dis = max(max_dis, j-i)

print(max_dis)