A = input() #'(' 또는 ')'로만 이루어진 문자열
length = len(A)

cnt = 0 # 쌍의 개수
for i in range(length-1):
    if A[i] == '(' and A[i+1] == '(':
        for j in range(i+2, length-1):
            if A[j] == ')' and A[j+1] == ')':
                cnt += 1

print(cnt)