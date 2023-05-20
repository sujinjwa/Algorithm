n = int(input())
nums = list(map(int, input().split()))

# 최대값 찾기
max_num = -1

for curr_num in nums:
    # 최대가 될 수 있는 후보
    if max_num < curr_num:
        # 갱신할 수 있는지 아닌지 확인하기 위한 숫자의 등장 빈도
        count = 0
        for elem in nums:
            if elem in nums:
                if elem == curr_num:
                    count += 1
        # 이 숫자가 배열에서 유일할 때만 갱신합니다.
        if count == 1:
            max_num = curr_num

print(max_num)