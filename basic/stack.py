# 올바른 괄호 문자열 예: ((()))((()))
# 올바르지 않은 괄호 문자열 예: ((())))(())(

stack = [] #주어진 문자열이 올바른 괄호 문자열인지 확인하기 위한 스택 배열
string = "((()))()()(())"; # 주어진 문자열

for i in range(len(string)): # 주어진 문자열 순회
    if string[i] == '(': # 열린 괄호인 경우 stack 배열에 추가
        stack.append('(')
    else: # 닫힌 괄호 나온 경우
        if stack == []: # stack이 비어있다면 올바른 괄호 문자열 아님
            print('false')
            exit()
        stack.pop() # stack이 비어있지 않은 경우 가장 위에 있는 값 지워줌

if stack != []: # 주어진 문자열 전부 순회한 후 stack이 비어있지 않다면 올바른 문자열 아님
    print('false')
else:
    print('true')
        