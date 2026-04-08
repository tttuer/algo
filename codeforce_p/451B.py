import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split(' ')))

left,right = 0,n-1

while left+1 < n and array[left] < array[left+1]:
    left += 1

while right-1 >= 0 and array[right] > array[right-1]:
    right -= 1

canAnswer = True

for i in range(left,right):
    if array[i] < array[i+1]:
        canAnswer = False
        break

if left > 0 and array[right] < array[left-1]:
    canAnswer = False

if right < n-1 and array[left] > array[right+1]:
    canAnswer = False

if left == n-1 and right == 0:
    canAnswer = True
    left = right

if canAnswer:
    print('yes')
    print(f'{left+1} {right+1}')
else:
    print('no')