n = int(input()) # n : 선분의 개수

# lines = [(1, 2), (3, 4), (5, 6)]
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

lines.sort()

arr = []
ans = 0


def is_overlapped(arr):
    temp = []

    # 선택된(값이 1인) 선분들만 temp 배열에 추가
    for i in range(n):
        if arr[i] == 1:
            temp.append(lines[i])

    # 모든 인접한 두개의 선분이 서로 겹치는지 확인
    for i in range(len(temp) - 1):
        _, e1 = temp[i]
        f2, _ = temp[i + 1]

        if e1 >= f2:
            return [True, 0]
    
    return [False, len(temp)]


# lines에서 curr_num번째 선분 고를지 말지 결정하는 함수
# arr의 curr_num번째 값이 1이면 고른 거, 0이면 안 고른 거
def choose(curr_num):
    global arr, ans

    if curr_num == n:
        # 선분끼리 겹치지 않는 조합일 경우에만 최댓값으로 갱신
        [overlapped, chosen_count] = is_overlapped(arr)
        if not overlapped:
            ans = max(ans, chosen_count)
        
        return

    arr.append(0)
    choose(curr_num + 1)
    arr.pop()

    arr.append(1)
    choose(curr_num + 1)
    arr.pop()


choose(0)


print(ans)