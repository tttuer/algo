import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,y,x = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(v//y*x for v in a)
    
    result = 0
    for i in range(n):
        candidate = a[i] + total - a[i]//y*x
        result = max(result, candidate)
        
    print(result)