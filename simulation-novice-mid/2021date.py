M, D = tuple(map(int, input().split()))

def Feb(D):
    if D > 28:
        return False
    return True

def thirty(D):
    if D > 30:
        return False
    return True

def thirty_one(D):
    if D > 31:
        return False
    return True

def exist(M, D):
    if M <= 8 and M >= 1:
        if M == 2:
            #2월, 28일
            return Feb(D)

        elif M == 8:
            # 8월, 31일
            return thirty_one(D)

        elif M % 2 == 0 and M != 2 and M != 8:
            # 30일
            return thirty(D)

        elif M % 2 == 1:
            # 31일
            return thirty_one(D)
    elif M <= 12 and M >= 8:
        if M % 2 == 1:
            #9, 11월
            return thirty(D)

        elif M % 2 == 0:
            #10, 12월
            return thirty_one(D)

if exist(M, D):
    print("Yes")
else:
    print("No")