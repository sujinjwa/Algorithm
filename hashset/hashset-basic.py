n = int(input()) # n : 명령의 개수

s = set() # hashset 선언, {} 도 가능

for _ in range(n):
    orders = input()

    # 명령어가 add x 라면 숫자 x를 hashset에 추가
    if orders.startswith('add'):
        s.add(int(orders.split()[1]))

    # 명령어가 remove x 라면 숫자x를 hashset에서 제거
    elif orders.startswith('remove'):
        s.remove(int(orders.split()[1]))
    
    # 명령어가 find x 라면 숫자x가 hashset에 있는지 판단
    else:
        if int(orders.split()[1]) in s:
            print('true')
        else:
            print('false')