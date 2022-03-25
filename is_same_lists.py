n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def is_same():
    for i in range(n):
        if A[i] != B[i]:
            return False
    return True

if is_same():
    print('Yes')
else:
    print('No')