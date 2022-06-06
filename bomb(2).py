n, k = list(map(int, input().split())) # 폭탄 개수 : n개, 특정 거리 : k
# 폭탄 나열한 순서 입력 받기
arr = [
    int(input())
    for _ in range(n)
]

ans = -1 # 터지는 폭탄 중 부여된 번호의 최댓값

# 모든 폭탄 순회
for i in range(n):
    for j in range(i+1, n):
        
        if arr[j] != arr[i] or abs(j - i) > k: # 폭탄에 부여된 번호가 동일하지 않고, 거리가 k보다 멀 경우
            continue

        ans = max(ans, arr[i]) # arr[i] := 폭탄에 부여된 번호가 arr[j]와 일치하고, 두 폭탄 간 거리가 k 이내일 때
            
print(ans) # 폭발할 폭탄 중 부여된 번호의 최댓값