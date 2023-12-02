# 프로그래머스 > 2023 KAKAO BLIND RECRUITMENT > '개인정보 수집 유효기간' 문제 (level 1)

# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370#

# 시간 복잡도 : O(N)

# 공간 복잡도 : O(N)

def solution(today, terms, privacies):
    today_arr = [int(elem) for elem in today.split('.')]
    
    dict = {}
    for elem in terms:
        elem = elem.split(' ')
        p, months = elem[0], elem[1]
        if p not in dict:
            dict[p] = int(months)
    
    answer = []
    for index, p in enumerate(privacies):
        p = p.split(' ')
        start_date = p[0].split('.')
        privacy = p[1]
        
        next_year, next_month, next_date = [int(elem) for elem in start_date]
        
        # 만기날짜의 월자 구하기
        next_month += dict[privacy]
        if next_month > 12:
            next_year += (next_month // 12)
            next_month -= 12 * (next_month // 12)
            if next_month == 0:
                next_month = 12
                next_year -= 1
        
        # 만기날짜의 일자 구하기
        if next_date == 1:
            next_date = 28
            if next_month == 1:
                next_month = 12
                next_year -= 1
            else:
                next_month -= 1
        else:
            next_date = int(start_date[2]) - 1
        
        # 만기날짜가 오늘날짜보다 초과하는 경우
        if next_year < today_arr[0]:
            answer.append(index + 1)
            continue
        elif next_year == today_arr[0]:
            if next_month < today_arr[1]:
                answer.append(index + 1)
                continue
            elif next_month == today_arr[1]:
                if next_date < today_arr[2]:
                    answer.append(index + 1)
                    continue

    return answer