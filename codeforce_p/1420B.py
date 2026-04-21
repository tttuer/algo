import sys
input = sys.stdin.readline

def two(n):
    result = 0
    while n//2 != 0:
        result += 1
        n = n//2
    return result

def nn(n):
    return n*(n-1)//2

answers = []

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    counts = {}
    
    for i in a:
        count = two(i)
        if count in counts:
            counts[count] += 1
        else:
            counts[count] = 1
    
    answer = 0
    for k in counts:
        answer += nn(counts[k])
    
    answers.append(answer)
    
print('\n'.join(map(str, answers)))