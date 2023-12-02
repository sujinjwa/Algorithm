# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    pets = {}
    for num in nums:
        if num not in pets:
            pets[num] = 1
        else:
            pets[num] += 1

    answer = len(pets) if len(pets) <= len(nums) / 2 else len(nums) // 2
    return answer

# 다른 사람 답안
def solution(ls):
    return min(len(ls)/2, len(set(ls)))