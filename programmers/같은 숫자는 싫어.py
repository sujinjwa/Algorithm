# 스택/큐 문제 : 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    for i in range(1, len(arr)):
        if i == 1:
            answer.append(arr[i-1])
            
        if arr[i] == arr[i-1]:
            continue
        
        answer.append(arr[i])
        
    return answer


def solution2(arr):
    answer = []
    for i in arr:
        # answer[-1:] = answer 값의 가장 뒤에 위치한 하나의 값을 list로 만든 것
        if answer[-1:] == [i]: continue
        
        answer.append(i)
    
    return answer
