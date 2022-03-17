A = input()

def is_palindrome(string):
    for i in range(len(A)//2):
        if A[i] != A[-1-i]:
            return False
    return True

if is_palindrome(A):
    print('Yes')
else:
    print('No')