n = int(input()) # n : 입력 받을 명령 개수

d = dict() # 빈 hashmap 생성

# order를 input()으로 입력 받고
# order.startswith('명령어')로 조건문 구분 가능
for _ in range(n):
    order = list(input().split(' '))
    k = order[1]

    if order[0] == 'add':
        v = order[2]
        d[k] = v # (k, v) 쌍을 hashmap에 추가

    elif order[0] == 'remove':
        d.pop(k) # key가 k인 쌍을 찾아 제거
    
    elif order[0] == 'find':
        # key가 k인 쌍이 hashmap에 있는지 판단
        # 있따면 value 출력, 없다면 None 출력
        if k in d:
            print(d[k])
        else:
            print('None')