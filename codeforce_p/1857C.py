import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    bs = list(map(int, input().split(' ')))

    bs.sort()

    answer = []

    n -= 1

    i = 0
    while n > 0:
        answer.append(bs[i])
        i += n
        n -= 1
    
    answer.append(bs[-1])                     
    
    print(' '.join(map(str, answer)))