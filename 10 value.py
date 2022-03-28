nums = list(map(int, input().split()))

arr = [0] * 10

for elem in nums:
    if elem == 0:
        break
    num = elem // 10 # 10의 자리 수
    arr[num] += 1

for i in range(1, 10):
    print(f"{i} - {arr[i]}")
