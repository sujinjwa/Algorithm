n = int(input()) # 선분의 개수 : n개
# n개의 각 선분 정보 (a, b) 입력받기
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0 # n-3개의 선분끼리 모두 겹치지 않는 서로 다른 가짓수

for i in range(n): # 3개의 i, j, k번째 선분 제거
    for j in range(i+1, n):
        for k in range(j+1, n):

            new_lines = [] # n-3개의 선분끼리 모여있는 새 배열 생성
            for l in range(n):
            
                if l != i and l != j and l != k: # i, j, k번째 선분 제외한 나머지 선분들 new_lines 배열에 추가
                    new_lines.append(lines[l])

            new_lines.sort() # 첫 번째 요소 기준 new_lines 오름차순 정렬
            no_overlap = True # 두 개의 선분 겹치는지 확인하는 boolean 변수

            for m in range(1, len(new_lines)): # new_lines 내 선분들 순회
                
                if new_lines[m-1][1] >= new_lines[m][0] : # 두 개의 선분 겹칠 경우
                    no_overlap = False
                    break
                
            if no_overlap: # 겹치는 선분 없을 경우
                cnt += 1

print(cnt)