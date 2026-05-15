import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    T,H,U = map(int, input().split())

    TU = min(T,U)

    answer = 0
    if TU > 0:
        answer += TU*4
        T -= TU
        U -= TU

    THT = min(H,T//2)
    if THT > 0:
        answer += THT*7
        T -= THT*2
        H -= THT
    
    TH = min(T,H)
    if TH > 0:
        answer += TH*5
        T -= TH
        H -= TH
    
    if T > 0:
        answer += T*2+1
    
    answer += H*3 + U*3

    print(answer)