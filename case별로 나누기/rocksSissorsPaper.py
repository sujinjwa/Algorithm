n = int(input()) # n : 가위바위보 한 횟수

# case 1 : 1이 2를 이기고, 2가 3을 이기고 3이 1을 이기는 경우
# 즉, (1, 2), (2, 3), (3, 1)인 경우

# case 2 : 1이 3을 이기고, 3이 2를 이기고 2가 1을 이기는 경우
# 즉, (1, 3), (3, 2), (2, 1)인 경우

case1_cnt = 0 # case1일 때 첫 번째 개발자의 승리 횟수
case2_cnt = 0 # case2일 때 첫 번째 개발자의 승리 횟수
for _ in range(n):
    num1, num2 = list(map(int, input().split())) # 두 개발자가 낸 가위바위보 결과 정수로 입력 받기

    if num1 == 1:
        if num2 == 2:
            case1_cnt += 1
        if num2 == 3:
            case2_cnt += 1
    
    elif num1 == 2:
        if num2 == 3:
            case1_cnt += 1
        if num2 == 1:
            case2_cnt += 1
    
    else:
        if num2 == 1:
            case1_cnt += 1
        if num2 == 2:
            case2_cnt += 1

print(max(case1_cnt, case2_cnt)) # 첫 번째 개발자가 최대로 이기는 횟수