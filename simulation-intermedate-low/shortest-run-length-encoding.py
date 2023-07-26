# Time Complexity : O(N^2)
# Memory Complexity : O(N)

import sys
from collections import deque
INT_MAX = sys.maxsize

a = input()
a = deque(a)

answer = INT_MAX
# len(a)번에 걸쳐 오른쪽으로 문자열 하나씩 shift한 후
# shift된 문자열의 run-length 인코딩 길이 구하면서 최소값 갱신
for _ in range(len(a)):
    last = a.pop()
    a.appendleft(last)
    
    encoded = ''
    cnt = 1

    # 주어진 문자열의 길이가 1인 경우 언제나 run-length 인코딩 길이는 2
    if len(a) == 1:
        answer = 2
        break

    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            cnt += 1
            if i == len(a) - 2: # 마지막 두개 요소가 같은 경우
                encoded += a[i]
                encoded += str(cnt)
        else:
            encoded += a[i]
            encoded += str(cnt)
            cnt = 1
            if i + 1 == len(a) - 1: # 마지막 인덱스 경우
                encoded += a[i + 1]
                encoded += str(cnt)

    # 저장하고 있는 최소 값(answer)보다 작다면 최소값 갱신
    answer = min(answer, len(encoded))

print(answer)