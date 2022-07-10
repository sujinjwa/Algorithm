n = int(input()) # n개: 원소의 개수
arr = list(map(int, input().split())) # n개의 원소 입력 받기

def partition(low, high):

    pivot = arr[high]
    i = low - 1 # 파란색 화살표 위치 정해주기
    # 주의!
    # 파란색 화살표 위치에 pivot보다 작은 원소 있더라도
    # arr[i]와 arr[j] 값 swap 해주고, i += 1 해줘야 함

    for j in range(low, high): # 빨간색 화살표 움직이기
        
        # 빨간색 화살표가 가리키는 원소가 pivot보다 작다면,
        # 왼쪽으로 가야 하므로 두 원소의 위치 바꿔줌
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 최종적으로 pivot을 경계에 있는 원소와 교환해주기
    # 이때 경계란, 마지막 파란색 화살표 위치에 1을 더한 위치
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1 # pivot의 최종 위치 반환


def quick_sort(low, high):
    # 배열 내 원소의 개수가 2개 이상인 경우에만 진행
    if low < high:
        pos = partition(low, high) # 해당 pivot의 위치를 pos에 넣어줌

        quick_sort(low, pos - 1) # pivot의 왼쪽 구간의 원소들 정렬
        quick_sort(pos + 1, high) # pivot의 오른쪽 구간의 원소들 정렬


quick_sort(0, n - 1)

# 정렬된 배열의 원소들 출력
for elem in arr:
    print(elem, end=' ')