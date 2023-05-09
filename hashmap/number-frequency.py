# n : 원소의 개수, m : 질의의 수
n, m = tuple(map(int, input().split()))

# arr : n개의 숫자 입력
arr = list(map(int, input().split()))

# nums : m개의 숫자 입력
nums = list(map(int, input().split()))

# nums에 있는 숫자가 arr 내에 몇 개 있는지 조회
index_of_nums = {}

for i, elem in enumerate(arr):
    if elem not in index_of_nums:
        index_of_nums[elem] = 1

    else:
        index_of_nums[elem] += 1

# nums에 있는 숫자가 arr 내에 몇 개씩 존재하는지 공백 사이에 두고 출력
for num in nums:
    if num not in index_of_nums:
        print(0, end=' ')
    else:
        print(index_of_nums[num], end=' ')