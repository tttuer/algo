import sys
input = sys.stdin.readline

n,k = map(int, input().split(' '))
elems = list(map(int, input().split(' ')))

elems.sort()

answer = elems[k-1]

if k == 0:
    if elems[0] == 1:
        print(-1)
    else:
        print(1)
elif k == n:
    print(elems[k-1])
elif answer == elems[k]:
    print(-1)
else:
    print(answer)