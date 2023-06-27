# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
            return False
    
    return True


# phone_book의 길이는 1이상 1,000,000 이하이므로 이중 for문 사용하면 안됨