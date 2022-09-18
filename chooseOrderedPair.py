k, n = list(map(int, input().split())) # k : 숫자 제한범위, n : 고르는 행위 반복하는 횟수
num = [] # 순서쌍 출력하기 위한 리스트

# 순서쌍 출력
def print_num(num):
    for elem in num:
        print(elem, end=" ")
    print()

# 순서쌍 만들기
def choose(cur_num):
		# cur_num 이 n + 1 일때 종료
    if cur_num == n + 1:
        print_num(num)
        return
    
		# 1 이상 k 이하의 숫자 하나씩 골라 n번 반복하여 모두 다른 순서쌍 만들기
    for i in range(1, k+1):
        num.append(i)
        choose(cur_num + 1)
        num.pop()

	# return

choose(1)