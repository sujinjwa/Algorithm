def solution(people, limit):
    # 50,000 * 50,000 = 2500,000,000 => O(N^2) 안됨
    # sort 후
    # 가장 큰 수부터 확인하면서
    # 가장 작은 수와 더해가며 < limit인지 확인
    
    people.sort(reverse=True)
    
    answer = 0
    j = len(people) - 1
    for i in range(len(people)):
        
        if i == j:
            answer += 1
            break
        
        if i > j:
            break
        
        if people[i] + people[j] <= limit:
            j -= 1
            answer += 1
        
        else:
            answer += 1
        
    
    return answer