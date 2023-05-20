n1, n2 = tuple(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_right(i, j):
    if A[i+1] == B[j+1]:
        print('Yes')
        exit()
    return False

for i in range(len(A)-1):
    for j in range(len(B)-1):
        if A[i] == B[j]:
            is_right(i, j)
print('No')