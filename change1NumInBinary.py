import sys

a = list(input()) # 2진수 숫자 a 입력 받기
INT_MIN = -sys.maxsize # 정수 중 가장 작은 값

max_n = INT_MIN # INT_MIN으로 가장 큰 N 초기화

# a의 10진수 숫자 리턴하는 함수
def find_n(a):
    N = 0 # 10진수 숫자 N 선언
    j = 0 # 2진수 내 숫자의 index 나타내는 변수
    # a의 맨 뒷 index부터 반대로 순회하는 반복문
    for i in range(len(a)-1, -1, -1):
        N += int(a[i]) * (2 ** j) # N에 a[i] * 2^j 값 더하기
        j += 1 # a의 index 1 증가
    return N # a의 10진수 숫자 리턴

# a의 숫자 하나씩 바꾸는 반복문
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        max_n = max(max_n, find_n(a)) # i번째 숫자만 바꾼 a의 10진수 찾는 함수 호출
        a[i] = '0' # 바꾼 a[i] 원래대로 변환
    else:
        a[i] = '0'
        max_n = max(max_n, find_n(a)) # i번째 숫자만 바꾼 a의 10진수 찾는 함수 호출
        a[i] = '1' # 바꾼 a[i] 원래대로 변환

print(max_n) # N 중 최대값 출력