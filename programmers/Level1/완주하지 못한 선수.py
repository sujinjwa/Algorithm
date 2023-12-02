# 고득점 KIT > 해시 > '완주하지 못한 선수' 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dict = {}
    for p in participant:
        if p not in dict:
            dict[p] = 1
        else:
            dict[p] += 1
    
    for c in completion:
        dict[c] -= 1
    
    for p in dict:
        if dict[p] > 0:
            return p
