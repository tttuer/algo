import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    answer = 0
    for i in range(n):
        for j in range(i+1,n):
            answer = max(answer,a[i]^a[j])
    
    print(answer)