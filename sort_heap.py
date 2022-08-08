n = int(input()) # 원소의 개수 : n개
input_arr = list(map(int, input().split()))
arr = [0] + input_arr # 편의를 위해 배열의 0번 값은 0으로 두고 정렬에서 제외

def heapify(arr, n, i):
    largest = i # 해당 (부모) 노드의 인덱스
    left = i * 2 # 부모 노드(i)의 왼쪽 자식 노드의 인덱스
    right = i * 2 + 1 # 부모 노드(i)의 오른쪽 자식 노드의 인덱스
    
    # 주의할 점!
    # 
    if left <= n and arr[left] > arr[largest]: # 왼쪽 자식 노드가 더 큰 경우
        largest = left
    
    if right <= n and arr[right] > arr[largest]: # 오른쪽 자식 노드가 더 큰 경우
        largest = right

    if largest != i: # 자식 노드가 부모 노드보다 더 큰 경우
        arr[largest], arr[i] = arr[i], arr[largest] # 두 값을 swap
        print(arr)
        heapify(arr, n, largest) # largest인 자식 노드에서 다시 heapify 진행
        # 이때 heapify 내 파라미터인 n은 처음 입력 받은 원소의 개수인 n이 아니라
        # 해당 heapify 함수로 전달 받은 파라미터 n 을 의미 (즉, 원소의 개수 + 1 임)


# 첫 번째 heapify 진행
# n / 2 부터 1번째 노드까지 (0번 값은 제외이므로 for문의 완료값은 0)
for i in range(n//2, 0, -1):
    # i := 해당 (부모) 노드의 인덱스
    heapify(arr, n, i)
    # n 대신 n + 1 쓰려면, heapify함수 내 if 조건문에서 left <= n, right <= n 으로 수정해야 함
    # 39번 줄의 i - 1 또한 i로 수정해야 함

# 두 번째 heapify 진행
# 이때 1번째 노드가 최댓값이므로 마지막 노드와 swap 해줌
# 이후 1번째 노드 기준으로 max-heap 만들기 위해 heapify 진행
for i in range(n, 0, -1):
    arr[i], arr[1] = arr[1], arr[i]
    heapify(arr, i - 1, 1)
    # i 가 아니라 i - 1이어야 함
    # 제일 첫 최댓값을 i번째 인덱스 위치에 이미 두고 난 이후이므로,
    # arr[n]의 위치 n을 제외한 n - 1이 heapify의 범위가 되어야 함

# 출력
for i in range(1, n+1):
    print(arr[i], end=' ')