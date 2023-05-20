# 정수 num과 바꿀 진수 n 입력 
num, n = list(map(int, input().split()))
changed_num = [] # num을 n으로 나눈 나머지 저장할 리스트
reversed_changed_num = [] # 순서가 reversed된 changed_num

if n == 4:
    while True:
        if num < 4:
            changed_num.append(num)
            break
        
        changed_num.append(num % 4)
        num //= 4

else:
    while True:
        if num < 8:
            changed_num.append(num)
            break
        
        changed_num.append(num % 8)
        num //= 8

# changed_num에 저장된 나머지 반대 순서로 reversed_changed_num 리스트에 저장
for elem in changed_num[::-1]:
    reversed_changed_num.append(elem)

# 출력
for elem in reversed_changed_num:
    print(elem, end='')