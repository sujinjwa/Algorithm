n = int(input())

def print_stars(n):
    if n == 0:
        return
    
    print_stars(n-1)
    print("*" * n)

print_stars(n)