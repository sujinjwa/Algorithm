# k : 고를 수 있는 마지막 범위의 숫자, n : 순서쌍의 길이
k, n = tuple(map(int, input().split()))
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

# arr에서 curr_num번째에 위치할 숫자를 고르는 함수
def choose(curr_num):
    # 종료 조건 : 주어진 n 크기를 초과하는 경우
    if curr_num == n + 1:
        print_arr()
        return
    
    # 1~k 숫자 중 하나를 추가할 때
    # 연속하여 같은 숫자가 3번 이상 나오는 경우 제외하고
    # 모든 서로 다른 순서쌍 구하기
    for num in range(1, k + 1):
        if curr_num == 1 or curr_num == 2 or (arr[-2] != num or arr[-1] != num):
            arr.append(num)
            choose(curr_num + 1)
            arr.pop()

choose(1)