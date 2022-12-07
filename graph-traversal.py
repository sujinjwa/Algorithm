n, m = list(map(int, input().split())) # n: 정점의 개수, m: 간선의 개수

# m개의 줄에 걸쳐 서로 연결된 두 정점 (x, y) 입력 받기
relation = [
    list(map(int, input().split()))
    for _ in range(m)
]

connectedNum = 0 # connectedNum : 도달할 수 있는 서로 다른 정점의 수

# 비어있는 2차원 인접 리스트 생성
graph = [
    []
    for _ in range(n + 1)
]

# 각 정점과 연결된 다른 정점에 대한 정보 담긴 인접 리스트 생성
for row, col in relation:
    graph[row].append(col)
    graph[col].append(row)

# visited: 각 정점에 방문했는지 확인하기 위한 배열
visited = [False for _ in range(n + 1)]

# 그래프의 각 정점을 DFS 탐색하는 함수
def dfs(curr_p):
    global connectedNum
    
    # 각 정점에 연결된 다른 정점(curr_v) 순회하여
    # 아직 방문하지 않은 정점이라면 그 정점으로 이동
    for curr_v in graph[curr_p]:
        if visited[curr_v] == False:
            connectedNum += 1 # 도달할 수 있는 정점의 수 +1
            visited[curr_v] = True
            dfs(curr_v)      

# 1부터 DFS 탐색 시작
curr_p = 1
visited[curr_p] = True
dfs(curr_p)

# 최종적으로 이동하여 도달할 수 있는 모든 정점의 수 출력
print(connectedNum)