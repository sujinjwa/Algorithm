# 돌의 개수 : n 개, 점프 거리 : k 이내
n, k = tuple(map(int, input().split()))

nums = list(map(int, input().split())) # n개의 숫자 입력

# 최댓값이 max_val 일 때
# 거리 k 이내로 점프 가능한지 확인
def is_possible(max_val):
    arr = [] # max_val 보다 큰 숫자가 포함되지 않는 숫자들의 index 모아 놓은 배열 생성
    for i, elem in enumerate(nums):
        if elem <= max_val:
            arr.append(i)
    
    # print()
    for i in range(1, len(arr)):
        dis = arr[i] - arr[i - 1] # 요소 간 점프 거리
        
        if dis > k: # 점프 거리가 k 초과할 경우
            return False # 정답이 될 수 없음
    
    return True


# 최댓값 a := n번에 도달하기 위해 거쳐간
# 모든 지점들에 적힌 숫자로 설정하여 하나씩 탐색
for a in range(max(nums[0], nums[n - 1]), 101):
    # 최댓값이 a 일 때
    # 거리 k 이내로 점프 가능한지 확인
    if is_possible(a): # 가능하다면, 그때가 a의 최솟값이므로 답 출력 후 종료
        print(a)
        break