import sys
input = sys.stdin.readline

limit = 10**5
t,k = map(int, input().split(' '))
ways = [0]*(limit+1)
prefix_sum = [0]*(limit+1)

ways[0] = 1
MOD = 10**9+7

for i in range(1,limit+1):
    ways[i] = ways[i-k]+ways[i-1] if i >= k else ways[i-1]
    ways[i] %= MOD

for i in range(1,limit+1):
    prefix_sum[i] = prefix_sum[i-1] + ways[i]
    prefix_sum[i] %= MOD

answers=[]
for _ in range(t):
    a,b = map(int, input().split(' '))

    answer = prefix_sum[b] - prefix_sum[a-1]
    answer %= MOD
    answers.append(answer)
    
print('\n'.join(map(str, answers)))