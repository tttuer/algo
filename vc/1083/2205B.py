import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    s = set()
    
    d = 2
    while d*d <= n:
        while n%d == 0:
            n//=d
            s.add(d)
        d += 1
    
    if n != 1:
        s.add(n)
    answer = 1
    
    for v in s:
        answer *= v
        
    print(answer)