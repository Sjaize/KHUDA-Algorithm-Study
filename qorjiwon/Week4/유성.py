R, S = map(int, input().split())

p = []
for _ in range(R):
    p.append(list(input()))

gap = R-1
uuidx = 0
for x in range(S):
    uidx = -1
    didx = R-1
    for y in range(R-2, -1, -1):
        if(p[y][x] == 'X'):
            uidx = y
            break
    for y in range(0, R-1):
        if (p[y][x] == '#'):
            didx = y
            break
    if (uidx == -1):
        continue
    gap = min(abs(uidx-didx), gap)
    uuidx = max(uuidx, uidx)
gap -= 1

for y in range(uuidx, -1, -1):
    for x in range(S):
        if(p[y+gap][x] !='#'):
            p[y+gap][x] = p[y][x]

for y in range(gap):
    for x in range(S):
        if(p[y][x] == 'X'):
            p[y][x] = '.'

for a in p:
    for b in a:
        print(b,end='')
    print()
