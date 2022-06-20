import sys

n = int(input())
a = list(map(int, input().split()))

# 새로운 배열을 만들어 정렬하고
# 2번째로 작은 숫자 찾아낸다
myarr = sorted(a)

# isexist : 2번째로 작은 숫자가 존재하면 true
# min_num : 가장 작은 원소
# second_min_num : 두 번째로 작은 원소
isexist = False
min_num = myarr[0]
second_min_num = 0

for elem in myarr:
    # 가장 처음으로 발견된 myarr[0]과 다른 숫자는
    # 두 번째로 작은 숫자이다
    if elem != min_num:
        second_min_num = elem
        isexist = True
        break

# 2번째로 작은 숫자가 존재하지 않을 때
if isexist == False:
    print(-1)
    sys.exit()

ansidx = -1 # 2번째로 작은 숫자가 여러 개 있는지 확인하기 위한 변수
for idx, elem in enumerate(a):
    if elem == second_min_num:
        # 2번째로 작은 숫자가 여러 개 있을 때
        if ansidx != -1:
            # low2와 동일한 elem이 두 개 이상 있을 경우
            # ansidx 가 -1이 아닌 조건을 만족한다
            print(-1)
            sys.exit()
        
        ansidx = idx

print(ansidx + 1)