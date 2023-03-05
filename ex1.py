def solution(p):
    
    answer = [0] * len(p)
    for i in range(len(p)):

        min_val = 0

        new_p = []
        for j in range(i, len(p)): # 확정된 최솟값 제외 새로운 최솟값 구하기
            new_p.append(p[j])
        min_val = min(new_p) # i ~ n까지 중 최솟 값
        #print(min_val)
        #print(p.index(min_val))
        min_index = p.index(min_val)

        if i != min_index: # 가장 최솟값 j가 맨 앞에 위치한 게 아니라면
            # 위치 옮기기
            temp = p[i]
            p[i] = min_val
            # p[p.index(min_val)] = temp
            p[min_index] = temp

            # print(p)
            
            # 위치 변화된 idx에 + 1
            answer[i] += 1
            answer[min_index] += 1

    return answer

    # import sys
    # si = sys.stdin.readline
    # a = list(map(int, si().split()))
    ## copy.deepcopy(a)