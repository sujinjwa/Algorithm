# 고득점 KIT > 완전 탐색 [level1]
# https://school.programmers.co.kr/learn/courses/30/parts/12230


# 어떻게 해야 최소 직사각형의 넓이를 구할 수 있는지를 생각해야 한다

# <최소 직사각형 넓이 구하는 방법>
# 모든 명함들을 조회하면서, 각 명함의 더 긴 모서리 부분을 가로로 돌려서 겹쳐본다
# 긴 모서리 부분들을 하나의 모서리에 포함시키려면 최대 길이값을 가로 길이로 가져야 한다
# 그 상태에서 하나의 지갑에 넣을 수 있으려면 세로 길이는 더 짧은 모서리들 중 최대 길이값을 가져야 한다

def solution(sizes):
    width, height = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        
        width = max(width, w) # width : 각 명함의 더 긴 표면의 길이 중 최댓값
        height = max(height, h) # height : 각 명함의 더 짧은 표면의 길이 중 최댓값

    return width * height