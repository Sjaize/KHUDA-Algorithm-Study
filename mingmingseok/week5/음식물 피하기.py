import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1

visited = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max = 0

def find(list):
    for i in range(n):
        for j in range(m):
            if list[i][j] == 1:
                return i, j
    return None

def bfs(x, y):
    max = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = 0
                max += 1
                q.append((nx, ny))
    return max

while True:
    pos = find(graph)
    if pos is None:
        break
    i, j = pos
    cnt = bfs(i, j)
    if cnt > max:
        max = cnt

print(max)
