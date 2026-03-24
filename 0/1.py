import sys
from collections import Counter

raw_inputs = sys.stdin.readline().strip()

words = [word.strip() for word in raw_inputs.split(',')]

count_dict = Counter(words)

max_key = max(count_dict, key=lambda k: count_dict[k])
max_value = count_dict[max_key]

print(max_key, max_value)
