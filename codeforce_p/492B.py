import sys 
input = sys.stdin.readline

n,l = map(int, input().split(' '))

lanterns = [0]

ls = list(map(int, input().split(' ')))

[lanterns.append(s) for s in ls]

lanterns.append(l)
lanterns.sort()

answer = 0

for i in range(len(lanterns) - 1):
    diff = lanterns[i+1] - lanterns[i]
    if (i == 0 or i == len(lanterns) - 2):
        answer = max(answer, diff)

    if diff > answer * 2:
        answer = max(answer, diff/2)

print(answer)


