import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, list(input()))) # int형 요소로 구성된 list 입력
length = len(binary)

ans = INT_MIN # N 중 최댓값 나타내는 변수
# 각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구해준다
for i in range(length):
	# i번째 자릿수를 바꾸기
	binary[i] = 1 - binary[i] # 0 <-> 1 변환
	
	# 십진수로 변환
	num = 0
	for j in range(length):
		num = num * 2 + binary[j]
	
	ans = max(ans, num)
	
	# i번째 자릿수를 원래대로 돌려놓기
	binary[i] = 1 - binary[i]

# 출력
print(ans)