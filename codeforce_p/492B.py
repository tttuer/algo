import sys 
input = sys.stdin.readline

n,l = map(int, input().split(' '))
lanterns = list(map(int, input().split(' ')))

lanterns.sort()

left,right = 0, l

def check(mid):
    if lanterns[0] - mid > 0:
        return False
    for i in range(n-1):
        diff = lanterns[i+1] - lanterns[i]

        if diff > mid*2:
            return False
    if lanterns[n-1] + mid < l:
        return False
    return True


answer = 0

while left < right:
    mid = (left+right) / 2
    print(mid)

    if check(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)