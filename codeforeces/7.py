"""
[Problem: Sum and XOR - Harder version]

Given two integers S (Sum) and X (XOR Sum).
Construct an array 'A' of ANY length (minimum 1) such that:
1. Sum of elements = S
2. Bitwise XOR sum of elements = X
3. All elements must be POSITIVE integers (A_i > 0).

Find the array with the MINIMUM possible length.
If no such array exists, output -1.

[Example 1]
Input: S=10, X=10
Output: 10 (Length 1)

[Example 2]
Input: S=10, X=4
Output: 3, 3, 4 (Sum=10, XOR=4, Length 3)
*Note: [7, 3] also works (7+3=10, 7^3=4). So length 2 is better!
Answer: 7, 3

[Hint]
1. If S < X, it's impossible. (Sum is always >= XOR)
2. (S - X) must be an even number (2, 4, 6...). Why? 
   Because S = X + 2*(AND sum).
3. Think about the property: A + B = (A XOR B) + 2*(A AND B).
"""
