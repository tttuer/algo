import sys
input = sys.stdin.readline

t = int(input())
answers = []
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    p = int(input())

    p -= 1

    goal = a[p]
    left = 0
    for i in range(p+1):
        if goal != a[i]:
            left += 1
            goal ^= 1
    
    goal = a[p]
    right = 0
    for i in range(n-1,p,-1):
        if goal != a[i]:
            right += 1
            goal ^= 1
    
    answer = max(left, right)
    if answer%2 == 1:
        answer += 1
    
    answers.append(answer)

print('\n'.join(map(str, answers)))