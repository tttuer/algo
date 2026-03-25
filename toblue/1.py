"""
[Step 1: Task Scheduler (Greedy + Heap)]

여러 개의 과제가 있습니다. 각 과제는 '마감 기한'과 '점수'가 있습니다.
모든 과제는 수행하는 데 1의 시간이 걸립니다.
시간 0부터 시작해서, 마감 기한 내에 과제를 마쳐야 점수를 얻을 수 있습니다.
최대로 얻을 수 있는 점수의 합을 구하세요.

[입력 형식]
- n: 과제의 개수 (1 <= n <= 10^5)
- tasks: (마감 기한, 점수)의 리스트
  예: [(2, 100), (1, 50), (2, 70), (1, 20)]

[출력 형식]
- 최대 점수 합 (정수)

[힌트: 블루 레벨의 사고방식]
1. 먼저 과제를 '마감 기한'이 빠른 순서대로 정렬하세요.
2. 과제를 하나씩 확인하면서 일단 '우선순위 큐(Min-Heap)'에 넣습니다.
3. 만약 (큐에 들어있는 과제의 개수)가 (현재 과제의 마감 기한)보다 많아진다면?
   -> 지금 큐에 있는 과제들 중 '점수가 가장 낮은 놈'을 하나 버립니다!
   -> 그래야 더 가치 있는 과제를 할 시간을 확보할 수 있습니다.
"""

import sys
import heapq # 우선순위 큐를 위해 필요합니다

input = sys.stdin.readline

# 여기에 코드를 작성해 보세요!
n = int(input().strip())
tasks = []
for _ in range(n):
    due_date, score = map(int, input().strip().split(','))
    tasks.append((due_date, score))

tasks.sort(key=lambda x: x[0])

pq = []

day = 0
for due_date,score in tasks:
    heapq.heappush(pq, score)
    if len(pq) > due_date:
        heapq.heappop(pq)   

print(sum(pq))