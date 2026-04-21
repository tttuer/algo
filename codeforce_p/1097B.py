import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()

for _ in range(n):
    a = int(input())
    
    nq = []
    if q:
        while q:
            now = q.popleft()
            nq.append(now+a)
            nq.append(now-a)
        q = deque(nq)
    else:
        q.append(a)
        q.append(-a)

result = False
while q:
    now = q.popleft()
    if now == 0 or now%360==0:
        result = True
        break

print('YES' if result else 'NO')