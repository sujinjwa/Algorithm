n = int(input()) # 입력받을 문자열 내 문자의 개수
word = input() # 입력받을 문자열
length = len(word)

cnt = 0 # 'COW' 순서대로 가능한 가짓수
for i in range(length):
    if word[i] == 'C':
        for j in range(i+1, length):
            if word[j] == 'O':
                for k in range(j+1, length):
                    if word[k] == 'W':
                        cnt += 1

print(cnt)