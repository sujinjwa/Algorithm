a, b = tuple(map(int, input().split()))

def calculate(a, b):
    if a >= b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a, b

a, b = calculate(a, b)
print(a, b)