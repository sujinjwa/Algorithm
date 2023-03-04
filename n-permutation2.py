n = int(input()) # n : 수열의 길이
arr = []
visited = [False] * (n + 1)

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

# arr의 curr_num번째에 위치할 숫자 고르는 함수
def choose(curr_num):
    # 종료 조건 : arr의 길이가 n을 초과할 때
    if curr_num == n + 1:
        print_arr()
        return
    
    # 1부터 n까지의 수 한 번씩만 사용햐여 만들 수 있는
    # 가능한 모든 수열 구하기
    for num in range(1, n + 1):
        if visited[num]: # 이미 arr에 추가한 숫자는 제외
            continue
        
        arr.append(num)
        visited[num] = True
        choose(curr_num + 1)
        arr.pop()
        visited[num] = False

choose(1)