import sys
input = sys.stdin.readline

t = int(input())

def is_ugly(p):
    ugly = 0
    
    for i in range(len(p)):
        if i+1 == max(p[0:i+1]):
            ugly += 1
    
    return ugly == 1
        

for _ in range(t):
    n = int(input())
    p = list(map(int,input().split(' ')))
    
    if is_ugly(p):
            print(' '.join(map(str, p)))    
    else:
        done = False
        for i in range(n):
            for j in range(i+1,n):
                pp = [v for v in p]
                temp = pp[i]
                pp[i] = pp[j]
                pp[j] = temp
                if is_ugly(pp):
                    print(' '.join(map(str, pp)))
                    done = True
                    break
            if done:
                break