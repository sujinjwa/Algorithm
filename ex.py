n, m = list(map(int, input().split()))
# n : 주어진 숫자의 총 개수
# m : 선택한 숫자의 개수

nums = list(map(int, input().split()))
# nums : 주어진 모든 숫자 모음

arr = [] # 선택된 m개의 숫자들 임시로 저장해두기 위한 배열
max_val = 0

# nums 중 k번째의 숫자 선택
# cur_val := k번째 숫자까지 xor 연산한 결과
def choose(k, cur_val):

    global max_val

    if k == m:
        # 최댓값 구하기
        if max_val < cur_val:
            max_val = cur_val
        return
    
    for i in range(n):
        if k == 0:
            arr.append(nums[i])
            choose(k + 1, arr[k])
            arr.pop()

        elif k >= 1:
            arr.append(nums[i])
            choose(k + 1, arr[k - 1] ^ arr[k])
            arr.pop()
    
    return

choose(0, 0)
print(max_val)