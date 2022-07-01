n = int(input()) # 명령의 수
arr = [] # 동적 배열 선언

for _ in range(n): # n개의 명령 순회하기
    order = input().split() # 명령 하나씩 입력 받기

    if order[0] == 'push_back': # push_back A 명령 : 정수 A를 동적 배열의 맨 뒤에 넣기
        arr.append(int(order[1]))
    
    elif order[0] == 'pop_back': # pop_back 명령 : 배열 맨 뒤 정수 하나 삭제
        arr.pop()
    
    elif order[0] == 'size': # size 명령 : 동적 배열 내 정수의 개수 출력
        print(len(arr))
    
    else: # get k 명령 : 동적 배열 내 k번째 숫자 출력
        print(arr[int(order[1]) - 1])
