import sys
input = sys.stdin.readline

MAX = 1000
x1,y1,x2,y2 = map(int, input().split(' '))
x3,y3,x4,y4 = 1001,1001,1001,1001

if x1==x2:
    diff = abs(y1-y2)
    x3 = x1+diff if x1+diff <= MAX else x1-diff
    y3 = y1
    x4 = x2+diff if x2+diff <= MAX else x2-diff
    y4 = y2
elif y1==y2:
    diff = abs(x1-x2)
    x3 = x1
    y3 = y1+diff if y1+diff <= MAX else y1-diff
    x4 = x2
    y4 = y2+diff if y2+diff <= MAX else y2-diff
else:
    x_diff,y_diff = abs(x1-x2),abs(y1-y2)
    if x_diff == y_diff:
        x3 = x2
        y3 = y1
        x4 = x1
        y4 = y2

if x3 <= -1001 or x3 >= 1001 or x4 <= -1001 or x4 >= 1001:
    print(-1)
else:
    print(x3,y3,x4,y4, sep=' ')
