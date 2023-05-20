A = input()

def cnt_func(A):
    cnt = 0
    for i in range(len(A)-2):
        if A[i] != A[0]:
            return True
    return False

if cnt_func(A):
    print("Yes")
else:
    print("No")