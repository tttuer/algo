import sys
input = sys.stdin.readline

n = int(input())
h1 = list(map(int, input().split(' ')))
h2 = list(map(int, input().split(' ')))

dp = [[0]*2 for _ in range(n)]
dp[0][0] = h1[0]
dp[0][1] = h2[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][1]+h1[i],dp[i-1][0])
    dp[i][1] = max(dp[i-1][0]+h2[i],dp[i-1][1])
    
print(max(dp[n-1]))