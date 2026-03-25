"""
[Problem: Minimizing Merge Cost]

You are given N piles of cards, where the i-th pile has A_i cards.
You need to merge all these piles into a single pile.

To merge any two piles with 'x' cards and 'y' cards, 
it costs exactly (x + y) units of effort.
The two piles then become one pile of (x + y) cards.

Find the MINIMUM total effort required to merge all N piles 
into one.

[Input]
- N: Number of piles (1 <= N <= 10^5)
- A: N integers representing the number of cards in each pile.
  (Assume they are given in one line, separated by commas)

[Output]
- A single integer: the minimum total effort.

[Example]
Input: 
3
10, 20, 40

Output: 
110

[Hint]
1. Every time you merge, which two piles should you pick 
   to keep the current cost as low as possible?
2. Once you merge two piles, the new pile goes back into 
   the 'candidate' list. How can you efficiently find 
   the next smallest piles?
"""

import sys
import heapq

input = sys.stdin.readline

# 여기에 코드를 작성해 보세요!