import sys
input = sys.stdin.readline

t = int(input())

answers = []

for i in range(t):
    n = int(input())
    elems = list(map(int, input().split(' ')))

    posi = True if elems[0] > 0 else False
    best = elems[0]
    
    answer = 0
    
    for e in elems:
        if posi and e > 0:
            best = max(best, e)
        elif posi and e < 0:
            answer += best
            posi = False
            best = e
        elif not posi and e < 0:
            best = max(best, e)
        else:
            answer += best
            posi = True
            best = e
    
    answer += best
    answers.append(answer)
    
print('\n'.join(map(str, answers)))