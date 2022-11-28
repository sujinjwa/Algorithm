n = int(input()) # n : 수열의 크기
answer = [] # answer : 완성된 각 수열을 출력하기 위한 배열
visited = [False] * (n + 1) # visited : 각 수열의 위치에 값이 채워져있는지 확인하기 위한 배열

# 완성된 각 수열을 출력하는 함수
def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

# answer의 curr_num번째 위치에 채워질 숫자를 구하는 함수
def choose(curr_num):
    if curr_num == 0: # 종료 조건 : 수열의 크기를 초과할 때
        print_answer()
        return
    
    # n부터 1까지 사전순으로 가장 뒤에 있는 순열부터 구하는 함수
    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)

        choose(curr_num - 1)

        visited[i] = False
        answer.pop()

choose(n)