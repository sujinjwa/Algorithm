from sortedcontainers import SortedDict

n = int(input()) # n : 원소의 개수

# arr : n개의 숫자
arr = list(map(int, input().split()))

sd = SortedDict()

# 주어진 숫자들 중복 제거하고 처음 주어진 위치를 value로 설정
for i in range(n):
    if arr[i] in sd:
        continue
    
    sd[arr[i]] = i + 1 # i + 1 : 숫자 arr[i]가 처음 주어진 위치

# sd를 key 기준 오름차순 정렬하여 출력
for key, value in sd.items():
    print(key, value)
