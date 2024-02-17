def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
            continue
        
        if s[i - 1] == ' ':
            answer += s[i].upper()
            continue
        
        if s[i - 1] != ' ' and s[i].isupper():
            answer += s[i].lower()
            continue
        
        answer += s[i]
        
    return answer