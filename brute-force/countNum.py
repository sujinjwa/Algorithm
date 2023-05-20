n = int(input()) # B가 유추하는 숫자와 카운트에 대한 정보 주어진 횟수 (n번)
# B가 A에게 n번 물어본 각 숫자와 카운트에 대한 정보 입력 받기
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0 # 정답의 가능성이 있는 숫자의 개수

# 모든 숫자 다 만들어 순회하는 반복문
# 백의 자리 수 : i,  십의 자리 수 : j,  일의 자리 수 : k
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            
            # i, j, k 중 같은 숫자가 있는지 확인
            if i == j or j == k or k == i:
                continue # B가 물어본 숫자는 각 자리의 수가 서로 다르므로, 각 자리 수 중 같은 수가 있다면 제외
        
            success = True # 해당 숫자가 정답일 때, 모든 입력에 대해 올바른 답이 나왔는지 확인하는 변수
            
            # a: B가 유추한 숫자,  num_cnt1와 num_cnt2: 숫자 a에 대한 카운트 정보
            for a, num_cnt1, num_cnt2 in arr:
                # x : 각 a의 백의 자릿수,  y : 십의 자릿수,  z: 일의 자릿수
                x = a // 100
                y = a // 10 % 10
                z = a % 10

                # cnt1 : 1번 카운트, cnt2 : 2번 카운트
                cnt1 = 0
                cnt2 = 0

                # i, j, k와 a가 유추한 x, y, z를 각각 비교하여 cnt1, cnt2 연산
                if x == i:
                    cnt1 += 1
                if y == j:
                    cnt1 += 1
                if z == k:
                    cnt1 += 1
                if x == j or x == k:
                    cnt2 += 1
                if y == i or y == k:
                    cnt2 += 1
                if z == i or z == j:
                    cnt2 += 1
                
                # 만약 카운트 수가 다르다면 해당 숫자(i, j, k)는 정답이 될 수 없음
                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    success = False
                    break
            
            if success: # 조회한 숫자 i,j,k가 B가 유추한 숫자 x,y,z와 비교했을 때 각 카운트 정보가 모두 동일한 경우
                cnt += 1 # 해당 숫자는 정답이 될 가능성 있음

print(cnt)