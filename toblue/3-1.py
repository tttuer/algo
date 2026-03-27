"""
[Step 3-1: The Static Range Sum]

You are given an array 'A' of N integers. 
You need to answer 'Q' queries. Each query consists of two indices L and R.
For each query, calculate the sum of elements from A[L] to A[R] (inclusive).

[Constraints]
- N = 10^5, Q = 10^5
- Array elements A_i <= 10^9

[Example]
Input: 
A = [10, 20, 30, 40, 50]
Query 1: L=1, R=3 (indices start from 0)
Output: 20+30+40 = 90

[The Challenge]
If you use a loop for each query, the time complexity will be O(N * Q).
With N, Q = 10^5, this is 10^10 operations (Time Limit Exceeded!). 
Can you pre-calculate something so each query takes O(1) time?
"""

import sys
input = sys.stdin.readline

# 여기에 코드를 작성해 보세요!
n = int(input().strip())
a = list(map(int, input().strip().split(',')))
left, right = map(int, input().strip().split(','))

sum_list = [0] * (n+1)

for i in range(n):
    sum_list[i+1] = sum_list[i] + a[i]

answer = sum_list[right + 1] - sum_list[left]

print(answer)