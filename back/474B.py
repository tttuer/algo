import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

prefix_sum = [0]*(n+1)

for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1]+a[i-1]

for v in q:
    print(bisect_left(prefix_sum, v))