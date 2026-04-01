import sys
import math
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split(' ')))

MAX = 1000001

p = [True] * MAX
p[1] = False

limit = int(math.sqrt(MAX)) + 1
for i in range(2, limit):
    if p[i]:
        for j in range(i*i, MAX, i):
            p[j] = False
    
for number in numbers:
    s = int(math.sqrt(number))
    if p[s] and s*s == number:
        print('YES')
    else:
        print('NO')