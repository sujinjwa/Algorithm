n, m = list(map(int, input().split()))
# n : 자릿수에 들어갈 숫자 중 최대 숫자, m : 자릿수
arr = [] # 각 모든 조합이 임시저장되기 위한 공간(배열)

# 출력 함수
def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

# arr의 idx번째에 위치할 숫자 1 ~ n 중 고르는 함수
def choose(idx, num):

		# 종료 조건: 정해진 자릿수(m)에 도달했을 때
    if idx == m:
        print_arr()
        return

		# 오름차순의 조합을 조회하기 위해 
		# 새로운 매개변수 i + 1 도 같이 보내줌
    for i in range(num, n+1):        
        arr.append(i)
        choose(idx + 1, i + 1)
        arr.pop()
    return

choose(0, 1)