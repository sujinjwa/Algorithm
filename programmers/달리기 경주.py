# 달리기 경주 - level 1
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 내 답안 O(N^2)
def solution(players, callings):
    for c in callings:
        for p in range(len(players)):
            if players[p] == c:
                players[p-1], players[p] = players[p], players[p-1]
    
    answer = players
    return answer

# 다른 사람 답안 O(N)
# 딕셔너리 공부해야겠다
def solution2(players, callings):
    p_dic = {player: index for index, player in enumerate(players)}

    for p in callings:
        c = p_dic[p]

        p_dic[p] -= 1
        p_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]
    
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))