import sys
from bisect import bisect_right
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,q = map(int, input().split(' '))
    steps = list(map(int, input().split(' ')))
    qs = list(map(int, input().split(' ')))

    a_max = [0]*(n+1)
    for i in range(n):
        a_max[i+1] = max(steps[i],a_max[i])
    prefix_sum = [0] *(n+1)
    for i in range(n):
        prefix_sum[i+1] = steps[i]+prefix_sum[i]
    
    answer = []
    for q in qs:
        i = bisect_right(a_max, q)
        answer.append(prefix_sum[i-1])
    
    print(' '.join(map(str, answer)))