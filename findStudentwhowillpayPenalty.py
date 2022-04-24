# 학생 수 n명, 호명하게 될 횟수 m번, 벌칙 받게 되는 기준 k번 입력 받기
n, m, k = tuple(map(int, input().split()))
students = [0] * (n + 1) # 학생의 번호 별 호명된 횟수 저장하는 배열

breaker = False # 벌칙 받을 학생을 찾았을 경우 for문 빠져나오기 위한 boolean 변수
# m번에 걸쳐 벌칙받을 학생의 번호 호명하는 반복문
for _ in range(m):
    selected = int(input()) # 호명 받을 학생 번호 입력 받기
    students[selected] += 1 # 해당 학생 번호 index 요소에 + 1

    ans = -1 # 벌금 내게 될 학생의 번호 나타내는 변수
    for i in range(n+1):
        if students[i] >= k: # 호명된 횟수가 k번 이상인 학생일 경우
            ans = i
            breaker = True # 모든 for문 빠져나오기 위해 breaker = True로 설정
            break
    if breaker: # for문 빠져나오기 위한 조건
        break
    
print(ans)