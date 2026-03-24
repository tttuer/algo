


import sys

raw_inputs = sys.stdin.readline().strip()

nums = [int(word.strip()) for word in raw_inputs.split(',')]

target = int(sys.stdin.readline().strip())

dic = {}
for idx, num in enumerate(nums):
    goal = target - num
    if goal in dic:
        print([dic[goal], idx])
        break
    dic[num] = idx
    