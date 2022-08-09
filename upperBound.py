arr = [1, 2, 3, 3, 3, 5, 8, 11, 16]
target = 3

left = 0
right = len(arr) - 1
min_idx = len(arr) # 최솟값을 답으로 출력해야 하므로, 답이 될 수 있는 값보다 더 큰 값으로 우선 설정

while left <= right:
    mid = (left + right) // 2

    if arr[mid] > target:
        right = mid - 1 # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 있으므로, right를 mid - 1로 변환
        min_idx = min(min_idx, mid) # 큰 값들의 위치 중 최솟값 계속 갱신
    
    else:
        left = mid + 1 # 같거나 작은 경우라면 left값 바꿔줌

print(min_idx) # 조건을 만족하는 최소 index 값 반환