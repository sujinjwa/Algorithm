n = int(input())

def increase(n):
    if n == 0:
        return

    increase(n-1)
    print(n, end=' ')

def decrease(n):
    if n == 0:
        return
    
    print(n, end=' ')
    decrease(n-1)

increase(n)
print()
decrease(n)