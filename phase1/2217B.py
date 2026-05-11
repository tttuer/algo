import sys
input = sys.stdin.readline

t = int(input())

def is_done(arr, goal):
    return all(v == goal for v in arr)

for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    p = int(input())
    goal = arr[p-1]
    
    left = 0
    now_goal = goal
    for i in range(p):
        if arr[i] != now_goal:
            left += 1
            now_goal ^= 1
    right = 0
    now_goal = goal
    for i in range(n-1,p-1,-1):
        if arr[i] != now_goal:
            right += 1
            now_goal ^= 1
    
    answer = max(left,right)
    if answer%2 == 1:
        answer += 1
    
    print(answer)