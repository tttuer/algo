import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split(' '))
cats = list(map(int, input().split(' ')))

graph = [[] for _ in range(n)]

for _ in range(n-1):
    x,y = map(int, input().split(' '))
    x-=1
    y-=1
    
    graph[x].append(y)
    graph[y].append(x)
    
q = deque()
q.append((0,-1,cats[0]))

answer = 0

while q:
    now, parent, consecutive = q.popleft()
    
    if consecutive > m:
        continue
    
    children = [i for i in graph[now] if i != parent]
    
    if len(children) == 0:
        answer += 1
        
    for child in children:
        n_consecutive = consecutive + 1 if cats[child] == 1 else 0
        q.append((child, now, n_consecutive))

print(answer)