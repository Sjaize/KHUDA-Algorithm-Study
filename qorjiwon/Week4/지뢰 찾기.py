import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

n = int(input())

maps = [list(input().rstrip()) for _ in range(n)]
mine = [list(input().rstrip()) for _ in range(n)]

bomb = False
for i in range(n):
    for j in range(n):
        if mine[i][j] == 'x': # 오픈
            if maps[i][j] == '*': # 지뢰
                mine[i][j] = '*'
                bomb = True
                continue
            cnt = 0
            for k in range(8): # 주변 지뢰 세기
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == '*':
                    cnt += 1
            mine[i][j] = str(cnt)

if bomb: # 지뢰 터졌으면 모든 지뢰 표시
    mine = [['*' if maps[i][j] == '*' else '.' for j in range(n)] for i in range(n)]
        
for row in mine:
    print(''.join(row))
