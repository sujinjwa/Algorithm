# 두 문자열 선언 / pattern이 text에 포함되는지 확인
text = input()
pattern = input()

# start_index = text의 모든 인덱스 위치(i)가 차례로 들어감
def is_substr(start_idex):
    n, m = len(text), len(pattern)

    # pattern 길이가 text 길이보다 클 경우
    if start_idex + m -1 >= n:
        return False

    # pattern과 하나라도 다르면 false
    for j in range(m):
        if text[start_idex + j] != pattern[j]:
            return False
    
    # 전부 일치할 경우
    return True

def find_index():
    n = len(text)
    # text의 모든 문자 탐색
    for i in range(n):
        # i번째를 시작으로 부분 문자열이 된다면, 해당 위치 반환 / is_substr 함수는 i번 호출
        if is_substr(i):
            return i
    return -1

print(find_index())