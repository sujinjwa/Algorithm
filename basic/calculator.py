def plus(a, o, c):
    return a+c

def minus(a, o, c):
    return a-c

def division(a, o, c):
    return a//c

def multiply(a, o, c):
    return a * c

arr = input().split()
a = int(arr[0])
o = arr[1]
c = int(arr[2])

if o == '+':
    answer = plus(a, o, c)
    print(f"{a} {o} {c} =",answer)
elif o == '-':
    answer = minus(a, o, c)
    print(f"{a} {o} {c} =",answer)
elif o == '/':
    answer = division(a, o, c)
    print(f"{a} {o} {c} =",answer)
elif o == '*':
    answer = multiply(a, o, c)
    print(f"{a} {o} {c} =",answer)
else:
    answer = False
    print(answer)