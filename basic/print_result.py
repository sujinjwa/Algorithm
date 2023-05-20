num = 5

def g():
    global num
    print(num, end=" ")
    num += 9

def f():
    num = 7
    print(num, end=" ")
    num += 2

g()
f()
g()
f()
g()