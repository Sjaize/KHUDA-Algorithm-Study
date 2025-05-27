from collections import deque
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs(trash, i, j, n, m):
    q = deque()
    q.append((i, j))
    trash[i][j] = 0
    size = 1

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            X = x + dx
            Y = y + dy
            if 0 <= X < n and 0 <= Y < m and trash[X][Y] == 1:
                size += 1
                trash[X][Y] = 0
                q.append((X, Y))
    return size


n, m, k = map(int, input().split())

trash = [[0 for _ in range(m)] for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    trash[x-1][y-1] = 1

max_size = 0
for i in range(n):
    for j in range(m):
        if trash[i][j] == 1:
            size = bfs(trash, i, j, n, m)
            if size > max_size:
                max_size = size

print(max_size)
