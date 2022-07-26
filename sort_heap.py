n = int(input()) # 원소의 개수 : n개
input_arr = list(map(int, input().split()))
arr = [0] + input_arr

def heapify(arr, n, i):
    largest = i # 해당 (부모) 노드
    left = i * 2 # 부모 노드(i)의 왼쪽 자식 노드
    right = i * 2 + 1 # 부모 노드(i)의 오른쪽 자식 노드
    
    if left < n and arr[left] > arr[largest]: # 왼쪽 자식 노드가 더 큰 경우
        largest = left
    
    if right < n and arr[right] > arr[largest]: # 오른쪽 자식 노드가 더 큰 경우
        largest = right

    if largest != i: # 자식 노드가 부모 노드보다 더 큰 경우
        arr[largest], arr[i] = arr[i], arr[largest] # 두 값을 swap
        heapify(arr, n, largest) # largest인 자식 노드에서 다시 heapify 진행


# 첫 번째 heapify 진행
# n / 2 부터 1번째 노드까지
# 이때 i := 해당 노드
for i in range(n//2, 0, -1):
    heapify(arr, n + 1, i) # (고민 필요) 왜 n이 아니라 n + 1인지 좀 더 고민 필요!

# 두 번째 heapify 진행
# 이때 1번째 노드가 최댓값이므로 마지막 노드와 swap 해줌
# 이후 1번째 노드 기준으로 max-heap 만들기 위해 heapify 진행
for i in range(n, 0, -1):
    arr[i], arr[1] = arr[1], arr[i]
    heapify(arr, i, 1)

# 출력
for i in range(1, n+1):
    print(arr[i], end=' ')