c = int(input()) # c : 컴퓨터의 수
n = int(input()) # n : 쌍의 수

graph = [
    [0 for _ in range(c + 1)]
    for _ in range(c + 1)
]

visited = [False for _ in range(c + 1)]

for _ in range(n):
    node1, node2= tuple(map(int, input().split()))
    
    graph[node1][node2] = 1
    graph[node2][node1] = 1

for i in range(c + 1):
    graph[i][i] = 1

def can_visit(curr_node, i):
    return graph[curr_node][i] and not visited[i]

def dfs(curr_node):
    for i in range(c + 1):
        if can_visit(curr_node, i):
            visited[i] = True
            dfs(i)

start_node = 1
visited[start_node] = True
dfs(start_node)

cnt = 0
for elem in visited:
    if elem:
        cnt += 1

print(cnt - 1)