import sys
from collections import Counter
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    numbers = list(map(int, input().split(' ')))

    subs = [(v-i) for i,v in enumerate(numbers)]
    
    counts = Counter(subs)
    
    answer = 0
    
    for i in counts:
        v = counts[i] - 1
        
        answer += v*(v+1)//2
    
    print(answer)
        