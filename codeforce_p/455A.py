import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split(' ')))

MAX = max(numbers) + 1
dp = [0] * MAX

score = [0] * MAX

for num in numbers:
    score[num] += num

for i in range(MAX):
    dp[i] = max(dp[i-1], dp[i-2] + score[i])

print(max(dp))