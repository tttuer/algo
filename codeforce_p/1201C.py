import sys
from bisect import bisect_right
input = sys.stdin.readline

n,k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

a.sort()

mid = n//2

a_diff = []

for i in range(n):
    a_diff.append(a[i]-a[mid])

prefix_sum = [0]*n

for i in range(mid+1,n):
    prefix_sum[i] = prefix_sum[i-1]+a_diff[i]

end = bisect_right(prefix_sum, k)
answer = a[mid]

answer = a[end-1]
k -= prefix_sum[end-1]
answer += k//(end-mid)

print(answer)
