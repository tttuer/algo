import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = defaultdict(str)
d = defaultdict(int)

q = []
for _ in range(n):
    name,score = map(str, input().split(' '))
    score = int(score)
    
    d[name] += score
    if d[name] not in a:
        a[d[name]] = name
    
    q.append((name,score))

result = max(d.values())

result_name = ''
c = defaultdict(int)
for name,score in q:
    c[name] += score
    if c[name] >= result and d[name] == result:
        result_name = name
        break

print(result_name)
