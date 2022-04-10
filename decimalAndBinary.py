# 2진수 n 선언
n = list(map(int, list(input())))
num = 0 # 

# n을 십진수로 변환
for i in range(len(n)):
    num = num * 2 + n[i]

# 십진수에 17 곱한다.
num *= 17

binary = [] # 새로운 2진수 리스트 선언

#  num을 이진수로 변환
while True:
    if num < 2:
        binary.append(num)
        break
    
    binary.append(num % 2)
    num //= 2

# 이진수 출력
# 뒤집은 다음 출력해야 함.
for elem in binary[::-1]:
    print(elem, end='')