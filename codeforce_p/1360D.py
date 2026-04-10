import sys
import math
input = sys.stdin.readline

t = int(input())

answers = []

for _ in range(t):
    n,k = map(int, input().split(' '))

    MAX = int(math.sqrt(n)+1)+1
    shovels = []
    for i in range(1,MAX):
        if n % i == 0:
            if i <= k:
                shovels.append(i)
                if i**2 != n:
                    if n//i <= k:
                        shovels.append(n//i)
    
    shovels.sort()
    
    answers.append(n//shovels[-1])

print('\n'.join(map(str, answers)))