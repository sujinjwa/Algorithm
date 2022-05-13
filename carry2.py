import sys
INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

# 모든 쌍을 다 잡아보기
ans = INT_MIN
for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			carry = False # 각 자릿수 합마다 캐리 발생하는지 확인하는 boolean 함수
			
			# 일의 자리에서 carry가 발생하는 경우
			if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
				carry = True
			
			# 십의 자리에서 carry가 발생하는 경우
			if arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10:
				carry = True
			
			# 백의 자리에서 carry가 발생하는 경우
			if arr[i] % 1000 // 100 + arr[j] % 1000 // 100 + arr[k] % 1000 // 100 >= 10:
				carry = True
			
			# 천의 자리에서 carry가 발생하는 경우
			if arr[i] % 10000 // 1000 + arr[j] % 10000 // 1000 + arr[k] % 10000 // 1000 >= 10:
				carry = True
			
			if carry == False: # 모든 자릿수에서 carry 발생하지 않은 경우
				ans = max(ans, arr[i] + arr[j] + arr[k]); # 세 정수의 합의 최댓값 갱신

print(ans)