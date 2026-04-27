import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))

if sum(a)%3 != 0:
    print(0)
else:
    t = sum(a)//3
    cnt = [0]*n
    sum = 0
    for i in range(n-1,0,-1):
        sum += a[i]
        if sum == t:
            cnt[i] = 1
    
    prefix_sum = [0]*(n+1)
    for i in range(n-1,0,-1):
        prefix_sum[i] = prefix_sum[i+1]+cnt[i]

    sum = 0
    answer = 0
    for i in range(n):
        sum += a[i]
        if t == sum and i+2 < n:
            answer += prefix_sum[i+2]
    
    print(answer)