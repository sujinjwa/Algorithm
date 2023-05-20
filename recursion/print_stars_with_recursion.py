n = int(input()) # n : 마지막 n번째 줄에 위치할 별의 개수

# 내가 구현한 재귀함수
def print_star(num):
    if num == n + 1: # 종료 조건
        return
    
    for _ in range(num):
        print("*", end='')
    print()
    print_star(num + 1)

print_star(1)


# 다른 방법 💥
def print_star2(n):
    if n == 0:
        return
    
    print_star2(n - 1)
    print("*" * n)

print_star2(n)