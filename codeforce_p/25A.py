import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split(' ')))

odd_even = {
    0: 0,
    1: 0,
}

odd_even_idx = {
    0: 0,
    1: 0,
}

for idx,number in enumerate(numbers):
    if number % 2 == 0:
        odd_even[0] += 1
        if odd_even[0] == 1:
            odd_even_idx[0] = idx
    else:
        odd_even[1] += 1
        if odd_even[1] == 1:
            odd_even_idx[1] = idx

if odd_even[0] == 1:
    print(odd_even_idx[0] + 1)
else:
    print(odd_even_idx[1] + 1)