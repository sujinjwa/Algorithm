A = list(input()) # '(', ')'로만 이루어진 문자열 입력 받기

count = 0 # 여는 괄호와 닫는 괄호의 쌍을 이루는 가지수
for i in range(len(A)):
    if A[i] == '(': # 여는 괄호일 경우
        for j in range(i+1, len(A)): # A[i]의 다음 위치부터 순회
            if A[j] == ')': # 닫는 괄호일 경우
                count += 1

print(count)