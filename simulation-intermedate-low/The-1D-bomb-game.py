# 코드트리 > intermediate-low > 시뮬레이션 > 1차원 폭발 게임
# 문제 링크: https://www.codetree.ai/missions/2/problems/The-1D-bomb-game?utm_source=clipboard&utm_medium=text

# 시간 복잡도 : O(N^2)
# 공간 복잡도 : O(N)


# n : 폭탄의 총 개수, m : 연속되는 숫자의 개수
n, m = tuple(map(int, input().split()))

bombs = [
    int(input())
    for _ in range(n)
]

# m개 이상 연속되는 폭탄들을 0으로 초기화하는 함수
def pop_up():
    global bombs

    for i in range(len(bombs)):
        cnt = 0 # cnt : m개 이상 연속으로 같은 숫자 있는지 확인하기 위한 변수
        # m개 이상 연속으로 같은 숫자 적힌 구간 구하기
        for j in range(i, len(bombs)):
            if bombs[i] != bombs[j]:
                break
            cnt += 1
        
        if cnt >= m: # m개 이상 연속으로 같은 숫자 적힌 구간(i부터 j까지)인 경우
            for k in range(i, i + cnt):
                bombs[k] = 0 # 폭탄 터진 칸 0으로 초기화

# 0으로 초기화된 칸들을 제외하여 새로운 폭탄 배열을 만드는 함수
def fall_down():
    global bombs

    result = []
    for bomb in bombs:
        if bomb != 0:
            result.append(bomb)
    
    return result

# m개 이상 같은 숫자가 연속되는 폭탄들이 있는지 여부 확인하는 함수
def has_m_bombs():
    global bombs

    for i in range(len(bombs)):
        cnt = 0
        for j in range(i, len(bombs)):
            if bombs[i] != bombs[j]:
                break
            cnt += 1
        
        if cnt >= m:
            return True
        
    return False

# m개 이상 같은 숫자가 연속되는 폭탄들이 없을 때까지 시뮬레이션 반복하는 함수
def simulate():
    global bombs

    while True:
        # m개 이상 동일한 숫자를 연속해서 갖는 구간이 존재하지 않다면 반복문 종료
        if not has_m_bombs():
            return bombs

        # m개 이상 동일한 숫자를 가지는 폭탄들 터뜨리기
        pop_up()

        # 폭탄 터진 후 자리 정렬하여 새로운 bombs로 만들기
        bombs = fall_down()


result = simulate()

# 출력
# 최종적으로 남은 폭탄의 개수와
# 위에서 아래 방향으로 각 폭탄에 적힌 숫자 출력
print(len(result))
for r in result:
    print(r)