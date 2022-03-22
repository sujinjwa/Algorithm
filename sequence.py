n = int(input())

def remain(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return remain(n-1) * remain(n-2) % 100

print(remain(n))