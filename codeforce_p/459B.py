import sys
input = sys.stdin.readline

n = int(input())
beauties = list(map(int, input().split(' ')))

sorted_beauties = sorted(beauties)
beauties.sort(reverse=True)

diff = beauties[0] - sorted_beauties[0]

max_count = beauties.count(beauties[0])
min_count = beauties.count(sorted_beauties[0])

answer = 0

if diff != 0:
    answer = max_count * min_count
else:
    answer = n*(n-1)//2

print(f'{diff} {answer}')