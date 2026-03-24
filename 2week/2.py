"""
[문제 설명]
프린터기에 여러 개의 문서가 쌓여 있습니다. 각 문서에는 **중요도(숫자가 높을수록 중요)**가 붙어 있습니다.

맨 앞의 문서(A)를 꺼냅니다.

나머지 문서들 중에 A보다 중요도가 높은 문서가 단 하나라도 있으면, A를 다시 맨 뒤로 보냅니다.

그렇지 않으면(A가 가장 중요하다면) 바로 인쇄합니다.

내가 인쇄를 요청한 문서가 현재 몇 번째 위치에 있는지(target) 주어질 때, 그 문서가 몇 번째로 인쇄되는지 구하세요.

입력 예시:

중요도: [2, 1, 3, 2], 내 문서의 위치(target): 2 (중요도 3인 문서)

출력 예시:

1 (중요도가 3인 문서가 가장 먼저 인쇄되므로)
"""
import sys
from collections import deque

raw_inputs = sys.stdin.readline().strip()

priorities = [int(num) for num in raw_inputs.split(',')]

target = int(sys.stdin.readline().strip())

d = deque()

t = priorities[target]

s_p = deque(priorities.sorted(reverse=True))

for i, n in enumerate(priorities):
    d.append((n,i))

answer = -1
while True:
    num, idx = d.popleft()
    next_pop_num = s_p.popleft()

    if next_pop_num != num:
        d.append((num, idx+1))
        s_p.appendleft(next_pop_num)
        continue
    
    if num == t:
        answer = idx + 1
        break

print(answer)