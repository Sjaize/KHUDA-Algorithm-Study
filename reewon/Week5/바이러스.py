import sys
from collections import deque

n = int(sys.stdin.readline())
M = [[0 for _ in range(n)] for _ in range(n)]

e = int(sys.stdin.readline())
for i in range(e):
    x, y = map(int, input().split())
    M[x-1][y-1] = 1
    M[y-1][x-1] = 1

visited = [False] * n
visited[0] = True
q = deque()
q.append(0)
virus = 0

while q:
    X = q.popleft()
    for i in range(len(M[X])):
        if M[X][i] == 1 and visited[i] == False:
            q.append(i)
            visited[i] = True
            virus += 1

print(virus)
