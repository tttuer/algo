import sys
input = sys.stdin.readline

n,l = map(int, input().split())
lanterns = list(map(int,input().split()))

lanterns.sort()

candidates = []

candidates.append(lanterns[0]-0)
candidates.append(l-lanterns[-1])

for i in range(n-1):
    diff = (lanterns[i+1]-lanterns[i])/2
    
    candidates.append(diff)

print(max(candidates))