import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n,k = map(int, input().split(' '))
    
    divisor = n - 1
    
    a,b = k // divisor, k % divisor
    
    answer = n * a
    if b == 0:
        answer -= 1
    else:
        answer += b
    
    print(answer)