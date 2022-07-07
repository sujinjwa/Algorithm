n = int(input()) # 원소 n개
arr = list(map(int, input().split())) # n개의 원소 입력 받기

p = 1 # 1의 자릿수부터 최대 자릿수까지 digit 값 갱신하기 위해 사용되는 값
# 최대 원소 값이 100,000으로 정해져 있으므로
# for문은 최대 6 자리까지 조회하면 된다
for _ in range(6): # 모든 자릿수 조회
    
    new_arr = [ [] for _ in range(10) ] # 해당하는 자릿수 숫자
    for elem in arr:

        digit = (elem // p) % 10 # 1, 2, .. 자릿수
        
        new_arr[digit].append(elem) # new_arr의 해당 자릿수 행에 elem 넣기
    
    arr = []
    # new_arr에 추가된 순서대로 arr 에 값 넣기
    for row in new_arr:
        for elem in row:
            if elem:
                arr.append(elem)

    p *= 10 # 다음 자릿수 조회하기 위해(digit 갱신 위해) p에 10 곱하기

# 오름차순 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')
    