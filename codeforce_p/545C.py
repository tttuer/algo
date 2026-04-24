import sys
input = sys.stdin.readline

n = int(input())
xh = []
for _ in range(n):
    x,h = map(int, input().split(' '))
    xh.append((x,h))

xhl = [(x-h,x) for x,h in xh]
xhr = [(x,x+h) for x,h in xh]

se = [(xhl[0][0],xhl[0][1])]
answer = 1

for i in range(1,n):
    now = se.pop()
    if xhl[i][0] > now[1]:
        answer += 1
        se.append(xhl[i])
    elif xhr[i][0] > now[1]:
        if i+1 < n and xh[i+1][0] > xhr[i][1]:
            answer += 1
            se.append(xhr[i])
        elif i+1 == n:
            answer += 1
        else:
            se.append((xh[i][0],xh[i][0]))
    else:
        se.append((xh[i][0],xh[i][0]))

print(answer)
