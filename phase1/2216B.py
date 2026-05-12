import sys
input =  sys.stdin.readline

t = int(input())
for _ in range(t):
    T,H,U = map(int, input().split())

    answer = 0
    if U > 0 and T > 0:
        TU = min(U,T)
        answer += TU * 4
        T -= TU
        U -= TU
    
    if H > 0 and T > 0:
        THT = min(H,T//2)
        answer += THT*7
        T -= THT*2
        H -= THT
    
    if H > 0 and T > 0:
        HT = min(H,T)
        answer += HT * 5
        T -= HT
        H -= HT
    
    if T > 0:
        answer += T*2+1
    
    answer += H*3 + U*3
    
    print(answer)