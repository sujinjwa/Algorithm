n = int(input()) # 원소 n개
arr = list(map(int, input().split())) # n개의 원소 입력 받기

p = 1 # 1의 자릿수부터 최대 자릿수까지 digit 값 갱신하기 위해 사용되는 값

# 입력받을 수 있는 최대 원소 값이 100,000으로 정해져 있으므로
# for문은 최대 6 자리까지 조회하면 된다
for _ in range(6): # 1의 자릿수부터 6의 자릿수까지 모든 자릿수 조회
    
    new_arr = [ [] for _ in range(10) ] # 0~9까지의 자릿수 숫자를 index로 나타낸 배열
 
    # arr내 모든 원소 하나씩 순서대로 순회하여
    # 해당 자릿수(p)에 위치한 숫자 기준으로 정렬 진행
    for elem in arr:
        digit = (elem // p) % 10 # 1, 2, .. 자릿수
        new_arr[digit].append(elem) # arr 내 해당 원소(elem)를 new_arr의 해당 자릿수 행(digit)에 넣기
    
    arr = [] # new_arr 통해 새로이 정렬된 숫자를 arr에 복사하기 위해 빈 배열로 재선언
    # arr2 = [] # 새로운 배열 arr2 선언
    # 해당 자릿수를 기준으로 정렬된 new_arr에 추가된 순서대로 arr 에 값 넣기
    for row in new_arr:
        for elem in row:
            if elem:
                arr.append(elem)
                # arr2.append(elem)
    
    # arr = arr2 # new_arr 내 요소 순서대로 추가한 arr2를 arr에 복사

    p *= 10 # 다음 자릿수 조회하기 위해(digit 갱신 위해) p에 10 곱하기

# 오름차순 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')
    