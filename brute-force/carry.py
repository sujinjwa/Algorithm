import sys
INT_MIN = -sys.maxsize

n = int(input()) # 숫자의 개수
# n개의 숫자들 입력 받기
nums = [
    int(input())
    for _ in range(n)
]

max_sum = INT_MIN # carry(더한 숫자가 10의 자리 넘기는 것)가 발생하지 않으면서 최댓값인 값
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_of_nums = nums[i] + nums[j] + nums[k] # 서로 다른 세 정수의 모든 경우의 합
            
            str_of_sum = str(sum_of_nums) # 조회한 세 정수의 합을 문자열로 변환
            num1, num2, num3 = str(nums[i]), str(nums[j]), str(nums[k]) # 문자열로 변환

            # 세 정수의 합의 1의 자릿수부터 최대 자릿수까지 조회하는 반복문
            for l in range(len(str_of_sum)-1, -1, -1):
                # 세 정수가 세 정수의 합인 숫자의 길이와 동일해지는 만큼 왼쪽에 0 추가
                num1 = ("0" * (len(str_of_sum)-len(num1))) + num1
                num2 = ("0" * (len(str_of_sum)-len(num2))) + num2
                num3 = ("0" * (len(str_of_sum)-len(num3))) + num3
                sum_digit = int(num1[l]) + int(num2[l]) + int(num3[l]) # 세 정수의 특정 자릿수끼리의 합
                if sum_digit >= 10: # carry 발생할 경우
                    break

                if l == 0: # carry 발생하지 않고 최대 자릿수에 도달한 경우
                    max_sum = max(max_sum, sum_of_nums) # max_sum과 비교 후 세 정수의 합 중 최대값으로 갱신

# 출력
if max_sum == INT_MIN:
    print(-1)
else:
    print(max_sum)