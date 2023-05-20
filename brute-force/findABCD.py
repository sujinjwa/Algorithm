nums = list(map(int, input().split()))

# 해당 a, b, c, d 연산한 arr이 입력 받은 nums와 같은지 확인
def isSame(arr, nums):
    
    arr.sort()
    nums.sort()

    for num, elem in zip(nums, arr):
        if num != elem:
            return False
    
    return True

# 4 개의 정수 a, b, c, d 의 모든 경우 조회
# 해당 a, b, c, d 연산한 arr이 입력 받은 nums와 같은지 확인
for A in range(1, 41):
    for B in range(A, 41): # 범위 A <= B <= C <= D 이므로, B는 A부터, C는 B부터, D는 C부터 조회
        for C in range(B, 41):
            for D in range(C, 41):
                
                # i, j, k, l 의 연산식으로 이루어진 배열 arr 생성
                arr = [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]
                
                # if sorted(arr) == sorted(nums): 도 가능
                if isSame(arr, nums):
                    print(A, B, C, D)
                    break