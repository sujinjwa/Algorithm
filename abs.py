n = int(input())

_list = list(map(int, input().split()))

def abs_func(_list):
    for i in range(n):
        _list[i] = abs(_list[i])
    return _list

new_list = abs_func(_list)

for elem in new_list:
    print(elem, end=' ')