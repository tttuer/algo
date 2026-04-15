import sys
input = sys.stdin.readline

n,q = map(int, input().split(' '))
elems = list(map(int, input().split(' ')))

diff_arr = [0]*(n+1)

for _ in range(q):
    l,r = map(int, input().split(' '))

    diff_arr[l-1] += 1
    diff_arr[r] -= 1

for i in range(n):
    diff_arr[i+1] = diff_arr[i]+diff_arr[i+1]

elems.sort(reverse=True)
diff_arr.sort(reverse=True)

answer = 0

for i in range(n):
    answer += diff_arr[i]*elems[i]

print(answer)