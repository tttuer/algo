import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,x = map(int, input().split(' '))
    elems = list(map(int, input().split(' ')))

    ms = [elem%2 for elem in elems]

    counts = Counter(ms)

    possible = False

    for i in range(1,counts[1]+1):
        if i <= x:
            if i%2 == 1 and counts[0] >= x-i:
                possible = True
                break
    
    print('Yes' if possible else 'No')
