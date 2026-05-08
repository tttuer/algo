import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
q.append(0)

for _ in range(n):
    a = int(input())
    l = len(q)
    for _ in range(l):
        now = q.popleft()
        q.append(now+a)
        q.append(now-a)

if any(abs(x)%360 == 0 for x in q):
    print('YES')
else:
    print('NO')