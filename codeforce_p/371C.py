import sys
from collections import defaultdict
input = sys.stdin.readline

recipe = input().strip()
bsc = list(map(int, input().split(' ')))
rbsc = list(map(int, input().split(' ')))
r = int(input())

left = 0
right = 10**14

count = defaultdict(int)
for e in recipe:
    count[e] += 1

def is_possible(n):
    nb = n*count['B']
    ns = n*count['S']
    nc = n*count['C']

    money = 0

    if nb > bsc[0]:
        money += (nb-bsc[0])*rbsc[0]
    if ns > bsc[1]:
        money += (ns-bsc[1])*rbsc[1]
    if nc > bsc[2]:
        money += (nc-bsc[2])*rbsc[2]
    
    return r >= money

answer = 0
while left <= right:
    mid = (left+right)//2

    if is_possible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)