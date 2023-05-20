import sys

n, m, p = tuple(map(int, input().split()))
message = [
    list(input().split())
    for _ in range(m)
]

# 모두 읽은 채팅이라면 읽지 않은 사람 없다
if int(message[p - 1][1]) == 0:
    sys.exit()

# 각 사람에 대해 채팅 읽었는지, 안 읽었는지 확인
for i in range(n):
    # read : 확실하게 채팅 읽었으면 true
    person = chr(ord('A') + i)
    read = False

    # 만약 p번 메시지를 읽은 사람 수와 같은 채팅을 기준으로
    # 한번이라도 채팅을 쳤다면 확실하게 채팅 읽었다
    for c, u in message:
        u = int(u)
        if u >= int(message[p - 1][1]) and c == person:
            read = True
        
    if read == False:
        print(person, end=" ")