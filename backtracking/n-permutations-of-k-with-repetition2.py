k, n = list(map(int, input().split())) # k : 최대 숫자 범위, n : 총 자릿수
arr = []

# 출력
def print_arr():
    for elem in arr:
        print(elem, end=" ")
    print()

# arr에서 num번째 자리에 위치할 숫자 1 ~ k 중 선택
def choose(num):
    
    # 종료 조건 : num이 arr의 인덱스 범위 초과할 때
    if num == n:
        print_arr()
        return

    # arr의 num번째 자리에 1이상 k이하의 숫자 중 순서대로 선택
    for i in range(1, k + 1):
        # 연속하여 같은 숫자가 3번 이상 나오는 경우 제외
        if num >= 2 and arr[num - 2] == arr[num - 1] and arr[num - 1] == i:
            continue
        
        else:
            arr.append(i)
            choose(num + 1)
            arr.pop()
        
choose(0)