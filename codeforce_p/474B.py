import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().strip())
bugs = list(map(int, input().split(' ')))
m = int(input().strip())
fat_bugs = list(map(int, input().split(' ')))

prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + bugs[i]

for b in fat_bugs:
    print(bisect_left(prefix_sum, b))
