import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    secrests = []
    for _ in range(k):
        s = input().strip()
        secrests.append(s)
    
    l = defaultdict(set)
    
    for i in range(n):
        for j in range(k):
            if secrests[j][i] not in l[i]:
                l[i].add(secrests[j][i])
            
    m = [i for i in range(1,n+1) if n%i==0]
    for d in m:
        pattern = []
        ok = True
        
        for i in range(d):
            common = set(l[i])
            
            for j in range(i, n, d):
                common &= l[j]
                
            if not common:
                ok = False
                break
            
            pattern.append(next(iter(common)))
        
        if ok:
            print(''.join(map(str, pattern))*(n//d))
            break