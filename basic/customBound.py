arr = [1, 2, 3, 3, 3, 5, 8, 11, 16]
target = 3

left = 0
right = len(arr) - 1
max_idx = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] <= target: # 선택한 원소 arr[mid]가 target보다 같거나 작다면
        left = mid + 1 # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 있으므로, left를 mid + 1로 변환
        max_idx = max(max_idx, mid) # 같거나 작은 값들의 위치 중 최댓값 계속 갱신
    
    else:
        right = mid - 1 # 선택한 원소 arr[mid]의 값이 target보다 더 큰 경우라면, right를 mid - 1로 변환

print(max_idx) # 조건을 만족하는 최대 index 값 반환