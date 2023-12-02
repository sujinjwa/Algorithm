# 스택/큐 '올바른 괄호' 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    
    cnt = 0
    for c in s:
        if c == ')' and cnt == 0:
            return False
        
        if c == '(':
            cnt += 1
        
        if c == ')':
            cnt -= 1
    
    if cnt != 0:
        return False

    return True