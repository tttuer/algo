import sys
input = sys.stdin.readline

x = int(input())

divide = 1
answer = 0

while x // divide > 0:
    last = (x // (divide) % (10))

    if last >= 5:
        if (x // (divide * 10) == 0 and last == 9):
            answer += last * divide
        else:
            answer += (9-last) * divide
    else:
        answer += last * divide
    
    divide *= 10

print(answer)
