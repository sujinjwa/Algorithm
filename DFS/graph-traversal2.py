# n : 정점의 개수, m : 간선의 개수
n, m = tuple(map(int, input().split()))
# graph : n개의 각 정점과 간선으로 이루어진 다른 정점을 연결 리스트로 표현하기 위한 1차원 배열
graph = [[] for _ in range(n + 1)]
# visited : n개의 각 정점에 방문한 여부 확인하기 위한 1차원 배열
visited = [False for _ in range(n + 1)]
cnt = 0 # cnt : 1ㅓㄴ 정점 제외하고 간선 따라 이동시 도달할 수 있는 정점의 총 개수

# m개의 줄에 걸쳐 연결된 두 정점 (x,y) 입력 받아
# 연결 리스트 graph에 추가
for _ in range(m):
    start, end = tuple(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)

# 현재 위치한 숫자 curr_num의 다음 이동 숫자 고르기
def dfs(curr_num):
    global cnt

    # 이동한 정점 curr_num과 연결된 모든 정점(number) 조회
    for number in graph[curr_num]:
        # number가 이미 방문한 정점인 경우 제외
        if not visited[number]:
            cnt += 1
            visited[number] = True
            dfs(number) # 해당 정점 number으로 이동

visited[1] = True # 1번 정점에 방문했음을 표시
dfs(1) # 1번 정점에서 시작하여 DFS 탐색 시작
print(cnt) # 도달한 총 정점의 개수 출력