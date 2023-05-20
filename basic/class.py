# 클래스 선언
class Secret:
    def __init__(self, code, space, time):
        self.code = code
        self.space = space
        self.time = time

code, space, time = tuple(input().split())

# 객체 생성
secret1 = Secret(code, space, int(time))

print('secret code :', secret1.code)
print('meeting point :', secret1.space)
print('time :', secret1.time)