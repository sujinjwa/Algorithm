n = int(input())
 
for num in range(1, n + 1):
    tmp = str(num)
    cnt = 0
     
    for s in tmp:
        if s == '3' or s == '6' or s == '9':
            cnt += 1
     
    if cnt >= 1:
        for _ in range(cnt):
            print('-', end='')
        print(' ', end='')
        continue
         
    print(str(num), end = ' ')