"""
[Step 2-2: The Divisor Challenge]

You are given an integer N. 
A "Perfect Number" in this problem is a number that has 
EXACTLY 3 divisors (약수). 

For example:
- 4 has divisors {1, 2, 4} -> Perfect!
- 9 has divisors {1, 3, 9} -> Perfect!
- 6 has divisors {1, 2, 3, 6} -> Not Perfect (4 divisors).

Given N, count how many "Perfect Numbers" exist between 1 and N.

[Constraints]
- 1 <= N <= 10^12 (N이 매우 큽니다!)

[Hint]
1. Which numbers have exactly 3 divisors? 
   (Think about prime numbers and their squares!)
2. If N = 10^12, you cannot check every number from 1 to N. 
   What is the maximum possible value of the square root of N?
"""

import sys
import math
input = sys.stdin.readline

n = int(input().strip())
limit = int(math.sqrt(n)) + 1

primes = [False, False] + [True] * limit

for i in range(2, limit):
    if primes[i]:
        for j in range(i*i, limit, i):
            primes[j] = False

answer = 0
for i in range(2, limit):
    if primes[i]:
        answer += 1

print(answer)