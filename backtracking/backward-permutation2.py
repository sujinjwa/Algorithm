n = int(input()) # n : 수의 최대 범위
arr = []
visited = [False] * (n + 1)

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

# arr의 curr_num번째에 위치할 숫자 고르기
def choose(curr_num):
    # 종료 조건 : arr의 길이가 n을 초과할 때
    if curr_num == n + 1:
        print_arr()
        return
    
    # 1 ~ n까지의 수 한 번씩만 사용하여 
    # 사전순으로 가장 뒤에 있는 수열부터 만듣도록
    # num을 n, n-1, n-2, ... 1의 순서로 arr에 추가
    for num in range(n, 0, -1):
        if visited[num]: # 해당 숫자 num이 이미 arr에 추가된 경우 제외
            continue

        arr.append(num)
        visited[num] = True
        choose(curr_num + 1)
        arr.pop()
        visited[num] = False

choose(1)