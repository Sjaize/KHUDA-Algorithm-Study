import sys
input = sys.stdin.readline

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

m = [list(map(int, input().rstrip().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if m[i][j]:
            for k in range(4):
                cnt = 1
                for l in range(1, 6):
                    nx = i + dx[k]*l
                    ny = j + dy[k]*l
                    if 0 <= nx < 19 and 0 <= ny < 19 and m[nx][ny] == m[i][j]:
                        cnt += 1
                if cnt == 5:
                    print(f'{m[i][j]}\n{i + 1} {j + 1}')
                    exit()
