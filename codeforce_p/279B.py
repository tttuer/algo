import sys
input = sys.stdin.readline

n,t = map(int, input().split(' '))
times = list(map(int, input().split(' ')))

answer = 0
right = 0
cur = 0

for left in range(n):
    while right < n:
        cur += times[right]
        
        if cur > t:
            cur -= times[right]
            break
        answer = max(answer, right-left+1)
        right += 1
    cur -= times[left]

print(answer)