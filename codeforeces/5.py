"""
[Problem: Placing Sensors]

A long straight road has N possible locations where you can place sensors. 
These locations are given as coordinates on a 1D line: x_1, x_2, ..., x_n.

You have C sensors, and you must place all of them at these locations 
(each location can hold at most one sensor). 

To avoid signal interference, you want to place the sensors such that 
the MINIMUM distance between any two sensors is as LARGE as possible.
What is the maximum possible value of this minimum distance?

[Input]
- First line: Two integers N and C (2 ≤ N ≤ 10^5, 2 ≤ C ≤ N)
- Second line: N integers representing the locations x_i (0 ≤ x_i ≤ 10^9)

[Output]
- A single integer: the maximum possible minimum distance.

[Example]
Input:
5, 3
1, 2, 8, 4, 9

Output:
3
(Explanation: If we place sensors at 1, 4, and 8, the distances are 
(4-1)=3 and (8-4)=4. The minimum distance is 3. 
If we place at 1, 2, 9, the minimum distance is (2-1)=1. 
The best we can do is 3.)

[Hint: How to use Binary Search on Answer]
1. We want to find the largest distance 'd' such that we can place 
   C sensors with at least 'd' distance between each.
2. If it's possible to place sensors with distance 'd', 
   can we do it with 'd-1'? Yes, definitely. 
   This monotonic property (Yes/No) is the key to Binary Search!
3. 'low' = 1, 'high' = 10^9 (max possible coordinate).
4. For a fixed 'mid', write a function 'can_place(mid)' that checks 
   if we can place C sensors with minimum distance 'mid'. 
   (Use Greedy for this check!)
"""

import sys
input = sys.stdin.readline

# 여기에 코드를 작성해 보세요!