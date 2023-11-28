import sys
from collections import deque

# n : 정점의 개수, m : 간선의 개수, 탐색 시작할 정점 번호 : v
n, m, start_v = tuple(map(int, input().split()))

nodes = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]
visited2 = [False for _ in range(n + 1)]

for start, end in nodes:
    graph[start][end] = 1
    graph[end][start] = 1

dfs_arr = []
bfs_arr = []
q = deque()

def dfs(vertex):
    for i in range(1, n + 1):
        if graph[vertex][i] and not visited[i]:
            visited[i] = True
            dfs_arr.append(i)
            dfs(i)

def bfs():
    while q:
        curr_v = q.popleft()

        for i in range(1, n + 1):
            if graph[curr_v][i] and not visited2[i]:
                visited2[i] = True
                bfs_arr.append(i)
                q.append(i)

visited[start_v] = True
dfs_arr.append(start_v)
dfs(start_v)

q.append(start_v)
bfs_arr.append(start_v)
visited2[start_v] = True
bfs()

# dfs 출력
for elem in dfs_arr:
    print(elem, end = ' ')
print()

# bfs 출력
for elem in bfs_arr:
    print(elem, end = ' ')