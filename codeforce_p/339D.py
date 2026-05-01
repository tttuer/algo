import sys
input = sys.stdin.readline

n,m = map(int, input().split(' '))

size = 2**n
a = list(map(int, input().split(' ')))
tree = [0] * (2*size)

for i in range(size, 2*size):
    tree[i] = a[i-size]

step = size
is_or = True
while step > 1:
    half = step//2
    for i in range(half, step):
        if is_or:
            tree[i] = tree[i*2]|tree[i*2+1]
        else:
            tree[i] = tree[i*2]^tree[i*2+1]
    step = half
    is_or = not is_or

answers = []
for _ in range(m):
    p,b = map(int,input().split(' '))
    p -= 1
    
    tree[p+size] = b
    
    step = size+p
    is_or = True
    
    while step > 1:
        half = step//2
        
        tree[half] = tree[half*2]|tree[half*2+1] if is_or else tree[half*2]^tree[half*2+1]
        
        step = half
        is_or = not is_or
    
    answers.append(tree[1])
    
print('\n'.join(map(str, answers)))
