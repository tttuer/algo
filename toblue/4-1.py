"""
[Problem: Target Sum Subarray]

Given an array 'A' of N positive integers, find the number of 
continuous subarrays whose sum is exactly equal to 'S'.

[Constraints]
- 1 <= N <= 10^5
- 1 <= S <= 10^9
- 1 <= A_i <= 10^4 (All elements are positive)

[Example]
Input: 
N=5, S=5
A = [1, 2, 3, 4, 5]

Output: 
2
(Explanation: The subarrays are [2, 3] and [5])

[Hint for Expert Level]
- Use two pointers (left and right).
- Expand 'right' when the sum is too small.
- Shrink 'left' when the sum is too large or equal to S.
- This approach works in O(N) time.
"""

import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    s = int(input().strip())
    a = list(map(int, input().strip().split(',')))

    l,r = 0,0
    prefix_sum = a[0]
    count = 0

    while r < n:
        if r < l:
            r += 1
            if r < n:
                prefix_sum += a[r]
        if prefix_sum <= s:
            if prefix_sum == s:
                count += 1
            r += 1
            if r < n:
                prefix_sum += a[r]
        
        if prefix_sum > s:
            prefix_sum -= a[l]
            l += 1
    return count

print(solve())
