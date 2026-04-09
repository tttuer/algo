import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(' ')))

answer = 0
for i in range(n):
    for j in range(i,n):
        c_nums = [num for num in nums]
        for k in range(i,j+1):
            c_nums[k] = 1 if c_nums[k] == 0 else 0

        count = Counter(c_nums)
        
        answer = max(answer, count[1])

print(answer)