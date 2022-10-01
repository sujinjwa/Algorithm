n = 3
answer = []

# 출력
def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

# answer배열에서 curr_num번째에 위치할 숫자(0 또는 1) 선택하는 함수
def choose(curr_num):

    # 종료 조건 : curr_num이 answer의 인덱스(최대 n) 벗어난 경우
    if curr_num == n + 1:
        print_answer()
        return
    
    # curr_num == 1 : 첫 번째 인덱스에 숫자를 넣어야 할 때
    # answer[-1] != 0 : answer의 길이가 어떻든 상관없이
    # 현재 answer의 마지막 값이 0이 아니고 1인 경우
    # => 두 가지 조건일 때 answer에 0을 추가해도 2개의 0이 인접해지지 않음
    if curr_num == 1 or answer[-1] != 0:
        answer.append(0)
        choose(curr_num + 1)
        answer.pop()
    
    answer.append(1)
    choose(curr_num + 1)
    answer.pop()
    
    return

choose(1)