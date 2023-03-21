# n : 입력 받는 정수의 개수, m : 뽑는 개수
n, m = tuple(map(int, input().split()))
# numbers : n개의 숫자 입력 받기
numbers = list(map(int, input().split()))

# arr : 뽑은 m개의 숫자 모아 놓기 위한 1차원 배열
arr = []
max_xor = 0

# find_xor : arr 내 숫자들을 xor한 결과의 최댓값 구하는 함수
def find_xor():
    global max_xor

    xor = arr[0]
    for i in range(1, m):
        xor = xor ^ arr[i]

    max_xor = max(max_xor, xor)

# 지금까지 뽑은 숫자의 개수가 cnt개이고,
# 직전에 뽑은 숫자의 numbers 내 인덱스가 pre_index일 때
# 어떤 숫자 뽑을지 결정하는 함수
def choose(cnt, pre_index):
    if cnt == m:
        find_xor()
        return

    for i in range(pre_index + 1, n):
        arr.append(numbers[i])
        choose(cnt + 1, i)
        arr.pop()

choose(0, -1)

# xor한 결과 중 최댓값 출력
print(max_xor)