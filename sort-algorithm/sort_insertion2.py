n = int(input()) # 원소의 개수: n개
arr = list(map(int, input().split()))

# i : 정렬된 위치 찾고자 하는 특정 원소의 index
for i in range(1, n):
    
    # j : i번째 원소의 바로 앞 원소부터 제일 첫 번째 원소까지 조회하기 위한 변수
    # 이때, i값이 변하기 전 제일 초기 arr[i]의 값과 arr[j]를 비교
    # 만약 arr[j]가 arr[i] 보다 클 경우 두 숫자 swap하고, i 한칸 앞으로 이동
    for j in range(i - 1, -1, -1):

        if arr[j] > arr[i]: # 오름차순이 아닌 경우
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1 # i를 j 위치로 설정하기 위해 -1

# 삽입 정렬된 배열 출력
for elem in arr:
    print(elem, end=' ')