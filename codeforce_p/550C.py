import sys
input = sys.stdin.readline

n = input().strip()

def check(n):
    limit = len(n)
    for i in range(0,limit):
        if int(n[i])%8==0:
            return (True,n[i])
        for j in range(i+1,limit):
            now = n[i]+n[j]
            inow = int(now)
            if inow%8==0:
                return (True,now)
            for k in range(j+1,limit):
                now = n[i]+n[j]+n[k]
                inow = int(now)
                if inow%8 == 0:
                    return (True,now)
                
    return (False,0)

result = check(n)
if result[0]:
    print('YES')
    print(result[1])
else:
    print('NO')