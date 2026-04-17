import sys
input = sys.stdin.readline

correct = input().strip()
smart = input().strip()

correct_answer = 0
for c in correct:
    if c == '+':
        correct_answer += 1
    elif c == '-':
        correct_answer -= 1

possibility = [0]

for s in smart:
    if s == '?':
        possi = []
        for p in possibility:
            possi.append(p+1)
            possi.append(p-1)
        possibility = possi
    else:
        for i in range(len(possibility)):
            if s == '+':
                possibility[i] += 1
            else:
                possibility[i] -= 1

ps = set(possibility)

answer = 0
for p in possibility:
    if p == correct_answer:
        answer += 1

print(answer/len(possibility))