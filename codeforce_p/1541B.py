import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    a_dict = {}
    for i in range(n):
        a_dict[a[i]] = i+1
    
    answer = 0
    for i in range(n):
        ai = a[i]
        ii = i+1
        for j in range(1, 2*n//ai+1):
            jj = ai*j-ii
            if j in a_dict and a_dict[j] == jj and ii < jj:
                answer += 1
    
    print(answer)