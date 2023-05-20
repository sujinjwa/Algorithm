people = ''
cnt = [0] * 4

for _ in range(3):
    answer = tuple(input().split())
    symptom = answer[0]
    degree = int(answer[1])

    if symptom == 'Y':
        if degree >= 37:
            people += 'A'
        else:
            people += 'C'
    else:
        if degree >= 37:
            people += 'B'
        else:
            people += 'D'


for person in people:
    if person == 'A':
        cnt[0] += 1
    elif person == 'B':
        cnt[1] += 1
    elif person == 'C':
        cnt[2] += 1
    else:
        cnt[3] += 1

for elem in cnt:
    print(elem, end=' ')
if cnt[0] >= 2:
    print('E')