import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split(' ')))
m = int(input())

prefix = [0] * (n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + costs[i]

order_prefix = [0] * (n+1)
costs.sort()
for i in range(n):
    order_prefix[i+1] = order_prefix[i] + costs[i]

for _ in range(m):
    type,start,end = map(int, input().split(' '))
    
    if type == 1:
        answer = prefix[end] - prefix[start-1]
        print(answer)
    else:
        answer = order_prefix[end] - order_prefix[start-1]
        print(answer)