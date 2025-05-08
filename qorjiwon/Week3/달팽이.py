import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0

n = int(input())
num = n * n
find_num = int(input())
arr = [[0] * n for _ in range(n)]
x, y = -1, 0

while num:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx > -1 and nx < n and ny > -1 and ny < n and not arr[nx][ny]:
        arr[nx][ny] = num
        x, y = nx, ny
        num -= 1
    else:
        d = (d+1)%4

for li in arr:
    print(*li)

for i in range(n):
    for j in range(n):
        if arr[i][j] == find_num:
            print(i+1, j+1)
            sys.exit(0)