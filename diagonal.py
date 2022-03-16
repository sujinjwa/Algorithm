n, m = list(map(int, input().split()))

answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

count = 1

def fill_diagonal(cur_row, cur_col):
    global count

    while 0 <= cur_col and cur_row < n:
        answer[cur_row][cur_col] = count

        cur_row += 1
        cur_col -= 1
        count += 1

for start_col in range(m):
    fill_diagonal(0, start_col)

for start_row in range(1, n):
    fill_diagonal(start_row, m-1)

for row in range(n):
    for col in range(m):
        print(answer[row][col], end=' ')
    print()