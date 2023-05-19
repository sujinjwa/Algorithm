from sortedcontainers import SortedDict

n = int(input()) # n : 문자열의 개수

sd = SortedDict()

# n개의 문자열 입력 받고 각 개수를 value로 저장
for _ in range(n):
    word = input()
    
    if word not in sd:
        sd[word] = 1
    else:
        sd[word] += 1

# 주어진 문자열 사전순으로 출력
# 문자열이 차지핳는 비율을 백분율로 소수점 4째자리까지 반올림하여 출력
for key, value in sd.items():
    print('%s %.4f' %(key, (value/n)*100))