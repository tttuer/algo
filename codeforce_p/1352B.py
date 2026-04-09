import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int, input().split(' '))

    a,b = n//k, n%k

    if a == 0:
        print('No')
        continue
    else:
        if a % 2 == (a+b)%2:
            print('YES')
            answer = [a] * k
            answer[0] += b
            print(' '.join(map(str, answer)))
        else:
            if (k-1)%2 == 1:
                print('NO')
            else:
                if a == 1:
                    print('NO')
                    continue
                now = 1
                answer = [a] * k
                answer[k-1] += b
                for i in range(k-1):
                    answer[i] = answer[i] + now
                    now *= -1
                print('YES')
                print(' '.join(map(str, answer)))
