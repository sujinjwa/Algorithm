class Number:
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx

# 수열의 길이와 양의 정수인 원소 입력
n = int(input())
given_input = tuple(map(int, input().split()))

# given_input를 new_nums에 그대로 복사
new_nums = [
    num
    for num in given_input
]

# new_nums 오름차순 정렬
new_nums.sort()

# 새로운 배열 new_nums2 생성 및 오름차순 정렬한 순으로 원소와 index 함께 저장
new_nums2 = [
    Number(num, i+1)
    for i, (num) in enumerate(new_nums)
]

# given_input의 원소와 new_nums2의 원소가 같을 경우
# new_nums2의 index 출력
# 이때, 동일한 숫자 있을 수 있으므로 new_nums2의 해당 원소는 0으로 초기화
# 내부 for문 돌 때 if문에 한번 걸리면 i+1 되도록 break 걸어줌
for i in range(n):
    for j in range(n):
        if given_input[i] == new_nums2[j].num:
            print(new_nums2[j].idx, end=' ')
            new_nums2[j].num = 0
            break