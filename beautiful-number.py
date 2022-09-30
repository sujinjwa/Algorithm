n = int(input()) # n : 자릿수
arr = [] # 1 ~ 4의 숫자로만 이루어진 모든 수열 담기 위한 배열


# arr가 아름다운 수인지 확인
def isBeauti():
    i = 0 # i : 연속하는 수열의 첫번째 인덱스
    while i < n: # i : 0 ~ 3

        # i + arr[i] - 1 : 연속하는 수열의 마지막 인덱스
        # 마지막 인덱스가 총 수열 내에 포함되는지 확인
        if i + arr[i] - 1 >= n:
            return False
        
        # i부터 i + arr[i] - 1까지 돌면서 모두 arr[i] 인지 확인
        for j in range(i, i + arr[i]):
            if arr[j] != arr[i]:
                return False
        
        # 앞에서 i부터 arr[i] - 1까지 모두 arr[i] 인지 확인했으므로
        # 그 구간은 또 조회할 필요 없으므로
        # 그 구간만큼 건너뛴다
        i += arr[i]
    
    return True


beauti_cnt = 0 # 아름다운 수열의 총 개수

# num 번째 자리에 위치할 숫자 1 ~ 4 중 선택
def makeNum(num):

    global beauti_cnt

    # num번째 자리까지 채워지고 n자리 수 완성되면 
    # isBeauti() 를 통해 아름다운 수인지 확인
    if num == n + 1:
        if isBeauti():
            beauti_cnt += 1
        return
    
    # arr의 num번째 자리에 위치할 숫자 1 ~ 4 중 선택하여
    # 모든 경우 조회
    for i in range(1, 5):
        arr.append(i)
        makeNum(num + 1)
        arr.pop()
    
    return

makeNum(1)
print(beauti_cnt)