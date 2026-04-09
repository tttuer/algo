import sys
input = sys.stdin.readline

m,s = map(int, input().split(' '))

if s == 0 and m != 1:
    print('-1 -1')
elif s > 9*m:
    print('-1 -1')
else:
    max_answer = 0
    s1 = s
    multi = m-1
    while s1 > 0:
        n = min(9,s1)
        max_answer += (n*(10**multi))
        s1 -= n
        multi -= 1
    
    min_answer = 0
    s1 = s
    multi = 0
    last_s1 = s1
    while s1 > 0:
        n = min(9, s1)
        min_answer += (n*(10**multi))
        last_s1 = s1
        s1 -= n
        multi += 1
    if m > multi and last_s1 > 0:
        min_answer -= (1*(10**(multi-1)))
        min_answer += (1*(10**(m-1)))
    print(f'{min_answer} {max_answer}')