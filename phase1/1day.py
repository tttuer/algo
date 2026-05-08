import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
print(*arr)
print('\n'.join(map(str, arr)))

a,b = b,a
arr[i], arr[j] = arr[j], arr[i]

new = arr[:]
new = list(arr)

grid = [[0]*m for _ in range(n)]

from itertools import accumulate
prefix_max = list(accumulate(arr, max))
prefix_sum = list(accumulate(arr))

from collections import Counter, defaultdict
cnt = Counter(arr)
graph = defaultdict(list)
graph[u].append(v)

arr.sort(key=lambda x: (x[0], -x[1]))

if all(x > 0 for x in arr):
if any(x == target for x in arr):

import heapq
heap = []
heapq.heappush(heap,x)
now = heapq.heappop(heap)

from bisect import bisect_left, bisect_right

