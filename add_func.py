n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))
cnt = 0

def change_m():
    global m
    while(m >= 1):
        add_A(m)
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1

def add_A(m):
    global cnt
    cnt += A[m-1]

change_m()
print(cnt)