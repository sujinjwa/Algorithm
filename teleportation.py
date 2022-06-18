A, B, x, y = tuple(map(int, input().split()))

# 방법 3가지
# 1. A -> B : abs(B - A)
dis = abs(B - A)
# 2. A -> x ->(순간이동)-> y -> B
dis_2 = abs(A - x) + abs(y - B)
# 3. A -> y ->(순간이동)-> x -> B
dis_3 = abs(A - y) + abs(x - B)

print(min(dis, dis_2, dis_3))