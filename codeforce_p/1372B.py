import sys
import math
input = sys.stdin.readline

t = int(input())
MAX = int(math.sqrt(10**9)+1)
prime = [True]*(MAX+1)
prime[0] = prime[1] = False
for i in range(2,MAX):
    if not prime[i]:
        continue
    for j in range(i*i, MAX, i):
        prime[j] = False

def is_prime(n):
    if n <= MAX and prime[n]:
        return True
    for i in range(2,MAX):
        if prime[i] and n%i==0:
            return False
    return True
            

for _ in range(t):
    n = int(input())

    if is_prime(n):
        print(1, n-1, sep=' ')
    elif n%2==0:
        print(n//2,n//2,sep=' ')
    else:
        answer = 1
        nn = n
        for i in range(2,MAX):
            if prime[i] and n%i==0:
                answer = i
                break
        
        answer = n//i

        print(answer, n-answer, sep=' ')