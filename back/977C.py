import sys
input = sys.stdin.readline

n,k = map(int, input().split())
a = [0] + list(map(int, input().split()))

a.sort()

x = a[k]

if k == 0:
    if a[1] == 1:
        print(-1)
    else:
        print(1)
elif a.count(x) > 1:
    print(-1)
else:
    print(x)