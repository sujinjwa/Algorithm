n = int(input()) # n : 출력하는 숫자 중 최댓값

# 1부터 n까지 숫자 차례대로 출력
def print_asc(num):
    if num == n + 1:
        print()
        return
    
    print(num, end=' ')
    print_asc(num + 1)

# n부터 1까지 숫자 차례대로 출력
def print_desc(num):
    if num == 0:
        return
    
    print(num, end=' ')
    print_desc(num - 1)

print_asc(1)
print_desc(n)


# 두 번째 방법
# 출력하는 코드를 재귀함수 호출 전 / 후 중 어디에 두는지에 따라
# 출력 결과 달라짐
def print_asc2(n):
    if n == 0:
        return
    
    print_asc2(n - 1)
    print(n, end=" ")

def print_desc2(n):
    if n == 0:
        return
    
    print(n, end=' ')
    print_desc2(n - 1)

print_asc2(n)
print()
print_desc2(n)