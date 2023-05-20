# 3 줄에 걸쳐 한 줄에 하나씩 3개의 숫자 주어짐
nums = [
    list(map(int, input()))
    for _ in range(3)
]

def count_cnt(i, j, a, b, c, arr): # 팀원 i, j 가 팀으로 이긴 경우 1 리턴, 아닌 경우 0 리턴
    if (i == a and i == b and j == c) or (i == a and i == c and j == b) or (j == a and j == b and i == c) or (j == a and i == b and j == c) or (i == a and j == b and j == c) or (j == a and i == b and i == c):
        arr.append([i, j]) # 팀으로 이긴 경우의 숫자 i, j 를 arr에 append
        return 1
    return 0

cnt = 0 # 팀으로 이길 수 있는 경우의 수

for i in range(1, 10): # 팀원 1은 i
    for j in range(i+1, 10): # 팀원 2는 j

        arr = [] # i, j가 가로, 세로, 대각선 중 중복되는 경우가 있는지 확인하기 위한 배열

        # case 1) 가로선으로 이겼을 경우
        for a, b, c in nums:
            cnt += count_cnt(i, j, a, b, c, arr) # 이긴 경우의 두 숫자 i, j 리턴하여 arr 배열에 저장

        # case 2) 세로선으로 이겼을 경우
        for k in range(3):
            a = nums[0][k]
            b = nums[1][k]
            c = nums[2][k]
            
            cnt += count_cnt(i, j, a, b, c, arr)

        # case 3) 대각선으로 이겼을 경우
        # case 3-1) 오른쪽으로 내려가는 대각선
        a = nums[0][0]
        b = nums[1][1]
        c = nums[2][2]

        cnt += count_cnt(i, j, a, b, c, arr)
        
        # case 3-2) 오른쪽으로 올라가는 대각선
        a = nums[2][0]
        c = nums[0][2]
        
        cnt += count_cnt(i, j, a, b, c, arr)

        # i, j가 가로, 세로, 대각선 중 중복되는 경우 있는지 확인하기 위해
        # arr를 오름차순 정렬한 후,
        # 인접한 요소 간 같은 요소 있는 경우 cnt에서 -1 해준다
        arr.sort() # 오름차순 정렬
        for l in range(1, len(arr)):
            
            if arr[l - 1] == arr[l]:
                cnt -= 1

print(cnt)