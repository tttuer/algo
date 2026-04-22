import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
c = [a[i]-b[i] for i in range(n)]

c.sort()

answer = 0
for i in range(n):
    idx = bisect_right(c, -c[i])
    if idx != -1:
        answer += min(n-i-1,(n-idx))

print(answer)