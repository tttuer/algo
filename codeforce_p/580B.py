import sys
input = sys.stdin.readline

n,d = map(int, input().split(' '))
ms = []
for _ in range(n):
    m,s = map(int,input().split(' '))
    ms.append((m,s))

ms.sort()

answer = 0
left = 0
right = 0
cur = 0
for left in range(n):
    while right < n:
        if ms[right][0]-ms[left][0] >= d:
            break
        cur += ms[right][1]
        right += 1
    answer = max(answer, cur)
    cur -= ms[left][1]

print(answer)