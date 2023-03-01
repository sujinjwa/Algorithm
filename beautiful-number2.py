n = int(input()) # n : 숫자의 자릿수
arr = []
beautiful_cnt = 0 # 아름다운 수열의 총 개수

# 숫자 arr이 아름다운 수인지 확인하는 함수
def is_beautiful():
    # arr에서 number로 구성된 i번째부터 시작하는 수열이
    # 아름다운 수인지 확인
    for number in range(2, 4 + 1):
        for i in range(n): # i : 수열의 첫번째 인덱스
            if (i == 0 and arr[i] == number) or (arr[i - 1] != number and arr[i] == number):
                length = 1 # length : 해당 수열에 포함된 number의 개수
                for j in range(i, n - 1):
                    if arr[j] != arr[j + 1]:
                        break
                    length += 1
                
                # length가 number의 배수인지 확인
                if length % number != 0:
                    return False
    
    return True


# curr_num번째에 위치할 숫자 고르는 함수
def choose(curr_num):
    global beautiful_cnt

    # 종료 조건
    if curr_num == n + 1:
        # 아름다운 수인지 확인
        if is_beautiful():
            beautiful_cnt += 1
        return
    
    # 1이상 4이하의 숫자로만 구성되도록 설정
    for i in range(1, 4 + 1):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)
print(beautiful_cnt) # 총 아름다운 수의 개수 출력