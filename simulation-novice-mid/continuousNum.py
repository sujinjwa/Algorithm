# 입력받을 숫자 개수 나타내는 변수 n
n = int(input())

# n개의 줄에 걸쳐 한 줄에 하나씩 숫자 입력받고 배열 arr에 저장
arr = [
	int(input())
	for _ in range(n)
]

# 연속하여 동일한 숫자가 나오는 횟수를 구해보며,
# 그 중 최댓값을 갱신합니다.
ans, cnt = 0, 0
# ans: 연속하여 동일한 숫자 나오는 횟수들 중 현재까지 최대값인 변수
for i in range(n):
		# Case 1 : 연속한 두 원소가 일치하는 경우
		if i >= 1 and arr[i] == arr[i - 1]:
				cnt += 1 # 동일한 숫자 나오는 횟수로써 cnt는 1 증가
		# Case 2 : 연속한 두 원소가 일치하지 않는 경우
		else: 
				cnt = 1 # cnt를 1로 초기화

		# 현재까지 최대값이었던 ans와 현재 구하진 값인 cnt값을 비교하여 그 중 더 큰 값을 다시 ans에 대입
		ans = max(ans, cnt)

print(ans)