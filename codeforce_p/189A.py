import sys
input = sys.stdin.readline

n,a,b,c = map(int, input().split(' '))

MIN = -1
dp = [MIN] * (n+1)
dp[0] = 0

for i in range(n):
    for j in (a,b,c):
        if i+j <= n and dp[i] != MIN:
            dp[i+j] = max(dp[i+j], dp[i] + 1)

print(dp[n])