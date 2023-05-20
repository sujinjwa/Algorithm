n = int(input()) # n개: 원소의 개수
arr = list(map(int, input().split())) # n개의 원소 입력 받기

# partition함수 : low부터 high까지의 숫자들을 빨간 / 파란색 화살표로 순회하며,
# arr[high]인 pivot 기준으로 작은 숫자와 큰 숫자 구분
def partition(low, high):

    pivot = arr[high] # 기준 숫자
    i = low - 1 # i : 파란색 화살표의 위치 (pivot보다 작은 숫자가 이동하여 위치할 index)

    # j : 빨간색 화살표의 위치
    # (pivot인 arr[high] 제외한 모든 숫자 순회하며 pivot 보다 작은지 큰지 확인하기 위한 index)
    for j in range(low, high): # 이때, j는 low부터 high - 1까지 순회. pivot인 arr[high]까지는 순회하지 않아도 되니까.
        
        # 빨간색 화살표가 가리키는 원소가 pivot보다 작다면,
        # pivot보다 왼쪽에 위치해야 하므로 두 원소의 위치 바꿔줌
        if arr[j] < pivot:
            i += 1 # 파란색 화살표 위치 + 1 이동
            arr[i], arr[j] = arr[j], arr[i] # 두 숫자끼리 swap
    
    # 최종적으로 pivot을 경계(i + 1)에 있는 원소와 교환해주기
    # 이때 경계란, pivot보다 작은 숫자들의 모임과 큰 숫자들의 모임 사이의 위치!
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1 # pivot의 최종 위치 반환


def quick_sort(low, high):
    # 배열 arr 내 원소의 개수가 2개 이상인 경우에만 진행
    # 배열 내 원소 0개 또는 1개만 있는 경우 진행 x
    if low < high:
        # partition함수 : low부터 high까지 arr[high] 기준으로 작은 숫자, 큰 숫자 구분하는 함수
        # 이때, 아래의 pos는 반환될 기준 숫자가 되는 pivot의 최종 위치임
        pos = partition(low, high) # 해당 pivot의 위치를 pos에 넣어줌

        # 중간 숫자인 pos 기준으로 양쪽 배열에 quick sort 진행. 이때 pos는 어디에도 속하지 않음.
        quick_sort(low, pos - 1) # pivot의 왼쪽 구간의 원소들 정렬
        quick_sort(pos + 1, high) # pivot의 오른쪽 구간의 원소들 정렬

# 시작!
quick_sort(0, n - 1)

# 정렬된 배열의 원소들 출력
for elem in arr:
    print(elem, end=' ')