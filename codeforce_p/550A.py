import sys
input = sys.stdin.readline

s = input().strip()

ab = s.find('AB')
ba = s.find('BA')

if ab == -1 or ba == -1:
    print('NO')
else:
    possible = False
    if abs(ab-ba) > 1:
        possible = True
    if abs(ab-ba) == 1:
        ab1 = s.find('AB', ba+2)
        ba1 = s.find('BA', ab+2)

        if ab1 != -1:
            possible = True
        if ba1 != -1:
            possible = True
    
    print('YES' if possible else 'NO')