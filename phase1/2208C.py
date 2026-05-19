import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cps = []
    for i in range(n):
        c,p = map(int,input().split())
        cps.append((c,p))
    
    answer = 0

    for i in range(n-1,-1,-1):
        q = 1-cps[i][1]/100
        answer = max(answer, cps[i][0]+answer*q)
    
    print(answer)