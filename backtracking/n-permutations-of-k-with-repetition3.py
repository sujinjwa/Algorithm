k, n = tuple(map(int, input().split())) # k : 고를 수 있는 숫자 범위, n : 숫자 
arr = [] # n 길이의 서로 다른 순서쌍 구하기 위한 숫자 배열 초기화

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

# choose : curr_num번째 자릿수에 위치할 숫자를 1 ~ k 중 선택하는 함수
def choose(curr_num):
    # 종료 조건 (자릿수가 주어진 n을 초과) 시 
    if curr_num == n + 1:
        print_arr()
        return
    
    # 1 ~ k 순서로 arr에 추가하고 arr 출력 후 맨 뒷 자리 숫자 pop
    for i in range(1, k + 1):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)