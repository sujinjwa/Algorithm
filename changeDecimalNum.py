
binary = list(map(int, list(input())))
num = 0

# 입력받은 2진수를 10진수로 변환
for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)