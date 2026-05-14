import sys
input = sys.stdin.readline

LIMIT = 2*10**5
primes = []
check = [False] + [False] + [True]*LIMIT

for i in range(2, LIMIT):
    if check[i]:
        primes.append(i)
    for j in range(i*i, LIMIT, i):
        check[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    answer = []
    for i in range(n):
        answer.append(primes[i]*primes[i+1])
    
    print(*answer)