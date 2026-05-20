import sys
from collections import deque
import heapq
input = sys.stdin.readline

t = int(input())
answers = []
for _ in range(t):
    n,k,p,m = map(int, input().split())
    alist = list(map(int,input().split()))
    
    a = deque()
    target = ()
    for i in range(n):
        now = (alist[i],i)
        if i == p-1:
            target = (alist[i],i)
        a.append(now)

    cost = 0
    kq = []
    for i in range(k):
        now = a.popleft()
        kq.append(now)

    heapq.heapify(kq)
    answer = 0
    while True:
        now = ()
        if target in kq:
            now = target
            kq.remove(now)
            heapq.heapify(kq)
        else:
            now = heapq.heappop(kq)
        cost += now[0]
        if cost > m:
            break

        if now[1] == p-1:
            answer += 1

        a.append(now)
        heapq.heappush(kq, a.popleft())

    answers.append(answer)

print('\n'.join(map(str, answers)))     