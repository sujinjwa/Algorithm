# 프로그래머스 스킬 체크 레벨 1-1

def solution(arr, divisor):
    answer = []
    checked = False
    for elem in arr:
        if elem % divisor == 0:
            checked = True
            answer.append(elem)

    if checked == False:
        answer.append(-1)

    answer.sort()
    return answer