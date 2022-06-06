n, k = list(map(int, input().split())) # 폭탄 개수 : n개, 특정 거리 : k
# 폭탄 나열한 순서 입력 받기
arr = [
    int(input())
    for _ in range(n)
]

pop = [] # 폭발할 모든 폭탄 번호 저장할 배열
not_pop = True # 터지는 폭탄이 전혀 없는지 확인하는 boolean변수

# 모든 폭탄 순회
for i in range(n):
    for j in range(i+1, n):
        
        if arr[j] == arr[i] and abs(j - i) <= k: # 폭탄에 부여된 번호가 동일할 경우
            not_pop = False
            pop.append(arr[j])

if not_pop: # 터지는 폭탄이 없다면
    print(-1)
else:
    print(max(pop)) # 폭발할 폭탄 중 부여된 번호의 최댓값