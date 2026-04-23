import sys
from bisect import bisect_right
input = sys.stdin.readline

n,k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

a.sort()

mid = n//2

left = a[mid]
right = a[mid]+k
answer = left

while left <= right:
    m = (left+right)//2

    cost = 0
    for i in range(mid, n):
        if a[i] < m:
            cost += m-a[i]
    
    if cost <= k:
        answer = m
        left = m+1
    else:
        right = m-1

print(answer)