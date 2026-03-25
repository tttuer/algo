"""
[Step 2-1: GCD Magic]

You are given an array 'A' of N integers. 
You can perform the following operation any number of times:
- Choose any two indices i and j (i != j).
- Replace A[i] with GCD(A[i], A[j]).

What is the MINIMUM possible sum of all elements in the array?

[Example]
Input: 3 / [4, 6, 8]
Output: 6
(Explanation:
1. GCD(4, 6) = 2. Replace 4 with 2. Array: [2, 6, 8]
2. GCD(6, 2) = 2. Replace 6 with 2. Array: [2, 2, 8]
3. GCD(8, 2) = 2. Replace 8 with 2. Array: [2, 2, 2]
Total sum: 2 + 2 + 2 = 6.)

[Hint]
1. If you keep replacing numbers with GCDs, what will ALL numbers 
   eventually become?
2. What is the smallest possible GCD you can get from the entire array?
"""

import sys
import math # math.gcd(a, b)를 사용할 수 있습니다.

input = sys.stdin.readline

# 여기에 코드를 작성해 보세요!
n = int(input().strip())

a = list(map(int, input().strip().split(',')))

smallest_gcd = a[0]

for i in range(1,len(a)):
    g = math.gcd(smallest_gcd, a[i])
    smallest_gcd = min(smallest_gcd, g)
    if smallest_gcd == 1:
        break

smallest_gcd *= n

print(smallest_gcd)