"""
📝 문제 상황 (Problem Statement)배열 현황: $N$개의 0이 들어있는 배열 $A$가 있습니다.
업데이트 쿼리: 총 $Q$번의 명령이 주어집니다. 
각 명령은 $(L, R, V)$ 형태입니다.
"인덱스 $L$부터 $R$까지의 모든 숫자에 $V$를 더하라."
최종 목표: 모든 업데이트가 끝난 뒤의 최종 배열을 출력하세요.
"""

import sys
input = sys.stdin.readline

n = int(input().strip())
q = int(input().strip())

prefix_sum = [0] * (n+1)

for _ in range(q):
    l,r,v = map(int, input().strip().split(','))

    prefix_sum[l] += v
    if r+1 < n:
        prefix_sum[r+1] -= v

a = [0] * n

answer = 0
for i in range(n):
    answer += prefix_sum[i]
    a[i] = answer

print(a)
