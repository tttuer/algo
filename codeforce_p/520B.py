import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split(' '))

MAX = 100000
visited = [0] * (MAX)

q = deque()
q.append(n)

while q:
    now = deque.popleft(q)

    if now == m:
        break

    next_red = now*2
    next_blue = now-1

    if next_red <= 20000 and visited[next_red] == 0:
        visited[next_red] = visited[now] + 1
        deque.append(q, next_red)
    if next_blue >= 0 and visited[next_blue] == 0:
        visited[next_blue] = visited[now]+1
        deque.append(q, next_blue)
    
print(visited[m])