# 변수 선언 및 입력
x, y = tuple(map(int, input().split()))


# 각 자리 숫자의 합을 구하여 반환하는 재귀 함수
def digit_sum(n):
    if n < 10:
        return n
    # 두 자리 이상의 숫자라면,
    # 맨 끝자리를 제외한 숫자들의 합을 재귀적으로 호출한 뒤,
    # 그 결과가 마지막 자릿수를 더해 반환
    else:
        return digit_sum(n // 10) + (n % 10)


ans = 0

# 각 숫자 i에 대해 
# 각 자리 숫자의 합을 구해
# 그 중 최댓값을 계산
for i in range(x, y + 1):
    ans = max(ans, digit_sum(i))
    
print(ans)