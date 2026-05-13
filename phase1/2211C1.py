import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b_cnt = Counter(b)
    if any(k > 0 and b_cnt[k] > 1 for k in b_cnt):
        print('no')
    else:
        left,right = 0,k

        result = True
        while right < n:
            if b[left] != -1 and a[left] != b[left]:
                result = False
            
            if b[right] != -1 and a[right] != b[right]:
                result = False
            
            left += 1
            right += 1
        
        mids = set(a[n-k:k])
        for i in range(n-k, k):
            if b[i] != -1 and b[i] not in mids:
                result = False
        
        print('yes' if result else 'no')