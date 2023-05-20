n = int(input()) # n : 수열의 크기
visited = [False] * (n + 1) # visited : answer의 해당 index가 채워져있는지 확인하기 위한 배열
answer = [] # answer : 각 수열의 출력을 위한 배열

# 완성된 각 수열 출력하는 함수
def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

# answer의 curr_num번째 위치할 숫자 구하는 함수
def choose(curr_num):
    # 종료 조건
    # : 자릿수 curr_num이 수열의 크기인 n을 초과할 경우 
    # 수열이 완성되었으므로 print_answer 함수 호출
    if curr_num == n + 1:
        print_answer()
        return
    
    # 1부터 n까지의 수 한 번씩만 사용하여 만들 수 있는
    # 모든 수열의 경우의 수 구하기
    for i in range(1, n+1):
        if visited[i]: # 이미 채워진 칸은 건너뛰기
            continue
        
        visited[i] = True # 채워지지 않은 i번째 칸 채우기
        answer.append(i) # i번째 칸에 숫자 i 추가

        choose(curr_num + 1) # 다음 칸으로 이동

        # 완성된 수열 출력 후
        # 가장 맨 마지막 인덱스의 칸 비우기
        visited[i] = False
        answer.pop()

choose(1)