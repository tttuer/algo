"""
[Problem: Minimizing the sum]

You have an array 'A' of N integers. 
In one move, you can choose any element A_i and replace it 
with the value of one of its neighbors (A_i-1 or A_i+1). 

You can perform at most 'K' moves. 
Your goal is to make the SUM of all elements in the array 
as SMALL as possible.

[Input]
- First line: N and K (1 ≤ N ≤ 10^5, 0 ≤ K ≤ 10)
- Second line: N integers representing array A (1 ≤ A_i ≤ 10^9)

[Output]
- The minimum possible sum of elements after at most K moves.

[Example]
Input: 5, 1
10, 20, 30, 40, 50
Output: 130
(Hint: Replace 20 with 10. The array becomes 10, 10, 30, 40, 50. 
Sum = 150 -> 140... Wait, what if we replace 50 with 40? 
Try to find the biggest drop!)
"""

import sys
input = sys.stdin.readline

n,k = map(int, input().strip().split(','))
a = list(map(int, input().strip().split(',')))

dp = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        dp[i][j] = dp[i-j][j]