n = int(input())

def minus(n):
    if n <= 1:
        return 0
    
    if n % 2 == 0:
        return minus(n/2) + 1
    else:
        return minus(n*3+1) + 1

print(minus(n))