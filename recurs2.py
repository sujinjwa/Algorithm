n = int(input())

def asdf(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    return asdf(a//3) + asdf(a-1)

print(asdf(n))