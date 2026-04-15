import sys
from bisect import bisect_right
input = sys.stdin.readline

a,b = map(int, input().split(' '))
a_elems = list(map(int, input().split(' ')))
b_elems = list(map(int, input().split(' ')))

a_elems.sort()

answer = []

for e in b_elems:
    result = bisect_right(a_elems, e)
    
    answer.append(result)
    
print(' '.join(map(str, answer)))