# 의상 
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 틀린 코드
def solution(clothes):
    dict = {}
    for c in clothes:
        name, type = c[0], c[1]
        
        if type in dict:
            dict[type].append(name)
        else:
            dict[type] = [name]
    
    arr = [
        [] for _ in range(len(dict))
    ]
    
    index = 0
    for d in dict:
        arr[index] = dict[d]
        index += 1
    
    answer = 0
    # i = 시작점
    for i in range(len(arr)):
        temp = len(arr[i])
        answer += temp
        if i != len(arr)-1:
            # j = 끝 점(계산 길이, 1,2,3,4,...len(arr) 로 늘어나야 함)
            for j in range(i+1, len(arr)):
                temp *= len(arr[j])
                answer += temp         
    
    return answer


# 정답 코드
def solution2(clothes):
    dict2 = {}
    
    for _, type in clothes:
        if type in dict2:
            dict2[type] += 1
        else:
            dict2[type] = 2
            # 모든 경우의 수 구할 때 type별로 있는 수의 n + 1를 곱해줘야 하므로
            # 해당 type에 해당하는 의상이 1개인 경우
            # 의상을 입었을 때와 안 입었을 때 2가지 경우를 모두 고려하기 위해 
            # 1이 아닌 2로 초기화
            
    cnt = 1
    for num in dict2.values():
        cnt *= num
    
    return cnt - 1 # 의상을 한 개도 입지 않은 경우 1가지 빼줘야 함