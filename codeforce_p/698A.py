import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))

dp = [[0]*3 for _ in range(n+1)]
if a[0] == 1:
    dp[0][1] = 1
elif a[0] == 2:
    dp[0][2] = 1
elif a[0] == 3:
    dp[0][1] = 1
    dp[0][2] = 1

for i in range(1,n):
    dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    if a[i] == 1:
        dp[i][1] = max(dp[i-1][0]+1,dp[i-1][2]+1)
    elif a[i] == 2:
        dp[i][2] = max(dp[i-1][0]+1,dp[i-1][1]+1)
    elif a[i] == 3:
        dp[i][1] = max(dp[i-1][0]+1,dp[i-1][2]+1)
        dp[i][2] = max(dp[i-1][0]+1,dp[i-1][1]+1)

answer = max(dp[n-1])
print(n-answer)