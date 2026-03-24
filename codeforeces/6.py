"""
[Problem: XOR equals Sum]

You are given two integers N and S. 
Your task is to construct an array 'A' consisting of N non-negative integers 
(A_i >= 0) such that:

1. The sum of all elements is exactly S. 
   (A_1 + A_2 + ... + A_n = S)
2. The bitwise XOR sum of all elements is also exactly S. 
   (A_1 XOR A_2 XOR ... XOR A_n = S)

If such an array exists, print the elements of the array. 
If there are multiple such arrays, any one of them is acceptable.
If it's impossible to construct such an array, print "No".

[Constraints]
- 1 <= N <= 10^5
- 0 <= S <= 10^9

[Example 1]
Input: 3, 10
Output: 10, 0, 0 (10+0+0=10, 10^0^0=10)

[Example 2]
Input: 1, 5
Output: 5 (5=5, 5=5)
"""

import sys
input = sys.stdin.readline

n,s = map(int, input().strip().split(','))

answer = [s] + [0] * (n-1)

print(*answer)