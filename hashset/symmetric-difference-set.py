# a : 집합 A의 원소 개수, b : 집합 B의 원소 개수
a, b = map(int, input().split())

# arr1 : 집합 A의 모든 원소, arr2 : 집합 B의 모든 원소
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# arr1과 arr2를 hashSet으로 변환
set1 = set(arr1)
set2 = set(arr2)

answer = []

# 집합 A - B인 부분 answer에 추가
for elem in set1:
    if elem not in set2:
        answer.append(elem)

# 집합 B - A인 부분 answer에 추가
for elem in set2:
    if elem not in set1:
        answer.append(elem)

# 집합 A와 B에 대한 대칭 차집합 원소의 개수 출력
print(len(set(answer)))