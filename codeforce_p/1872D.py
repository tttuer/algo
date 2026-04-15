import sys
import math

input = sys.stdin.readline

t = int(input())

answer = []

for _ in range(t):
    n,x,y = map(int, input().split(' '))

    lcm = math.lcm(x,y)
    p = n//x
    m = n//y
    mm = n//lcm
    m -= mm
    
    pp = n*(n+1)//2 - (n-p)*(n-p+1)//2
    mmm = (n-p+mm)*(n-p+mm+1)//2 - (n-p)*(n-p+1)//2 + m*(m+1)//2
    
    answer.append(pp-mmm)

print('\n'.join(map(str, answer)))
    