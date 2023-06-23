# 내 답안, 시간초과 남, O(N^3)
def solution(id_list, report, k):
    dict = []
    
    for id in id_list:
        dict.append({'id': id, 'report': [], 'stopped': []})
        
    for elem in report:
        name1, name2 = elem.split(' ')
        
        for i in range(len(dict)):
            # 동일한 유저에 대한 신고횟수는 1회로 처리
            if dict[i]['id'] == name1 and name2 not in dict[i]['report']:
                dict[i]['report'].append(name2)
    
    count = []
    # report 조회하면서 k번 이상 신고 당한 경우 stopped에 추가
    for name in id_list:
        cnt = 0
        for i in range(len(dict)):
            if name in dict[i]['report']:
                cnt += 1
        
        count.append({'name': name, 'cnt': cnt})
    
    # report 조회하면서 count 내에 k번 이상인 있는 사람이 report 내부에 있다면
    # stopped에다가 그 사람 추가하기
    for i in range(len(dict)):
        for person in dict[i]['report']:
            for j in range(len(count)):
                if count[j]['name'] == person and count[j]['cnt'] >= k:
                    dict[i]['stopped'].append(person)
    
    answer = []
    for i in range(len(dict)):
        answer.append(len(dict[i]['stopped']))
    return answer


# 다른 사람 답안, O(N)
def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    print(answer)

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)