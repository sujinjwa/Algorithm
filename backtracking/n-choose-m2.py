# n : 고를 수 있는 숫자의 최대 범위, m : 조합의 길이
n, m = tuple(map(int, input().split()))
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

# 직전 숫자가 pre_num일 때 curr_num번째에 위치할 숫자를 고르는 함수
def choose(curr_num, pre_num):
    # 종료 조건 : 숫자 arr의 길이가 m을 초과할 때
    if curr_num == m + 1:
        print_arr()
        return
    
    # 1이상 n이하의 숫자 중 적절한 숫자를 arr에 추가
    for num in range(1, n + 1):
        # 숫자 정렬이 오름차순이 아닌 경우 제외
        if pre_num >= num:
            continue
        
        arr.append(num)
        choose(curr_num + 1, num)
        arr.pop()

choose(1, 0)