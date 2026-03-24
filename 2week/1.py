"""
[문제 설명]
괄호로 이루어진 문자열 s가 주어집니다. 괄호가 올바르게 닫혔는지 확인하여 True 또는 False를 반환하세요.

() 는 올바릅니다. (True)

()[] {} 도 올바릅니다. (True)

(] 는 올바르지 않습니다. (False)

([)] 도 순서가 잘못되어 올바르지 않습니다. (False)
"""


import sys

inputs = sys.stdin.readline().strip()


stack = []
pair = {
    ')': '(',
    ']': '[',
    '}': '{'
}

answer = True

for input in inputs:
    if len(stack) == 0 and input in ')]}':
        answer = False
        break
    if input in '([{':
        stack.append(input)
        continue
    last = stack.pop()
    if last != pair[input]:
        answer = False
        break

if len(stack) != 0:
    answer = False

print(answer)
