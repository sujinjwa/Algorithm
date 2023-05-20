def swap(a, b):
    tmp = a
    a = b; b = tmp
    print('{}, {}, '.format(a, b), end='')

a = 2;b = 3
swap(a, b)
print('{}, {}'.format(a, b))