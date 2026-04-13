import sys
input = sys.stdin.readline

n,m = map(int, input().split(' '))

p,g = (n//m),(n%m)

max_num = ((n-m+1)*(n-m))//2
min_num = (m-g) * (p*(p-1))//2 + (g) * ((p+1)*p)//2

print(min_num, max_num, sep=' ')