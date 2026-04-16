import sys
input = sys.stdin.readline

t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    ski = list(map(int, input().split(' ')))
    movie = list(map(int, input().split(' ')))
    board = list(map(int, input().split(' ')))

    s = [(e,i) for i,e in enumerate(ski)]
    m = [(e,i) for i,e in enumerate(movie)]
    b = [(e,i) for i,e in enumerate(board)]
    
    s.sort(reverse=True)
    m.sort(reverse=True)
    b.sort(reverse=True)
    
    answer = 0
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if s[i][1] == m[j][1] or s[i][1] == b[k][1] or m[j][1] == b[k][1]:
                    continue
                answer = max(answer, s[i][0]+m[j][0]+b[k][0])
    
    answers.append(answer)
    
print('\n'.join(map(str, answers)))