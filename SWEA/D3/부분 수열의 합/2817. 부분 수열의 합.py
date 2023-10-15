T = int(input())

def dfs(curr_index, amount):
    global n, k, arr, ans
    
    if amount == k:
        ans += 1
        return
    
    if curr_index >= n:
        return
    
    if amount > k:
        return
    
    dfs(curr_index + 1, amount + arr[curr_index])
    dfs(curr_index + 1, amount)

for test_case in range(1, T + 1):    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = 0
    
    dfs(0, 0)
    
    print("#%d %d"%(test_case, ans))