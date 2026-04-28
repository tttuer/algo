import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()

    prefix_sum = [0]*(n+1)

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i]+int(a[i])

    d={}

    for i in range(n+1):
        diff = prefix_sum[i]-i
        if diff in d:
            d[diff] += 1
        else:
            d[diff] = 1

    answer = 0
    for i in d:
        answer += d[i]*(d[i]-1)//2

    print(answer)