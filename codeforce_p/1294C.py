import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    answer = []
    visited = set()
    while n > 1:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                n = n//i
                answer.append(i)
                visited.add(i)
            if len(answer) == 2 and n not in visited:
                answer.append(n)
                n = n//n
                break
        if len(answer) != 3:
            break
    if len(answer) == 3:
        print('YES')
        print(' '.join(map(str,answer)))
    else:
        print('NO')