import sys
input = sys.stdin.readline

n = int(input().strip())
boys = list(map(int, input().split(' ')))
m = int(input().strip())
girls = list(map(int, input().split(' ')))

boys.sort()
girls.sort()

i,j = 0,0
answer = 0

while i < n and j < m:
    b,g = boys[i], girls[j]

    cha = abs(b-g)

    if cha <= 1:
        answer += 1
        i += 1
        j += 1
    else:
        if b < g:
            i += 1
        else:
            j += 1

print(answer)