n = int(input())

def get_sum(n):
    if n == 1:
        return 1
    
    return get_sum(n-1) + n

result = get_sum(n)
print(result)