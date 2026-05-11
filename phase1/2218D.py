import sys
import math
input = sys.stdin.readline

LIMIT = 10**6
a = [False, False] + [True]*(LIMIT-1)
prime = []

for i in range(2, LIMIT):
    if a[i]:
        prime.append(i)
        for j in range(i*i, LIMIT, i):
            a[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    answer = [prime[0]]

    for i in range(1,n):
        answer.append(prime[i-1]*prime[i])
    
    print(*answer)