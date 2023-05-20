n = 29
digits = []

# 숫자 29를 2진법으로 표현하여 출력
# 2로 나누기를 반복하며, 몫이 1이 되는 순간 멈춤.
# 지금까지 나왔던 나머지들을 거꾸로 순서대로 출력
while True:
    if n < 2:
        digits.append(n)
        break
    
    digits.append(n % 2)
    n //= 2

for digit in digits[::-1]:
    print(digit, end="")