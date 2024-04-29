def solution(citations):
    max_h = 0
    
    counts = [0 for _ in range(10000 + 1)]

    # 모든 논문 조회하며 모든 논문의 인용된 숫자가 index인 10,000 크기의 1차원 배열 만들기
    for citations in citations:
        counts[citations] += 1
    
    # 0 ~ 10,000까지 중 h-index 구하기
    for h in range(10000 + 1):
        # h번 이상 인용된 논문 개수
        counts_more_than_h = sum(counts[h:])
        
        # h번 이하 인용된 논문 개수
        counts_less_than_h = sum(counts[:h-1])
        
        # h번 이상 인용된 논문이 h편 이상이면서 나머지 논문이 h번 이하 인용되면
        if counts_more_than_h >= h and counts_less_than_h <= h:
            max_h = h
    
    return max_h