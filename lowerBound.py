arr = [1, 2, 3, 3, 3, 5, 8, 11, 16]
target = 3

left = 0
right = len(arr) - 1
min_idx = len(arr) # 답으로 최솟값을 구하는 것이므로, 더 큰 값으로 설정

while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target: # 만약에 선택한 원소가 target보다 같거나 크다면
        right = mid - 1 # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 있으므로, right을 mid - 1 로 변환
        min_idx = min(min_idx, mid) # 같거나 큰 값들의 위치 중 최솟값을 계속 갱신
    
    else:
        left = mid + 1
    
print(min_idx)
