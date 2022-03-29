a, b = list(map(int, input().split()))

arr = [0] * b
while True:
    if a <= 1:
        break
    arr[a % b] += 1
    a = a // b
    
sum_ = 0
for elem in arr:
    sum_ += elem * elem

print(sum_)