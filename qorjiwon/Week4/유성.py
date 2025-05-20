"""
반례 공유

입력
6 3
..X
...
#..
#..
#..
###

출력
...
...
#..
#..
#.X
###

"""

import sys
input = sys.stdin.readline

r, s = map(int, input().split())

m = [list(input().rstrip()) for _ in range(r)]

gap = r
bottom = -1
star_bottoms = [-1] * s

for j in range(s):
    star_bottom = -1
    land_top = r
    for i in range(r):
        if m[i][j] == 'X':
            star_bottom = i
        if m[i][j] == '#':
            land_top = i
            break
    if star_bottom == -1:
        continue
    gap = min(gap, land_top - star_bottom - 1)
    star_bottoms[j] = star_bottom
    bottom = max(bottom, star_bottom)
for j in range(s):
    if star_bottoms[j] == -1:
        continue
    for i in range(star_bottoms[j], -1, -1):
        m[i+gap][j] = m[i][j]
    for i in range(gap):
        m[i][j] = '.'

print(*[''.join(m[i]) for i in range(r)], sep='\n')