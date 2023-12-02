# 고득점KIT 스택/큐의 주식가격 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# O(N^2)인데 왜 통과야?
def solution(prices):
    answer = []
    
    # prices[i]를 prices[i]의 뒤에 위치한 모든 가격들(prices[j])과 비교하여
    # 가격이 떨어지는 경우 break 후 answer에 기간(초) 추가
    for i in range(len(prices)):
        length = 0
        for j in range(i + 1, len(prices)):
            length += 1
            if prices[i] > prices[j]:
                break
        answer.append(length)
    
    return answer

# O(N) 풀이
def solution(prices):
    stack = []
    answer = [0] * len(prices)

    # prices의 각 가격 조회하면서
    # 직전 가격(stack[-1][1])보다 저렴한 가격인 경우일 때마다
    # 직전 가격의 떨어진 기간 계산
    for i in range(len(prices)):
        # stack이 빈 배열인 경우이거나
        # 조회된 가격이 직전 가격보다 비싼 경우 상승세이므로 while문 실행 X
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop() # 직전 가격 제거
            answer[past] = i - past # past번째 가격의 떨어지지 않은 기간(초) 계산
        
        stack.append([i, prices[i]]) # 지속적으로 상승되는 경우이므로 stack에 가격 추가
    
    # 떨어지는 순간 없이 끝까지 상승세인 가격의 기간(초) 계산
    for i, _ in stack:
        answer[i] = len(prices) - 1 - i
    
    return answer

print(solution([1, 2, 3, 2, 3]))