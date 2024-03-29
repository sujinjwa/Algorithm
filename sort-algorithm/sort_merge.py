n = int(input()) # 원소의 개수: n개
arr = list(map(int, input().split())) # n개의 숫자 입력 받기

# 배열 쪼개기
def divide(low, high):
    # 만약 low = high라면, 배열 내 원소의 개수가 1개이므로
    # 이미 정렬된 경우라고 할 수 있다
    if low < high: # 배열 arr 내 원소의 개수 2개 이상인 경우에만 진행

        mid = (low + high) // 2 # 가운데 원소의 위치
    
        divide(low, mid) # mid의 왼쪽 부분 병합정렬
        divide(mid+1, high) # mid의 오른쪽 부분 병합정렬
        merge(low, mid, high) # 정렬된 두 리스트 하나로 병합

merged_arr = [0] * n # 병합 이후의 결과 담기 위한 배열

# 정렬된 두 리스트 [low, mid]와 [mid+1, high]를 하나로 병합하는 함수
# 호출되는 low, mid, high 값이 경우에 따라 달라짐을 유의!
def merge(low, mid, high):

    i, j = low, mid + 1 # 각 리스트 내 첫 번째 원소 위치 잡기
    k = low # merged_arr의 index

    while i <= mid and j <= high: # 두 리스트 내 원소 남아 있다면
        if arr[i] <= arr[j]: # 첫 번째 리스트 내 원소가 더 작다면
            merged_arr[k] = arr[i] # 해당 원소를 merged_arr의 k번째로 이동
            k += 1
            i += 1
        else:
            merged_arr[k] = arr[j] # 그렇지 않다면 두 번재 리스트 내 원소를 이동
            k += 1
            j += 1
    
    while i <= mid: # 첫 번째 리스트 내 원소만 아직 남아있다면
        merged_arr[k] = arr[i] # 남은 원소들 모두 이동
        k += 1
        i += 1
    
    while j <= high: # 두 번째 리스트 내 원소만 아직 남아있다면
        merged_arr[k] = arr[j] # 남은 원소들 모두 이동
        k += 1
        j += 1
    
    for l in range(low, high + 1): # 호출 받은 low부터 high까지
        arr[l] = merged_arr[l] # 병합된 리스트 다시 원본 리스트(arr)에 이동


divide(0, n - 1) # 실제 index를 생각했을 때, low는 0, high는 n - 1 이어야 한다


# 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')