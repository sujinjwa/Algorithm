# word : 소문자 알파벳으로 이루어진 문자열 1개
word = input()

count = {}

# 각 알파벳(key) 문자열에 포함된 횟수 value로 저장
for alpha in word:
    if alpha in count:
        count[alpha] += 1
    else:
        count[alpha] = 1

has = False # 문자열에 단 한개만 포함된 문자 존재 여부
for alpha in count:
    if count[alpha] == 1:
        has = True
        print(alpha) # 해당 문자 출력
        break # 먼저 등장한 문자만 출력

# 문자가 없다면
if not has:
    print('None')