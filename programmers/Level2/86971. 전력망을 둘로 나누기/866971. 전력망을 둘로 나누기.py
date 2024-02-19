import sys

def reset_visited(visited):
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j] = False

def dfs(node, visited, graph, arr):
    for i in range(len(graph[node])):
        if graph[node][i] and not visited[node][i]:
            visited[node][i] = True
            arr.append(i)
            dfs(i, visited, graph, arr)
    
def solution(n, wires):
    graph = [
        [False for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    visited = [
        [False for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    # 1. 연결 여부를 2차원 배열로 저장
    for wire in wires:
        v1, v2 = wire
        graph[v1][v2], graph[v2][v1] = True, True

    # 2. 각 연결선을 하나씩 찾아서
    # 그 연결선에 연결된 노드 2개를 출발점으로 dfs 탐색
    # (graph를 '\' 선으로 나눴을 때 우상단 부분만 확인하면 됨)
    min_abs_answer = sys.maxsize
    for col in range(1, n + 1):
        for row in range(col, n + 1):
            if graph[row][col]: # 연결선인 경우
                # print('연결 노드: ', v1, v2)
                v1, v2 = row, col
                
                # 노드 v1을 시작점으로 dfs 탐색
                reset_visited(visited)
                visited[v1][v2] = True
                visited[v2][v1] = True
                arr = []
                arr.append(v1)
                dfs(v1, visited, graph, arr)
                # print(arr)
                num = len(set(arr))
                
                # 노드 v2를 시작점으로 dfs 탐색
                reset_visited(visited)
                visited[v1][v2] = True
                visited[v2][v1] = True
                arr = []
                arr.append(v2)
                dfs(v2, visited, graph, arr)
                # print(arr)
                num2 = len(set(arr))
                
                min_abs_answer = min(min_abs_answer, abs(num - num2))
                
    return min_abs_answer