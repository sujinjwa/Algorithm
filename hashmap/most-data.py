# n : 문자열의 개수
n = int(input())

nums_of_words = {}

# n번에 걸쳐 단어 입력받기
for _ in range(n):
    word = input()

    if word not in nums_of_words:
        nums_of_words[word] = 1
    else:
        nums_of_words[word] += 1

# 최대로 등장한 단어의 등장 횟수 출력
max_num = 0
for word in nums_of_words:
    max_num = max(max_num, nums_of_words[word])

print(max_num)