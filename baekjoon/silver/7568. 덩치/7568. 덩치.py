n = int(input()) # n : 전체 사람의 수

people = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 완전탐색으로 풀려면 O(N^2)
# N의 최댓값이 50 이므로 O(N^2) 가능

answer = []

for i in range(len(people)):
    weight_1, height_1 = people[i]
    bigger_people = 1

    for j in range(len(people)):
        if i == j: # 동일한 사람이면 비교 안함
            continue

        weight_2, height_2 = people[j]

        if weight_1 < weight_2 and height_1 < height_2:
            bigger_people += 1
    
    answer.append(bigger_people)

for elem in answer:
    print(elem, end = ' ')