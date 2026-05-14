import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    S = abs(x-y)

    if S == 0:
        print(1)
        answer = [1]*x+[-1]*y
        print(*answer)

    else:
        cnt = 0
        for i in range(1,int(math.sqrt(S)+1)):
            if S%i == 0:
                cnt += 1
                if S//i != i:
                    cnt += 1
        print(cnt)
        answer = [1]*x+[-1]*y
        print(*answer)

