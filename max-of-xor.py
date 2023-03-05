from operator import xor

# n : 입력 받을 수 있는 음이 아닌 정수의 총 개수, m : 그 중 뽑을 수 있는 숫자의 개수
n, m = tuple(map(int, input().split()))
numbers = list(map(int, input().split())) # n개의 수 입력 받기
numbers = [0] + numbers
arr = [] # m개의 숫자로 이루어진 수열 담기 위한 배열
# visited = [False] * (n + 1)
max_result = 0

# arr 내 숫자들의 xor 연산 수행하는 함수
def calculate():
    result = arr[0]
    for i in range(1, m):
        result = xor(result, arr[i])
    
    return result

# arr의 curr_num번째에 위치한 숫자 고르는 함수
def choose(curr_num, last_idx):
    global max_result

    if curr_num == m + 1:
        max_result = max(max_result, calculate())
        return
    
    # O(N^M)의 시간복잡도를 O(C(N, M))으로 줄인 방법
    # for문을 1 ~ n까지 돌리지 않고
    # last_index + 1부터 n 까지 돌려서 이미 고려한 숫자들은 절대 선택되지 않도록 하기!
    # 그래서 기존의 visited 배열도 필요 없음
    for i in range(last_idx + 1, n + 1):
        # if visited[i]:
        #    continue
    # for i in range(1, n + 1):
    #     if visited[i]:
    #         continue
        
        arr.append(numbers[i])
        # visited[i] = True
        choose(curr_num + 1, i)
        arr.pop()
        # visited[i] = False

choose(1, 0)
print(max_result)