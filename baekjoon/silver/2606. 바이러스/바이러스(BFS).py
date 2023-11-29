from collections import deque

# c : 컴퓨터 수
# n : 컴퓨터 쌍의 수
c = int(input())
n = int(input())

grid = [
    [0 for _ in range(c + 1)]
    for _ in range(c + 1)
]

visited = [False for _ in range(c + 1)]

for i in range(c + 1):
    grid[i][i] = 1

for _ in range(n):
    node1, node2 = tuple(map(int, input().split()))

    grid[node1][node2] = 1
    grid[node2][node1] = 1

q = deque()

def can_go(curr_x, i):
    return grid[curr_x][i] and not visited[i]

def bfs():
    while q:
        curr_x = q.popleft()

        for i in range(1, c + 1):
            if can_go(curr_x, i):
                visited[i] = True
                q.append(i)

warm_node = 1
visited[warm_node] = True
q.append(warm_node)
bfs()

cnt = 0
for elem in visited:
    if elem:
        cnt += 1

print(cnt - 1)