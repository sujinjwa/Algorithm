# n : 단어의 개수
n = int(input())

# words : n개의 단어 입력
# 한 단어에 속한 문자들의 순서를 바꾸어 만들 수 있는 단어들을 '같은 그룹에 속한다'고 정의
words = [
    input()
    for _ in range(n)
]

count = {}
ans = 0

for i in range(len(words)):
    words[i] = str(sorted(words[i])) # 같은 그룹에 속한 단어들을 정렬하면 모두 같아짐
    
    if words[i] in count:
        count[words[i]] += 1
    else:
        count[words[i]] = 1

# 동일한 그룹에 속한 단어가 가장 많은 그룹의 단어 개수 출력
print(max(count.values()))