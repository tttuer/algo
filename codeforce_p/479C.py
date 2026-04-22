import sys
input = sys.stdin.readline

n = int(input())
abs = []
for i in range(n):
    a,b = map(int, input().split(' '))
    abs.append((a,b))

abs.sort(key=lambda x: (x[0],x[1]))

now = min(abs[0][0],abs[0][1])

for i in range(1,n):
    a,b = abs[i][0],abs[i][1]
    na=nb=10**9+1
    if now <= a:
        na=a
    if now <= b:
        nb=b
    
    now = min(na,nb)
    

print(now)