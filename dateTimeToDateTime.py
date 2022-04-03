a, b, c = tuple(map(int, input().split()))
elipsed_time = 0

# 11일 11시 11분
day, hour, mins = 11, 11, 11

while True:
    if day == a and hour == b and mins == c:
        break

    elipsed_time += 1
    mins += 1

    if mins >= 60:
        hour += 1
        mins = 0

    if hour >= 24:
        day += 1
        hour = 0

# 만약 입력받은 시간이 11일 11시 11분보다 앞선 시간이라면
def printPast(a, b, c):
    if a <= 10:
        return True

    if a == 11:
        if b <= 10:
            return True
        if b == 11 and c < 11:
            return True
    return False

if printPast(a, b, c):
    print(-1)
else:
    print(elipsed_time)