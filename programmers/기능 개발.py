# 스택/큐 문제 : 기능 개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    # 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
    
    # 1. 각 progresses에 speeds 기준 배포 몇 번 필요한지 새로운 arr에 기록
    # 2. 앞 기능부터 순회하는데
    #    조회한 기능이 뒤에 있는 기능보다 크면 다같이 배포
    #    조회한 기능이 뒤에 있는 기능보다 작으면 혼자서 배포
    
    arr = []
    for p, s in zip(progresses, speeds):
        # (p + s * count) >= 100
        # count * s >= 100 - p
        # count >= (100 - p) / s
        count = math.ceil((100 - p) / s)
        arr.append(count)
        
    answer = []  
    i = 0
    while True:
        if i > len(arr) - 1:
            break
        cnt = 1
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                cnt += 1
            else:
                break
        
        answer.append(cnt)
        i += cnt

    return answer