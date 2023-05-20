# 클래스 입력
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index

# 변수 선언 및 입력
n = int(input())
given_inputs = list(map(int, input().split()))
numbers = [
    Number(num, i)
    for i, num in enumerate(given_inputs)
]

answer = [
    0 for _ in range(n)
]

# number가 같으면, index로 오름차순 정렬
numbers.sort(key = lambda x: (x.number, x.index))

# 정렬된 숫자들의 원래 인덱스 활용한 정답 배열 저장
for i, number in enumerate(numbers):
    answer[number.index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end=' ')