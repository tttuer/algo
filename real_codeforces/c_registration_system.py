import sys
input = sys.stdin.readline

n = int(input().strip())

db = {}

for _ in range(n):
    name = input().strip()

    if name in db:
        number = db[name]
        db[name] = number + 1
        new_name = f'{name}{number}'
        db[new_name] = 1
        print(new_name)
    else:
        db[name] = 1
        print('OK')
