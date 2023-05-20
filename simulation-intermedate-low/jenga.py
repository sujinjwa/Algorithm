n = int(input()) # 블럭의 수 : n개
block = [
    int(input())
    for _ in range(n) # 맨 위에서부터 맨 아래까지 순서대로 각 층 블럭의 숫자 입력
]

# 첫 번째로 제거할 블럭의 정보로, s1번째부터 e1번째까지의 블럭 삭제함
s1, e1 = list(map(int, input().split()))
# 두 번째로 제거할 블럭의 정보로, s2번째부터 e2번째까지의 블럭 삭제함
s2, e2 = list(map(int, input().split()))

temp = [] # 첫 번째 블록 빼기 작업한 결과 집어넣을 임시 배열 temp 선언
for i in range(s1 - 1, e1): # block의 s1번째부터 e1번째까지 숫자 0으로 변환
    block[i] = 0

for elem in block: # 0으로 변환된 숫자 제외한 모든 숫자 temp에 추가
    if elem == 0:
        continue
    temp.append(elem)

temp2 = [] # 두 번째 블록 빼기 작업한 결과 집어넣을 임시 배열 temp2 선언
for i in range(s2 - 1, e2): # temp1의 s1번째부터 e1번째까지 숫자 0으로 변환
    temp[i] = 0

for elem in temp: # 0으로 변환된 숫자 제외한 모든 숫자 temp2에 추가
    if elem == 0:
        continue
    temp2.append(elem)

# 출력
print(len(temp2)) # 남은 블럭의 개수 출력

for elem in temp2: # 남은 블록에 적힌 숫자들 한줄에 하나씩 출력
    print(elem)