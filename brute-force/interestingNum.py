#  ‘흥미로운 숫자’란 모든 자릿수에 있는 숫자들이 같지만, 정확히 한 자리만 다른 숫자를 의미

x, y = tuple(map(int, input().split())) # 두 개의 숫자 입력 받기

ans = 0 # 흥미로운 숫자의 개수
for i in range(x, y + 1): # x와 y 사이의 '흥미로운 숫자' 찾기
    
    num = list(str(i)) # 숫자 i를 문자로 이루어진 num으로 새로 선언
    arr = [0] * 10 # 각 숫자의 자릿수 1 ~ 9 개수 입력하기 위한 배열

    for j in range(len(num)): # num의 자릿수 순회
        for k in range(len(arr)):
            if int(num[j]) == k: # num의 자릿수가 arr의 index와 동일한 경우
                arr[k] += 1 # 해당 arr의 위치에 + 1
    
    cnt_0 = 0 # 자릿수 개수 0인 숫자 (0, 1과 a 빼고 8개여야 함)
    cnt_1 = 0 # 자릿수가 1인 개수 (1이어야 함)

    for l in range(len(arr)):
        if arr[l] == 0: # l이 자릿수인 경우가 한 번도 없는 경우
            cnt_0 += 1
        if arr[l] == 1: # l이 자릿수인 경우가 1인 경우
            cnt_1 += 1
    
    if cnt_1 == 1 and cnt_0 == 8: # 한 숫자가 자릿수인 경우가 한 번 있고, 나머지 숫자들 중 8개가 자릿수인 경우 한 번도 없는 경우
        ans += 1 # 흥미로운 숫자 개수 + 1

print(ans)