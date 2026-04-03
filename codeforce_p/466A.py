import sys
input = sys.stdin.readline

n,m,a,b = map(int, input().split(' '))

ride_ruble = [[1,a], [m,b]]

MAX = 100000001
dp = [MAX] * (n+m)
dp[0] = 0

for i in range(n):
    for k,v in ride_ruble:
        if i+k < n+m:
            dp[i+k] = min(dp[i+k], dp[i] + v)

answer = MAX

for i in range(n,n+m):
    answer = min(answer, dp[i])

print(answer)
