n = int(input())

def recur(n):
    if n == 0:
        return 2
    
    elif n == 1:
        return 4
    
    return (recur(n - 1) * recur(n - 2)) % 100

print(recur(n - 1))