# 1 이상 n 이하의 숫자 중 m개의 숫자를 골라 만들 수 있는 모든 조합 구하기
# 예) n = 4, m = 3인 경우, 1 2 3 / 1 2 4 / 1 3 4 / 2 3 4 가 가능하다

# n : 숫자의 최대 범위, m : 고를 수 있는 숫자의 총 개수
n, m = tuple(map(int, input().split()))
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

def choose(curr_num, pre_num):
    if curr_num == m + 1:
        print_arr()
        return

    for i in range(pre_num + 1, n + 1):
        arr.append(i)
        choose(curr_num + 1, i)
        arr.pop()

# choose(curr_num, pre_num)
# 직전에 선택한 숫자가 pre_num일 때
# curr_num번째 위치할 숫자를 고른다
choose(1, 0)