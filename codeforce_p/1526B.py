import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = int(input())

    result = False
    for i in range(11):
        if x - 111*i >= 0 and (x-111*i)%11==0:
            result = True
            break
    
    if result:
        print('YES')
    else:
        print('NO')
    
