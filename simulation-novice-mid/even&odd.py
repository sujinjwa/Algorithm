n = int(input()) # 숫자 개수 : n개
blocks = list(map(int, input().split()))

# 생각해 보면, 그룹의 숫자를 고를 때 어느 숫자를 고르던
# 그 숫자의 홀짝이 같다면 그룹의 총합에서 홀짝도 같아지게 된다
# 따라서 어느 숫자를 골랐는지 알 필요가 없으며,
# 짝수와 홀수 중 어느 숫자를 새로 골랐는지만 정보 가지고 있다면 문제 풀 수 있다
even = 0
odd = 0
for block in blocks:
    if block % 2 == 0:
        even += 1
    else:
        odd += 1

# 그룹을 나눌 때 숫자를 가능한 적게 쓰는 것이 유리하다.
# 숫자를 적게 사용해야 남은 숫자들로 더 많은 그룹을 만들 가능성이 생기기 때문.

# 생각해 보면, 홀수 그룹을 만들 때 짝수 숫자를 그룹에 넣는 것은 의미가 없다
# 짝수 숫자를 넣으나 마나 어차피 그룹의 홀짝성이 변하지 않기 때문.
# 따라서, 홀수 그룹을 만들 때에는 짝수 숫자를 넣지 않고, 홀수 숫자 1개로 그룹 형성하는 게 유리

# 짝수 그룹 만들 때에는 홀수 2개로 만들거나 짝수 1개로 만들 수 있는데,
# 홀수 그룹 만들 때 사용되지 않는 짝수 숫자부터 그룹에 이용하는 게 유리

group_num = 0
while True:
    # 묶음을 짝수, 홀수 번갈아가며 나오게끔 해야 하므로
    # group_num이 짝수일 때, 묶음은 짝수로 만들어야 하고
    # group_num이 홀수일 때, 묶음은 홀수로 만들어야 한다.

    if group_num % 2 == 0:
        # 짝수 묶음 만들 때에는, 짝수 숫자 1개로 그룹 만드는 게 최선
        # 만약 짝수 숫자가 부족하다면, 홀수 숫자 2개로 그룹을 만드는 게 최선
        if even: # 짝수 있다면
            even -= 1
            group_num += 1
        elif odd >= 2: # 홀수 2개 이상 있다면
            odd -= 2
            group_num += 1
        else:
            # 더 이상 그룹을 만드지 못하는 상황

            # 아직 숫자가 남아있다면 남아 있는 숫자들로 짝수 그룹 만들지 못한다
            # 이 경우 .. + (짝수 그룹 A) + (홀수 그룹 B) + (나머지 C (홀수 그룹))
            # 위와 같은 상태인데, 무슨 짓을 해도 그룹의 개수를 늘리거나 유지해서는
            # 문제 조건을 만족할 수 없다

            # 그 이유는 그룹의 개수 늘리려면 ... + 짝수 그룹 + 홀수 그룹 + 짝수 그룹 형태가,
            # 그룹의 개수를 유지하려면 ... + 짝수 그룹 + 홀수 그룹 형태가 되어야만 하는데
            # 홀짝성을 생각해 보았을 때 이는 불가능하다
            # 따라서 그룹의 개수를 1개 줄이는
            # ... + 짝수 그룹 (A + B + C) 형태가 최선이다
            if even > 0 or odd > 0:
                group_num -= 1
            
            break
        
    else:
        # 홀수 묶음을 만들 때에는, 홀수 숫자 1개로 그룹을 만드는 것이 최선이다
        # 짝수 숫자만으로는 홀수 묶음을 만들 수 없다
        if odd:
            odd -= 1
            group_num += 1
        else:
            # 더 이상 그룹을 만들지 못하는 상황이다

            # 아직 숫자가 남아있다면 남아 있는 숫자들로 홀수 그룹 만들지 못한다
            # 이 경우 ... + (홀수 그룹 A) + (짝수 그룹 B) + (나머지 C(짝수 그룹))
            # 다음과 같은 상태인데, 무슨 짓을 해도 그룹의 개수를 늘리는 방식으로는
            # 문제 조건을 만족할 수 없다

            # 그 이유는 그룹의 개수를 늘리려면 ... + 홀수 그룹 + 짝수 그룹 + 홀수 그룹 형태가
            # 되어야만 하는데 홀짝성을 생각해 보았을 때 이는 불가능하다
            # 따라서 그룹의 개수를 유지하는
            # ... + (홀수 그룹 A)+ (짝수 그룹 (B + C)) 형태가 최선이다
            break

print(group_num)