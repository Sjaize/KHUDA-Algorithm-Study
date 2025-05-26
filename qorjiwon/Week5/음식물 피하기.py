import sys
input = sys.stdin.readline

from collections import deque

N, M, K = map(int, input().split())
m = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    m[r-1][c-1] = 1

ans = 0
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(N):
    for j in range(M):
        if m[i][j]:
            m[i][j] = 0
            size = 1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and m[nx][ny]:
                        m[nx][ny] = 0
                        q.append((nx, ny))
                        size += 1
            ans = max(ans, size)
print(ans)