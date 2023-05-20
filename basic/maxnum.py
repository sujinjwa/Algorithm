n = int(input())
nums = list(map(int, input().split()))
arr = [0] * (max(nums)+1)

for elem in nums:
    arr[elem] += 1 # 각 숫자 개수 저장

for i in range(len(arr)-1, -1, -1):
    if arr[i] == 1:
        print(i)
        break
    if i == 0 and arr[i] != 1:
        print(-1)