# n : 방에 있는 사람 수, m : 메세지 정보의 수, p : 확인 필요한 메세지 번호
n, m, p = tuple(map(int, input().split()))

info = [
    list(input().split()) # c : 메시지 작성한 사람, u : 읽지 않은 사람 수
    for _ in range(m)
]

# 가능한 프로그래머의 모든 이름
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

people = []
for i in range(n): # 채팅방에 있는 n명의 모든 사람들의 이름 people 배열에 저장
    people.append(alpha[i])

person = info[p - 1][0] # f번째 메시지 작성한 사람
undefined = info[p - 1][1] # f번째 메시지 읽지 않은 사람 수

for message in info:
    # f번째 메시지 이후에 메시지 보낸 사람이 있는 경우
    # 그 사람들은 f번째 메세지를 정확히 읽은 것이므로
    # 읽었다는 표시를 '0'으로 표기
    for i in range(n):
        if int(message[1]) >= int(undefined) and message[0] == people[i]:
            people[i] = '0'

for elem in people:
    if undefined == '0': # 메시지 모두 읽은 경우
        break

    if elem != '0': # 메시지 안 읽은 가능성 있는 사람인 경우
        print(elem, end=' ')